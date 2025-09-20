#!/usr/bin/env python3
"""
JSON Audio Downloader
A simple GUI tool for downloading audio files from JSON data.
Perfect for downloading audio content from GitHub projects and other sources.

Author: [Your Name]
Version: 1.0.0
License: MIT
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import os
import requests
import re
import threading
import time
from pathlib import Path

class AudioDownloader:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui()
        self.download_thread = None
        self.is_downloading = False
        
    def setup_ui(self):
        """设置用户界面"""
        self.root.title("JSON Audio Downloader v1.0")
        self.root.geometry("500x350")
        self.root.resizable(True, True)
        
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="JSON Audio Downloader", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 说明文本
        desc_label = ttk.Label(main_frame, 
                              text="Select a JSON file containing audio URLs and choose download location",
                              font=("Arial", 10))
        desc_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # 文件选择
        ttk.Label(main_frame, text="JSON File:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.file_var = tk.StringVar()
        file_entry = ttk.Entry(main_frame, textvariable=self.file_var, width=40)
        file_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        ttk.Button(main_frame, text="Browse", 
                  command=self.select_json_file).grid(row=2, column=2, padx=(5, 0))
        
        # 下载目录选择
        ttk.Label(main_frame, text="Download to:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.dir_var = tk.StringVar()
        dir_entry = ttk.Entry(main_frame, textvariable=self.dir_var, width=40)
        dir_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        
        ttk.Button(main_frame, text="Browse", 
                  command=self.select_download_dir).grid(row=3, column=2, padx=(5, 0))
        
        # 进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, 
                                           maximum=100, length=300)
        self.progress_bar.grid(row=4, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # 状态标签
        self.status_var = tk.StringVar(value="Ready to download")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # 下载按钮
        self.download_btn = ttk.Button(main_frame, text="Start Download", 
                                      command=self.start_download)
        self.download_btn.grid(row=6, column=0, columnspan=3, pady=20)
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def select_json_file(self):
        """选择JSON文件"""
        filepath = filedialog.askopenfilename(
            title="Select JSON file",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if filepath:
            self.file_var.set(filepath)
            
    def select_download_dir(self):
        """选择下载目录"""
        directory = filedialog.askdirectory(title="Select download directory")
        if directory:
            self.dir_var.set(directory)
            
    def sanitize_filename(self, filename):
        """清理文件名中的非法字符"""
        return re.sub(r'[<>:"/\\|?*]', '_', filename)
        
    def extract_audio_info(self, item, index):
        """从JSON项目中提取音频信息"""
        # 支持多种JSON格式
        article_name = (item.get("article") or 
                       item.get("title") or 
                       item.get("name") or 
                       f"audio_{index}")
        
        url = (item.get("url") or 
               item.get("audio_url") or 
               item.get("link"))
        
        if not url:
            raise ValueError(f"No URL found in item {index}")
            
        return self.sanitize_filename(article_name), url
        
    def download_single_file(self, url, filepath, headers, max_retries=3):
        """下载单个文件，支持重试"""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, stream=True, timeout=30)
                response.raise_for_status()
                
                with open(filepath, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)
                return True
                
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"Failed to download after {max_retries} attempts: {e}")
                    return False
                time.sleep(2)  # 等待2秒后重试
        return False
        
    def download_audio_files(self):
        """下载音频文件的主要逻辑"""
        try:
            json_file = self.file_var.get()
            download_dir = self.dir_var.get()
            
            if not json_file or not download_dir:
                messagebox.showerror("Error", "Please select both JSON file and download directory")
                return
                
            # 读取JSON文件
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            if not isinstance(data, list):
                messagebox.showerror("Error", "JSON file should contain an array of items")
                return
                
            total_files = len(data)
            successful_downloads = 0
            failed_downloads = []
            
            # 设置请求头
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'audio/*,*/*;q=0.9'
            }
            
            for index, item in enumerate(data, start=1):
                if not self.is_downloading:  # 检查是否被取消
                    break
                    
                try:
                    article_name, url = self.extract_audio_info(item, index)
                    filename = os.path.join(download_dir, f"{index:03d}_{article_name}.mp3")
                    
                    # 检查文件是否已存在
                    if os.path.exists(filename):
                        self.status_var.set(f"Skipping existing file: {article_name}")
                        successful_downloads += 1
                    else:
                        self.status_var.set(f"Downloading: {article_name}")
                        
                        if self.download_single_file(url, filename, headers):
                            successful_downloads += 1
                            print(f"Downloaded: {article_name}")
                        else:
                            failed_downloads.append(article_name)
                            print(f"Failed: {article_name}")
                    
                    # 更新进度条
                    progress = (index / total_files) * 100
                    self.progress_var.set(progress)
                    self.root.update_idletasks()
                    
                except Exception as e:
                    failed_downloads.append(f"Item {index}: {str(e)}")
                    print(f"Error processing item {index}: {e}")
            
            # 显示结果
            if self.is_downloading:  # 只有在没有被取消的情况下显示结果
                result_msg = f"Download completed!\n\nSuccessful: {successful_downloads}\nFailed: {len(failed_downloads)}"
                if failed_downloads:
                    result_msg += f"\n\nFailed items:\n" + "\n".join(failed_downloads[:5])
                    if len(failed_downloads) > 5:
                        result_msg += f"\n... and {len(failed_downloads) - 5} more"
                
                messagebox.showinfo("Download Complete", result_msg)
                self.status_var.set("Download completed")
            else:
                self.status_var.set("Download cancelled")
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error occurred")
        finally:
            self.is_downloading = False
            self.download_btn.config(text="Start Download")
            self.progress_var.set(0)
            
    def start_download(self):
        """开始或取消下载"""
        if not self.is_downloading:
            self.is_downloading = True
            self.download_btn.config(text="Cancel Download")
            self.download_thread = threading.Thread(target=self.download_audio_files)
            self.download_thread.daemon = True
            self.download_thread.start()
        else:
            self.is_downloading = False
            self.download_btn.config(text="Start Download")
            self.status_var.set("Cancelling...")
            
    def run(self):
        """运行应用程序"""
        self.root.mainloop()

def main():
    """主函数，用于命令行调用"""
    app = AudioDownloader()
    app.run()

if __name__ == "__main__":
    main()