def get_audio_files():
    audio_files = []
    for file in os.listdir():
        if file.endswith(".mp3"):
            audio_files.append(file)
    return audio_files
