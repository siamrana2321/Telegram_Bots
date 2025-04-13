import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = '7893316729:AAFeu2dD1lx4k8Xirx7jNr9k0VeJ-uP5eE8'

# Function to download YouTube video or playlist
async def download_youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    await update.message.reply_text("Downloading... Please wait.")

    ydl_opts = {
    'outtmpl': 'downloads/%(title).70s.%(ext)s',  # Trim long names
    'format': 'best[ext=mp4]/best',               # safest format for Telegram
    'merge_output_format': 'mp4',
    'noplaylist': False,
    'ignoreerrors': True,
    'quiet': True,
    'no_warnings': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if 'entries' in info:  # It's a playlist
                for entry in info['entries']:
                    if entry is None:
                        continue
                    file_path = ydl.prepare_filename(entry)
                await send_file(update, file_path)
            else:  # Single video
                file_path = ydl.prepare_filename(info)
                await send_file(update, file_path)

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Helper function to send file
async def send_file(update, file_path):
    if os.path.exists(file_path):
        await update.message.reply_text(f"Download Complete.")
            


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send a YouTube video or playlist URL to download.")

# Main function to run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_youtube))

    print("Bot is running...")
    app.run_polling()
