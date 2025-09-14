from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from handlers import get_price, start

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", get_price))

if __name__ == "__main__":
    print("✅ Бот запущен. Жди команд...")
    app.run_polling()
