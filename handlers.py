# handlers.py

import requests
from telegram import Update
from telegram.ext import ContextTypes
from config import BINANCE_API_URL

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Напиши тикер, например: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    url = f"{BINANCE_API_URL}/api/v3/ticker/24hr?symbol={symbol}"

    try:
        response = requests.get(url)
        data = response.json()

        if "code" in data:
            raise ValueError("Неверный тикер")

        text = (
            f"📊 *{symbol}*\n"
            f"💰 Цена: `{data['lastPrice']}`\n"
            f"📉 Изменение за 24ч: `{data['priceChangePercent']}%`\n"
            f"📊 Объем торгов: `{data['volume']}`\n"
            f"🔺 Максимум: `{data['highPrice']}`\n"
            f"🔻 Минимум: `{data['lowPrice']}`"
        )

        await update.message.reply_markdown(text)

    except Exception as e:
        print(e)
        await update.message.reply_text("Ошибка. Проверь тикер и попробуй снова.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Привет! Я — крипто-бот.\n\n"
        "Вот что я умею:\n"
        "📊 /price BTCUSDT — текущая цена, изменение и объём\n"
        "📈 /chart BTCUSDT — график криптовалюты (скоро!)\n"
        "📉 /rsi BTCUSDT — индикатор RSI (скоро!)\n"
        "🔥 /liquidations BTC — ликвидации по монете (в разработке)\n\n"
        "💡 Просто введи нужную команду!"
    )
    await update.message.reply_text(text)
