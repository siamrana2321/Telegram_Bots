# 🎥 YouTube Video Downloader Telegram Bot

A Telegram bot built with Python that allows users to download YouTube videos or entire playlists by simply sending a link.

## 🚀 Features

- Download single YouTube videos
- Download full playlists
- Automatically converts to MP4 (best format for Telegram)
- Auto trims long video names to avoid errors
- Sends confirmation after download completes

## 📦 Requirements

- Python 3.7+
- Telegram Bot Token from [BotFather](https://t.me/BotFather)

### Python Dependencies

Install the required Python packages with:

```bash
pip install python-telegram-bot yt-dlp
```

You may also need FFmpeg installed on your system for video conversion:

- Windows: [FFmpeg Download](https://ffmpeg.org/download.html)
- macOS: `brew install ffmpeg`
- Linux (Debian/Ubuntu): `sudo apt install ffmpeg`

## 🛠 Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/telegram-youtube-downloader-bot.git
cd telegram-youtube-downloader-bot
```

2. Replace `'YOUR_BOT_TOKEN_HERE'` in the script with your actual Telegram bot token.

```python
BOT_TOKEN = 'YOUR_ACTUAL_BOT_TOKEN'
```

3. Create a `downloads` directory (optional but recommended):

```bash
mkdir downloads
```

4. Run the bot:

```bash
python bot.py
```

## 💬 How to Use

- Start the bot with `/start`
- Send any valid YouTube video or playlist URL
- The bot will download the video(s) and reply once done

> ⚠️ Note: This bot only sends confirmation after download. You can extend it to send the actual file if it's within Telegram's file size limit (currently 2GB).

## 📁 Directory Structure

```
.
├── bot.py            # Main bot script
├── downloads/        # Directory where videos are saved
└── README.md         # This file
```

## 📌 Notes

- Playlist videos are downloaded one by one.
- Errors are silently ignored for problematic videos.
- Long video titles are trimmed to avoid filename issues.
