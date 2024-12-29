from fastapi import FastAPI
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram.ext import Application
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Telegram bot token and chat IDs
TELEGRAM_BOT_TOKEN = "7304148206:AAGFKiddvSoaKe0zxToMqcJccPmLhPgcH6c"
CHAT_IDS = ["7197413077", "260674127"]  # Add more IDs here

# URLs for fetching prices
URL_EURO = "https://www.tgju.org/profile/price_eur"
URL_GOLD = "https://www.tgju.org/profile/geram18"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Function to fetch Euro price
def get_euro_price():
    try:
        response = requests.get(URL_EURO, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            span_tag = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
            return span_tag.get_text(strip=True) if span_tag else "Euro price not found."
        else:
            return "Error fetching Euro price."
    except Exception as e:
        return f"Error in Euro price fetch: {e}"

# Function to fetch Gold price
def get_gold_price():
    try:
        response = requests.get(URL_GOLD, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            span_tag = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
            return span_tag.get_text(strip=True) if span_tag else "Gold price not found."
        else:
            return "Error fetching Gold price."
    except Exception as e:
        return f"Error in Gold price fetch: {e}"

# Function to send messages
async def send_message(application: Application):
    euro_price = get_euro_price()
    gold_price = get_gold_price()
    message = f"💶 Euro Price: {euro_price} Toman\n💰 Gold (18K): {gold_price} Toman"
    for chat_id in CHAT_IDS:
        await application.bot.send_message(chat_id=chat_id, text=message)

# Main function
async def main():
    print("Bot is running...")
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Scheduler for periodic updates
    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(send_message, 'interval', args=[application], minutes=30)

    # Start bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    try:
        await asyncio.Event().wait()
    finally:
        await application.stop()
        await application.shutdown()

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
