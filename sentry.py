import json
import os
import asyncio
from telegram import Bot

# 1. Sovereign Configuration
TOKEN = '8782969513:AAElFy0x7uF-NfwJzXTTxeB3mexqUGZIu2A'
CHAT_ID = '1150834771'

async def send_alert(message):
    bot = Bot(token=TOKEN)
    async with bot:
        # Using plain text to avoid parsing errors with underscores
        await bot.send_message(chat_id=CHAT_ID, text=message)

def monitor_ledger():
    ledger_path = 'market_ledger.json'
    if os.path.exists(ledger_path):
        with open(ledger_path, 'r') as f:
            data = json.load(f)
        
        balance = data.get('balance_usd', '991.32')
        state = data.get('current_state', 'LIQUIDITY_VACUUM')
        
        # 2. Simplified Alert Formatting (No Markdown to avoid crashes)
        alert_msg = (
            f"Nairobi-01 Node: Active Sentry\n"
            f"--------------------------------\n"
            f"Balance: ${balance}\n"
            f"State: {state}\n"
            f"Logic: Strategic Protection Active\n"
            f"--------------------------------\n"
            f"Verified by The Peculiar Librarian"
        )
        
        asyncio.run(send_alert(alert_msg))
        print("Sentry: Plain-text alert pushed to Telegram.")
    else:
        print("Sentry: market_ledger.json not found.")

if __name__ == "__main__":
    monitor_ledger()
