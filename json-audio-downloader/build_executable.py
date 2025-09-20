#!/usr/bin/env python3
"""
构建可执行文件的脚本
使用PyInstaller将Python程序打包成独立的可执行文件
"""

import os
import sys
import subprocess

def build_executable():
    """构建可执行文件"""
    
    # 检查是否安装了PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("正在安装PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # PyInstaller命令
    cmd = [
        "pyinstaller",
        "--onefile",  # 打包成单个文件
        "--windowed",  # Windows下隐藏控制台窗口
        "--name=JSON-Audio-Downloader",  # 可执行文件名
        "--icon=icon.ico",  # 图标文件（如果有的话）
        "main.py"
    ]
    
    # 如果没有图标文件，移除图标参数
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    print("开始构建可执行文件...")
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ 构建成功！")
        print("可执行文件位置: dist/JSON-Audio-Downloader")
        if sys.platform == "win32":
            print("Windows用户: dist/JSON-Audio-Downloader.exe")
    except subprocess.CalledProcessError as e:
        print(f"❌ 构建失败: {e}")
        return False
    
    return True

if __name__ == "__main__":
    build_executable()