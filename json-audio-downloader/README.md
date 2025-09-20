# JSON Audio Downloader

一个简单易用的GUI工具，用于从JSON文件中批量下载音频文件。特别适合下载GitHub项目中的音频资源。

## 功能特点

- 🎵 支持从JSON文件批量下载音频
- 🖥️ 简洁直观的图形界面
- 📊 实时进度显示
- 🔄 自动重试机制
- 📁 智能文件命名
- ⏸️ 支持取消下载
- 🛡️ 跳过已存在的文件

## 安装方法

### 方法1: 直接运行（推荐）
1. 确保已安装Python 3.7+
2. 下载项目文件
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行程序：
   ```bash
   python main.py
   ```

### 方法2: 使用pip安装
```bash
pip install json-audio-downloader
json-audio-downloader
```

## 使用方法

1. **选择JSON文件**：点击"Browse"按钮选择包含音频链接的JSON文件
2. **选择下载目录**：选择音频文件的保存位置
3. **开始下载**：点击"Start Download"开始批量下载

## JSON文件格式

工具支持多种JSON格式，例如：

```json
[
  {
    "article": "音频标题1",
    "url": "https://example.com/audio1.mp3"
  },
  {
    "title": "音频标题2",
    "audio_url": "https://example.com/audio2.mp3"
  },
  {
    "name": "音频标题3",
    "link": "https://example.com/audio3.mp3"
  }
]
```

支持的字段名：
- 标题字段：`article`, `title`, `name`
- URL字段：`url`, `audio_url`, `link`

## 常见用途

- 下载播客节目
- 批量获取音频教程
- 从GitHub项目下载音频资源
- 音频资料收集整理

## 系统要求

- Python 3.7 或更高版本
- 网络连接
- 支持的操作系统：Windows, macOS, Linux

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v1.0.0
- 初始版本发布
- 基础GUI界面
- 批量下载功能
- 进度显示
- 错误处理

---

如果这个工具对你有帮助，请给个⭐️支持一下！