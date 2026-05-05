import requests
import os

sources = [
    "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.m3u",
    "https://raw.githubusercontent.com/IPTVFlixBD/Fancode-BD/refs/heads/main/playlist.m3u",
    "https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u",
    "https://raw.githubusercontent.com/srhady/crichd-speical-live-event/refs/heads/main/playlist.m3u"
]

output_file = "Test.m3u"

def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text if r.status_code == 200 else ""
    except:
        return ""

final = "#EXTM3U\n"

for url in sources:
    content = fetch(url)
    for line in content.splitlines():
        if line.strip() != "#EXTM3U":
            final += line + "\n"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(final)

# Git push
os.system("git config --global user.email 'you@example.com'")
os.system("git config --global user.name 'auto-bot'")
os.system("git add Test.m3u")
os.system("git commit -m 'auto update' || echo no changes")
os.system("git push")
