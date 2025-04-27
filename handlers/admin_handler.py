from utils.database import promote_user_to_premium, get_total_stats

async def promote_premium(client, message):
    try:
        user_id = message.text.split()[1]
        promote_user_to_premium(user_id)
        await message.reply(f"✅ User `{user_id}` promoted to Premium!")
    except IndexError:
        await message.reply("Usage: `/addpremium user_id`")

async def stats(client, message):
    total_users, total_uploaded = get_total_stats()
    await message.reply(f"📊 Total Users: {total_users}\n📦 Total Uploaded: {total_uploaded / (1024 * 1024):.2f} MB")
