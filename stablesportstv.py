import requests

OUTPUT_FILE = "STABLE-SPORTS TV.m3u"

sources = [
    "https://raw.githubusercontent.com/abusaeeidx/CricHd-playlists-Auto-Update-permanent/refs/heads/main/ALL.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u"
]

# =========================
# CUSTOM CHANNELS (TOP)
# =========================

custom_channels = """
#EXTM3U

#EXTINF:-1 group-title="PROMO",STABLE-SPORTS TV
http://198.195.239.50:8095/StarSports2/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="SPORTS",T Sports
http://198.195.239.50:8095/Tsports/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="SPORTS",Sony Sports 2
http://198.195.239.50:8095/SonyTenSports2/index.m3u8
"""

output = custom_channels + "\n"

# =========================
# FETCH PLAYLISTS
# =========================

for source in sources:
    try:
        r = requests.get(source, timeout=20)

        if r.status_code == 200:
            lines = r.text.splitlines()

            for line in lines:
                if line.strip() != "#EXTM3U":
                    output += line + "\n"

            print(f"Loaded: {source}")

        else:
            print(f"Failed: {source}")

    except Exception as e:
        print("Error:", e)

# =========================
# SAVE FILE
# =========================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ STABLE-SPORTS TV.m3u Updated Successfully")
