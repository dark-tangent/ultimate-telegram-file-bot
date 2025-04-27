import subprocess

def compress_video(input_file, output_file):
    command = [
        "ffmpeg", "-i", input_file,
        "-vcodec", "libx264", "-crf", "28",
        "-preset", "fast", output_file
    ]
    subprocess.run(command)

def extract_thumbnail(input_file, output_image):
    command = ["ffmpeg", "-ss", "00:00:02", "-i", input_file, "-vframes", "1", output_image]
    subprocess.run(command)