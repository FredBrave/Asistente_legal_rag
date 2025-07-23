import asyncio
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from app.config import TELEGRAM_BOT_TOKEN
from app.rag_engine import responder_pregunta

async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = update.message.text
    respuesta = responder_pregunta(pregunta)
    await update.message.reply_text(respuesta)

def iniciar_bot():
    async def main():
        app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("Bot de Telegram activo")
        await app.run_polling()

    asyncio.run(main())

def iniciar_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(iniciar_bot_async())