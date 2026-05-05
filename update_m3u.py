import requests
import time

sources = [
    "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.m3u",
    "https://raw.githubusercontent.com/IPTVFlixBD/Fancode-BD/refs/heads/main/playlist.m3u",
    "https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u",
    "https://raw.githubusercontent.com/srhady/crichd-speical-live-event/refs/heads/main/playlist.m3u"
]

output_file = "Test.m3u"

def fetch_playlist(url):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.text
    except:
        return ""
    return ""

def merge_playlists():
    final_content = "#EXTM3U\n"
    
    for src in sources:
        content = fetch_playlist(src)
        lines = content.splitlines()
        
        for line in lines:
            if line.strip() != "#EXTM3U":
                final_content += line + "\n"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("Updated playlist!")

# loop every 15 minutes
while True:
    merge_playlists()
    time.sleep(900)
