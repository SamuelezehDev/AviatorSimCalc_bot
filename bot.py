import os
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8525646107:AAF3kRA7UBNkgRLKb4P0TBm-nnNvbPkRGGE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /signal to get the latest round multiplier simulation."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Simulated multiplier generation logic
    multiplier = round(random.uniform(1.01, 3.50), 2)
    await update.message.reply_text(f"📊 Next Signal Multiplier: {multiplier}x")

def main():
    if not TOKEN:
        print("Error: BOT_TOKEN environment variable not set.")
        return

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))

    print("Bot is polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
