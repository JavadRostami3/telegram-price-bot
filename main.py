import asyncio
import requests
from bs4 import BeautifulSoup
from telegram.ext import Application
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Telegram bot token
TELEGRAM_BOT_TOKEN = "7304148206:AAGFKiddvSoaKe0zxToMqcJccPmLhPgcH6c"
CHAT_IDS = ["7197413077", "1234567890", "9876543210"]  # List of chat IDs

# URLs of web pages
URL_EURO = "https://www.tgju.org/profile/price_eur"
URL_GOLD = "https://www.tgju.org/profile/geram18"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Function to fetch the price of Euro
def get_euro_price():
    try:
        response = requests.get(URL_EURO, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            span_tag = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
            if span_tag:
                return span_tag.get_text(strip=True)
            else:
                return "Euro not found."
        else:
            return "Error fetching Euro."
    except Exception as e:
        return f"Error in Euro: {e}"

# Function to fetch the price of 18K Gold
def get_gold_price():
    try:
        response = requests.get(URL_GOLD, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            span_tag = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
            if span_tag:
                return span_tag.get_text(strip=True)
            else:
                return "Gold not found."
        else:
            return "Error fetching Gold."
    except Exception as e:
        return f"Error in Gold: {e}"

# Function to send messages
async def send_message(application: Application):
    euro_price = get_euro_price()
    gold_price = get_gold_price()
    message = f"💶 Euro Price: {euro_price} Toman\n💰 18K Gold Price: {gold_price} Toman"
    for chat_id in CHAT_IDS:  # Send messages to all chat IDs
        try:
            await application.bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Error sending message to {chat_id}: {e}")

# Main function to run the program
async def main():
    print("Bot is running...")
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Message scheduling
    scheduler = AsyncIOScheduler()
    scheduler.start()

    # Add scheduling to the event loop
    scheduler.add_job(send_message, 'interval', args=[application], minutes=30)

    # Run the bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    try:
        await asyncio.Event().wait()  # Keep the program running
    finally:
        await application.stop()
        await application.shutdown()

# Start the program
if __name__ == "__main__":
    asyncio.run(main())
