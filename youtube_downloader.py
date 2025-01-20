"""
Try downloading a YouTube video using pytube first.
If that fails, fall back to youtube-dl, then finally to yt-dlp.
"""

import sys

def download_with_pytube(url):
    from pytube import YouTube
    
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading '{yt.title}' using pytube...")
    stream.download()
    print("Download completed with pytube!")


def download_with_youtube_dl(url):
    import youtube_dl  # Ensure youtube_dl is installed: pip install youtube-dl
    
    ydl_opts = {
        # Add any youtube-dl options here if desired (e.g., "outtmpl", "format", etc.)
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Attempting download with youtube-dl...")
        ydl.download([url])
    print("Download completed with youtube-dl!")


def download_with_yt_dlp(url):
    import yt_dlp  # Ensure yt-dlp is installed: pip install yt-dlp
    
    ydl_opts = {
        # Add any yt-dlp options here if desired (e.g., "outtmpl", "format", etc.)
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Attempting download with yt-dlp...")
        ydl.download([url])
    print("Download completed with yt-dlp!")


def download_video(video_url):
    """
    Try pytube -> youtube-dl -> yt-dlp in that order.
    """
    try:
        download_with_pytube(video_url)
    except Exception as e_pytube:
        print(f"pytube failed: {e_pytube}\nFalling back to youtube-dl...")

        try:
            download_with_youtube_dl(video_url)
        except Exception as e_ytdl:
            print(f"youtube-dl failed: {e_ytdl}\nFalling back to yt-dlp...")

            try:
                download_with_yt_dlp(video_url)
            except Exception as e_ytdlp:
                print(f"yt-dlp failed: {e_ytdlp}\nNo more fallback methods available.")


if __name__ == "__main__":
    # Get URL from user or command line
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube video URL: ")

    download_video(url)
