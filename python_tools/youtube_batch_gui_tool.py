import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
import yt_dlp
import whisper
import datetime
import tempfile
import shutil
import time

# Whisper 模型加载（默认使用 base 模型）
model = whisper.load_model("base")

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube 视频&字幕下载工具（支持本地字幕生成）")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # URL 输入
        self.url_label = tk.Label(self.root, text="YouTube 视频链接（可多条）：")
        self.url_label.pack(anchor="w")
        self.url_entry = tk.Text(self.root, height=5)
        self.url_entry.pack(fill="x")

        # 下载选项
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(fill="x", pady=5)
        self.subtitles_var = tk.BooleanVar(value=True)
        self.embed_subtitles_var = tk.BooleanVar(value=False)

        tk.Checkbutton(self.options_frame, text="下载字幕", variable=self.subtitles_var).pack(side="left")
        tk.Checkbutton(self.options_frame, text="合并字幕进视频", variable=self.embed_subtitles_var).pack(side="left")

        # 下载按钮
        self.download_button = tk.Button(self.root, text="开始下载（多线程）", command=self.start_download_thread)
        self.download_button.pack(pady=5)

        # 本地视频字幕生成按钮
        self.local_button = tk.Button(self.root, text="上传本地视频生成中英文字幕", command=self.generate_local_subtitles_thread)
        self.local_button.pack(pady=5)

        # 日志输出
        self.log_output = scrolledtext.ScrolledText(self.root, height=20)
        self.log_output.pack(fill="both", expand=True, pady=5)

    def log(self, msg):
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S] ")
        self.log_output.insert(tk.END, timestamp + msg + "\n")
        self.log_output.see(tk.END)

    def start_download_thread(self):
        threading.Thread(target=self.download_videos, daemon=True).start()

    def download_videos(self):
        urls = self.url_entry.get("1.0", tk.END).strip().splitlines()
        for url in urls:
            if url.strip():
                self.download_video(url.strip())

    def download_video(self, url):
        self.log(f"开始下载：{url}")
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'writesubtitles': self.subtitles_var.get(),
            'writeautomaticsub': self.subtitles_var.get(),
            'subtitleslangs': ['en', 'zh-Hans'],
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }

        if self.embed_subtitles_var.get():
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegEmbedSubtitle'
            })

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                self.log(f"✅ 下载完成：{url}")
            except Exception as e:
                self.log(f"❌ 下载失败：{e}")

    def generate_local_subtitles_thread(self):
        threading.Thread(target=self.generate_local_subtitles, daemon=True).start()

    def generate_local_subtitles(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.mov *.avi")])
        if not filepath:
            return
        self.log("🎞️ 已选择视频：" + filepath)

        temp_dir = tempfile.mkdtemp()
        audio_path = os.path.join(temp_dir, "audio.wav")
        ffmpeg_cmd = f'ffmpeg -y -i "{filepath}" -ar 16000 -ac 1 -c:a pcm_s16le "{audio_path}"'
        subprocess.run(ffmpeg_cmd, shell=True)
        self.log("🔊 音频提取完成")

        # 语言检测
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        _, probs = model.detect_language(mel)
        lang = max(probs, key=probs.get)
        self.log(f"🌍 检测到语言：{lang}")

        # 字幕识别
        try:
            result = model.transcribe(audio_path)
            self.log("📝 字幕转录完成")
        except Exception as e:
            self.log(f"❌ 字幕转录失败：{e}")
            shutil.rmtree(temp_dir)
            return
        
        segments = result['segments']
        self.log(f"🧩 字幕段数量：{len(segments)}")

        if lang == 'zh':
            self.write_srt(segments, filepath + ".zh.srt")
            self.write_translated_srt(segments, filepath + ".en.srt", 'en')
        else:
            self.write_srt(segments, filepath + ".en.srt")
            self.write_translated_srt(segments, filepath + ".zh.srt", 'zh')

        self.log("✅ 字幕生成完成！")
        shutil.rmtree(temp_dir)

    def write_srt(self, segments, path):
        with open(path, "w", encoding="utf-8") as f:
            for seg in segments:
                start = self.format_timestamp(seg['start'])
                end = self.format_timestamp(seg['end'])
                f.write(f"{seg['id']+1}\n{start} --> {end}\n{seg['text']}\n\n")

    def write_translated_srt(self, segments, path, to_lang):
        with open(path, "w", encoding="utf-8") as f:
            for seg in segments:
                translated = self.fake_translate(seg['text'], to_lang)
                start = self.format_timestamp(seg['start'])
                end = self.format_timestamp(seg['end'])
                f.write(f"{seg['id']+1}\n{start} --> {end}\n{translated}\n\n")

    def fake_translate(self, text, to_lang):
        return f"[{to_lang.upper()}] {text}"  # TODO: 替换为真实翻译 API

    def format_timestamp(self, seconds: float) -> str:
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds - int(seconds)) * 1000)
        return f"{h:02}:{m:02}:{s:02},{ms:03}"

if __name__ == '__main__':
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
