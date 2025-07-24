import threading
import asyncio # <--- Make sure this import is present
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from app.config import TELEGRAM_BOT_TOKEN
from app.rag_engine import responder_pregunta

async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
    print("Mensaje recibido:", update.message.text)
    pregunta = update.message.text
    respuesta = responder_pregunta(pregunta)
    print("Respuesta generada:", respuesta)
    await update.message.reply_text(respuesta)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app_telegram = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app_telegram.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot de Telegram activo")
    loop.run_until_complete(app_telegram.run_polling())

def iniciar_bot():
    thread = threading.Thread(target=run_bot, daemon=True)
    thread.start()