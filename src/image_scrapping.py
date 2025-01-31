import os
import sys
from telethon import TelegramClient
import csv
from dotenv import load_dotenv
from telethon.tl.types import MessageMediaPhoto

load_dotenv()

# Access the variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
client = TelegramClient("session_name", api_id, api_hash)

# Define channel username
channel_username = "lobelia4cosmetics"  # Change this to your target channel

# Directory to save images
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

import logging

# Set up logging
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def scrape_images():
    await client.start()
    
    messages = await client.get_messages(channel_username, limit=100)  # Adjust limit

    with open("image_metadata.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Message ID", "Image Path", "Date"])

        for message in messages:
            if message.media and isinstance(message.media, MessageMediaPhoto):
                # Download the image
                file_path = await client.download_media(message.media, file=output_dir)
                writer.writerow([message.id, file_path, message.date])
                # Optionally log the download
                logging.info(f"Downloaded: {file_path}")

with client:
    client.loop.run_until_complete(scrape_images())