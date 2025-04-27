async def progress_bar(current, total, message, stage):
    progress = int(current / total * 30)
    bar = "[" + "#" * progress + " " * (30 - progress) + "]"
    percent = (current / total) * 100
    await message.edit(f"{stage}\n{bar} {percent:.2f}%")