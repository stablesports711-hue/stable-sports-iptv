import requests

source = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u"

output = "#EXTM3U\n"

# Fetch Toffee playlist
try:
    r = requests.get(source, timeout=10)
    if r.status_code == 200:
        for line in r.text.splitlines():
            if line.strip() != "#EXTM3U":
                output += line + "\n"
except:
    pass

# Custom channels
custom = """
#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/13XVVyg3/1773936967533.png",STABLE-SPORTS TV
http://198.195.239.50:8095/StarSports2/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.ibb.co.com/V04pB3mj/1776384168515.png",Bangladesh VS New Zealand
http://172.20.21.22/live/skyfeed1005/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1676193184888_2.png&w=1080&q=75",SANGSAD BANGLADESH
https://www.btvlive.gov.bd/live/37f2df30-3edf-42f3-a2ee-6185002c841c/BD/9ee3b4f9-fd0a-47c5-a135-2575c5691613/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://ssl.com.bd/sites/default/files/BTV%20Logo%20Gallery.png",BTV
https://owrcovcrpy.gpcdn.net/bpk-tv/1709/output/index.m3u8
"""

output += custom

# Save file
with open("STABLE-SPORTS TV.m3u", "w", encoding="utf-8") as f:
    f.write(output)

print("Sports playlist updated!")
