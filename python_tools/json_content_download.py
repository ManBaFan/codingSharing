import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import requests

# graphic interface that download audio of economist
def download_audio():
    try:
        # Open the JSON file
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not filepath:
            return

        with open(filepath, 'r') as file:
            data = json.load(file)

        # Ask for a download directory
        download_dir = filedialog.askdirectory()
        if not download_dir:
            return

        # Download all audio files
        # for item in data:
        for index,item in enumerate(data, start=1):
            article_name = item["article"]
            url = item["url"]
            # Get the audio file name
            filename = os.path.join(download_dir, f"{index}_{article_name}.mp3")
            # Download the file
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as audio_file:
                    audio_file.write(response.content)
                print(f"Downloaded: {index}_{article_name}")
            else:
                print(f"Failed to download: {index}_{article_name}")
        
        messagebox.showinfo("Success", "All audio files have been downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Audio Downloader")
root.geometry("400x200")

# Add a button to trigger the download
download_button = tk.Button(root, text="Download Audio from JSON", command=download_audio, font=("Arial", 14))
download_button.pack(pady=50)

# Start the application
root.mainloop()
