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
[You can get the tutorial from here](https://reallytyler.github.io/howtoget/channel-id)

### Getting Bot Token
**[You can get the tutorial from here](https://reallytyler.github.io/howtoget/bottoken)**

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


**requirements.txt**
```txt
requests>=2.25.1
```
