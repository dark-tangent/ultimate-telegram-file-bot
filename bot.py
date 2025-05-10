from pyrogram import Client, filters
import os
from handlers.upload_handler import upload_file
from handlers.rename_handler import rename_file
from handlers.admin_handler import promote_premium, stats
from utils.database import init_db

app = Client(
    "UploaderBot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

init_db()

@app.on_message(filters.document | filters.video)
async def handle_upload(client, message):
    await upload_file(client, message)

@app.on_message(filters.command("rename"))
async def handle_rename(client, message):
    await rename_file(client, message)

@app.on_message(filters.command("addpremium") & filters.user(int(os.getenv("OWNER_ID"))))
async def handle_premium(client, message):
    await promote_premium(client, message)

@app.on_message(filters.command("stats") & filters.user(int(os.getenv("OWNER_ID"))))
async def handle_stats(client, message):
    await stats(client, message)

print("Bot is running...")

if __name__ == "__main__":
    app.run()
