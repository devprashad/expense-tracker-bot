import logging
import gspread
from google.oauth2.service_account import Credentials
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Setup Google Sheets
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS = Credentials.from_service_account_file('spendexpensetracker-1152d44c4271.json', scopes=SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open('ExpenseTracker').sheet1

# Setup Telegram
TELEGRAM_TOKEN = '7721911699:AAE-jJNg20G6i27RWh2bk1M0R2kY9Au7-6M'
logging.basicConfig(level=logging.INFO)

# Function to add expense
def add_expense(update: Update, context: CallbackContext):
    try:
        text = update.message.text
        amount, category = text.split(' ', 1)
        sheet.append_row([amount, category])
        update.message.reply_text(f"Added: ₹{amount} for {category}")
    except Exception as e:
        update.message.reply_text("Error: Send like 'amount category' (e.g., '200 groceries')")

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to SpendBot! Send expenses like '200 groceries'.")

# Main function
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, add_expense))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
