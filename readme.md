# YouTube Video Downloader with Fallbacks

This Python script downloads a YouTube video by trying multiple libraries in succession. It first attempts to download the video using **pytube**. If that fails, it falls back to **youtube-dl**, and finally to **yt-dlp** if the previous methods are unsuccessful.

## Features

- **Multiple Download Options:** Automatically attempts to download using pytube, youtube-dl, and yt-dlp in that order.
- **Easy Fallback:** If one method fails, the script gracefully moves to the next available method.
- **Simple to Use:** Provide a YouTube video URL via command-line argument or input prompt.

## Prerequisites

- **Python 3.x** is required.
- The following Python packages must be installed:
  - [pytube](https://github.com/pytube/pytube)
  - [youtube-dl](https://github.com/ytdl-org/youtube-dl)
  - [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Installation

1. **Clone or Download the Repository**

   Clone this repository or download the script file directly to your local machine.

2. **Install the Required Dependencies**

   You can install the necessary packages using pip. Open your terminal or command prompt and run:

   ```bash
   pip install pytube youtube-dl yt-dlp
