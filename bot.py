from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from handlers import get_price, start

async def main():
    
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", get_price))

    
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
