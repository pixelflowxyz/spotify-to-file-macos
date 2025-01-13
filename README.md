
# spotify-to-file-macos

I wanted a way to get my currently playing song into a text file. [Snip](https://github.com/dlrudie/Snip), a program often used by streamers to save their currently playing song to a text file so it can be read by OBS, is Windows-only - so I made a macOS alternative. It's not the most streamlined solution, but in general should be pretty easy to use - and easily understandable for custom modifications.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) ![Twitter](https://img.shields.io/twitter/follow/danpxlflw) ![Twitch Status](https://img.shields.io/twitch/status/danpxlflw)




## How it works

The file `app.sh` first runs `script.scpt`, which is an AppleScript script that talks locally to Spotify to get a bunch of information about the currently playing song. This is outputted in JSON format into `data.json`, and then `app.sh` runs `parse.py` which turns that data into OBS-ready files `artist.txt` and `title.txt`. `app.sh` is set by default to repeat every 15 seconds. The Python file should be easily understandable so you can mess with it and extend this. It's not great code, but it does the job - and that's all I really need!
