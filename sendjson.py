import requests
import json

# === CONFIGURATION ===
CHANNEL_ID = "1359842427426439328"   # replace with your target channel ID
BOT_TOKEN = "ABCDEFGHIJKLMNOQRSTUVWXYZ" # replace with your bot token
JSON_FILE = "message.json"       # don't change 
# ======================

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
} 

# Load your JSON message
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Send the message
response = requests.post(url, headers=headers, json=data)

# Check result
if response.status_code == 200 or response.status_code == 201:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed to send message ({response.status_code})")
    print(response.text)
