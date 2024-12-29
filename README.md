# Telegram Price Bot

Telegram Price Bot is a Python application that fetches real-time prices of Euro and 18K gold from the TGJU website and sends periodic updates to specified Telegram users or groups.

## Features

- **Real-time data:** Fetches the latest prices of Euro and 18K gold.
- **Scheduled updates:** Automatically sends updates at regular intervals (default: every 30 minutes).
- **Multiple recipients:** Sends updates to multiple Telegram users or groups.

## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.8 or higher** installed on your system.
2. **Telegram Bot Token:** You need a bot token from [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
3. **Chat IDs:** Telegram user or group chat IDs where updates should be sent.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/telegram-price-bot.git
   cd telegram-price-bot
Create a virtual environment and activate it (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Configuration
Open the main.py file.
Replace the placeholder TELEGRAM_BOT_TOKEN with your bot token:
python
Copy code
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
Add the chat IDs to the CHAT_IDS list:
python
Copy code
CHAT_IDS = ["123456789", "987654321"]
Usage
Run the bot:

bash
Copy code
python main.py
The bot will start fetching prices and sending periodic updates to the specified chat IDs.

File Structure
bash
Copy code
telegram-price-bot/
├── main.py                # Main script
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
Dependencies
The project uses the following Python libraries:

requests - To fetch data from the TGJU website.
beautifulsoup4 - For HTML parsing.
python-telegram-bot - To interact with the Telegram API.
apscheduler - For scheduling periodic updates.
Future Improvements
Add more currencies and commodities.
Enhance error handling and logging.
Create a web-based dashboard for monitoring.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

Author
Your Name - Your GitHub Profile
Enjoy using Telegram Price Bot! If you find it useful, don't forget to give a ⭐ on GitHub!

markdown
Copy code

### Instructions:
1. Replace placeholders like `your-telegram-bot-token`, `yourusername`, and `Your Name` with the relevant details.
2. Add a `requirements.txt` file with the project dependencies (if not already present):
requests beautifulsoup4 python-telegram-bot apscheduler

less
Copy code
3. Optional: Include a `LICENSE` file if you decide to apply a specific license (e.g., MIT License).
