from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from app.rag_engine import responder_pregunta
from app.config import TELEGRAM_BOT_TOKEN

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = update.message.text
    respuesta = responder_pregunta(pregunta)
    await update.message.reply_text(respuesta)

def iniciar_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()