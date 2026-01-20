# telegram_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN

BOT_RUNNING = True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 MemeCoin Bot е активен!\n"
        "/status – статус\n"
        "/continue – продължи търговията\n"
        "/stop – спри бота"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Ботът работи. Балансът се обновява.")

async def continue_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_RUNNING
    BOT_RUNNING = True
    await update.message.reply_text("▶️ Ботът продължава работа.")

async def stop_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_RUNNING
    BOT_RUNNING = False
    await update.message.reply_text("⏸️ Ботът е спрян.")

def run_telegram_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("continue", continue_bot))
    app.add_handler(CommandHandler("stop", stop_bot))

    print("🤖 Telegram bot started")
    app.run_polling()
