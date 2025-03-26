from dotenv import load_dotenv
import os
from pathlib import Path
from openai import OpenAI

# 加载 .env 文件中的环境变量
load_dotenv()
# 读取 API Key
api_key = os.getenv("OPENAI_API_KEY")

# 确保 API Key 存在
if not api_key:
    raise ValueError("Missing API Key! Please check your .env file.")
# 初始化 OpenAI 客户端
client = OpenAI(api_key=api_key)


speech_file_path = Path(__file__).parent / "speech.mp3"
# response = client.audio.speech.create(
#   model="gpt-4o-mini-tts",
#   voice="coral",
#   input="Today is a wonderful day to build something people love!",
#   # instructions="Speak in a cheerful and positive tone.",
# )
# response.stream_to_file(speech_file_path)

# 生成语音
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Today is a wonderful day to build something people love!",
)

# 保存到文件
response.with_streaming_response.method(speech_file_path)

print(f"Speech saved to {speech_file_path}")
