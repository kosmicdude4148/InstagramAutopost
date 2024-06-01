import os
import time
import random
from instabot import Bot

# Set the image URL
image_url = "https://images.app.goo.gl/btXUfsXeGMKPdBRFA"

# Set the Instagram account credentials
instagram_username = "thakurarushiiii"
instagram_password = "block420"

# Set the caption settings
captions = ["Random caption 1", "Random caption 2", "Random caption 3"]

# Create a new Instagram bot instance
bot = Bot()

# Login to the Instagram account
bot.login(username=instagram_username, password=instagram_password)

while True:
    # Post the image with a random caption
    bot.upload_photo(image_url, caption=random.choice(captions))
    print("Image posted successfully!")
    time.sleep(30)  # Wait for 30 seconds before posting again
