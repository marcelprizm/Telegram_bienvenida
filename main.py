import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Falta el BOT_TOKEN. Asegúrate de configurarlo en Render.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Bienvenido/a al ecosistema Concilium!\n\nEstamos construyendo el futuro de la descentralización. Pronto recibirás más información."
    )

if __name__ == "__main__":
    print("Bot Concilium iniciado en Render...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()