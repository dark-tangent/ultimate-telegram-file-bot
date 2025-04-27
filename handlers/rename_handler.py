async def rename_file(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: `/rename new_filename.ext`", quote=True)
        return

    reply = message.reply_to_message
    if not (reply and (reply.document or reply.video)):
        await message.reply("Reply to a file to rename!", quote=True)
        return

    new_name = message.command[1]
    downloading = await message.reply("📥 Downloading...")
    file_like = await reply.download(in_memory=True)

    await downloading.edit("📤 Uploading with new name...")
    await client.send_document(message.chat.id, file_like, file_name=new_name, caption="Here is your renamed file.")

    await downloading.delete()