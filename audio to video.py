import yt_dlp

def speak(message):
    """Simulates speaking by printing a message."""
    print(f"Jarvis: {message}")

def download_youtube_audio(url, output_path='./'):
    """
    Download audio from a YouTube video and save as mp3 format.
    
    Parameters:
    - url (str): YouTube video URL.
    - output_path (str): Directory to save the downloaded audio.
    """
    # Set up the yt-dlp options for audio only
    options = {
        'format': 'bestaudio/best',  # Best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract and convert audio
            'preferredcodec': 'mp3',  # Convert audio to mp3 format
            'preferredquality': '192',  # Set quality of the mp3
        }],
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Save with video title as filename
        'noplaylist': True,  # Avoid downloading entire playlists
    }

    # Download the audio
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        speak("Audio download complete!")
    except Exception as e:
        speak(f"Error downloading audio: {e}")

def audio_to_video(audio_path, image_path, output_path='output_video.mp4'):
    """
    Convert an audio file to a video with an image as the background.
    
    Parameters:
    - audio_path (str): Path to the audio file (MP3, etc.)
    - image_path (str): Path to the image (JPG, PNG) used as video background.
    - output_path (str): Path to save the resulting video file.
    """
    try:
        import ffmpeg
        (
            ffmpeg
            .input(image_path, loop=1)
            .input(audio_path)
            .output(output_path, vcodec='libx264', acodec='aac', strict='experimental', shortest=1)
            .run()
        )
        speak(f"Video saved as {output_path}")
    except Exception as e:
        speak(f"Error creating video: {e}")

def main():
    """Main function to interact with user and perform conversions."""
    # Step 1: Download YouTube audio
    youtube_url = input("Enter the YouTube video URL to download audio: ")
    download_youtube_audio(youtube_url, './downloads/')
    
    # Step 2: Convert audio to video
    audio_file = input("Enter the path to the downloaded audio (e.g., ./downloads/audio.mp3): ")
    image_file = input("Enter the path to the image you want to use for the background: ")
    audio_to_video(audio_file, image_file, 'output_video.mp4')

if __name__ == '__main__':
    main()
