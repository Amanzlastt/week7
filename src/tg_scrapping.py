import os
import sys

from telethon import TelegramClient
import csv
from dotenv import load_dotenv
load_dotenv()

# Access the variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

# Create a Telethon client
client = TelegramClient("scraping_for_health_eahci", api_id, api_hash)

# Channel username (or ID)
channel_username = "https://t.me/EAHCI"

async def scrape_messages():
    await client.start()
    messages = await client.get_messages(channel_username, limit=500)

    # Save messages to a CSV file
    with open("eahci_messages.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Message ID", "Sender", "Text", "Date"])

        for message in messages:
            writer.writerow([message.id, message.sender_id, message.text, message.date])

    print("Scraping complete. Data saved in telegram_messages.csv")

with client:
    client.loop.run_until_complete(scrape_messages())
