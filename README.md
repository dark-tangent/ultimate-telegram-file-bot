# Ultimate Telegram File Bot 🚀

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?templateLink=https://github.com/YOURUSERNAME/ultimate-telegram-file-bot&envs=BOT_TOKEN,API_ID,API_HASH,MONGO_URI,OWNER_ID&projectName=Ultimate-Telegram-File-Bot&serviceName=uploader-bot)

A universal bot to upload, rename, compress and manage file uploads to Telegram.

## Features
- Stream uploads (no full download needed)
- Rename files easily
- Compress videos with ffmpeg
- User quotas (Free vs Premium)
- Admin panel to promote users
- MongoDB user management

## Deployment
1. Fill `.env`
2. Build Docker: `docker build -t uploader-bot .`
3. Run: `docker run uploader-bot`
4. Or deploy easily on [Railway](https://railway.app)

## Variables
| Name | Purpose |
|:----|:----|
| BOT_TOKEN | Your bot token |
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| MONGO_URI | MongoDB URI |
| OWNER_ID | Your Telegram ID |

## Credits
Made with 💖 by YOU!