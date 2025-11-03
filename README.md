# Discord Say Bot/JSON Message bot

A simple Python script that sends custom JSON-formatted messages to Discord channels using the Discord API.

## ⚠️ Important Setup Instructions

### Step 1: Prepare Your Message
**Please put your specified JSON message in `message.json`!**

Example `message.json`:
```json
{
    "content": "Hello World!",
    "embeds": [
        {
            "title": "Embed Title",
            "description": "This is an embed",
            "color": 5814783
        }
    ]
}
```

### Step 2: Configure Credentials
**Change line 5 with your channel ID and line 6 with your bot token!**

```python
CHANNEL_ID = "YOUR_CHANNEL_ID_HERE"   # ← Replace this
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"     # ← Replace this
```

## 🔧 How to Get Credentials

### Getting Channel ID
(You can get the tutorial from here)[https://reallytyler.github.io/howtoget/channel-id/index.html]

### Getting Bot Token
1. **Go to [Discord Developer Portal](https://discord.com/developers/applications)**
2. **Create/Select Your Application:**
   - Click "New Application" or select existing one
3. **Navigate to Bot Section:**
   - Click on "Bot" in the left sidebar
4. **Create/Copy Bot Token:**
   - Click "Reset Token" or "Copy" to get your bot token
   - ⚠️ **Never share your bot token!**

### Bot Permissions
Make sure your bot has:
- **View Channel** permission
- **Send Messages** permission
- **Embed Links** permission (if using embeds)

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

### Install Requirements
```bash
pip install requests
```

## 🚀 Usage

1. Complete the setup steps above
2. Run the script:
```bash
python sendjson.py
```

3. Check output:
   - ✅ **Message sent successfully!** - Success
   - ❌ **Failed to send message** - Check your credentials and permissions

## 📁 File Structure
```
discord-bot/
├── sendjson.py     # Main script
├── message.json    # Your message content 
└── README.md       # This file
```

## 🛠️ Troubleshooting

**Common Issues:**
- **Invalid token**: Check your bot token is correct
- **Missing permissions**: Ensure bot has required channel permissions
- **Channel not found**: Verify channel ID is correct
- **JSON syntax error**: Validate your `message.json` format

## ⚠️ Security Note

Never commit your actual bot token or channel ID to version control. Use environment variables or config files that are added to `.gitignore` for production use.
```

**Code Files:**

**sendjson.py**
```python
import requests
import json

# === CONFIGURATION ===
CHANNEL_ID = "CHANNEL_ID_HERE"   # replace with your target channel ID
BOT_TOKEN = "BOT_TOKEN_HERE" # replace with your bot token
JSON_FILE = "message.json"       # the file containing your message data
# ======================

# Don't forget to put your specified json message in message.json !

# Dont touch this part ↓
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


**requirements.txt**
```txt
requests>=2.25.1
```
