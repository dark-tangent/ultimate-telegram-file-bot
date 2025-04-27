import io
from utils.progress_bar import progress_bar
from utils.database import get_user, reset_daily_quota_if_needed
from pyrogram import enums

async def upload_file(client, message):
    user_id = message.from_user.id
    reset_daily_quota_if_needed(user_id)
    user = get_user(user_id)

    file_size = message.document.file_size if message.document else message.video.file_size
    if user["used_today"] + file_size > user["daily_limit"]:
        await message.reply("❌ You exceeded your daily upload limit.")
        return

    downloading = await message.reply("📥 Downloading...")
    file_like = io.BytesIO()
    await message.download(file_like, progress=progress_bar, progress_args=(downloading, "Downloading"))
    file_like.seek(0)

    uploading = await downloading.edit("📤 Uploading...")
    await client.send_document(message.chat.id, file_like, caption="Here you go!", progress=progress_bar, progress_args=(uploading, "Uploading"))

    from utils.database import update_user_usage
    update_user_usage(user_id, file_size)
    await uploading.edit("✅ Uploaded successfully!")