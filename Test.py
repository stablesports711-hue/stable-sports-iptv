import requests

OUTPUT_FILE = "Test.m3u"

JSON_URL = "https://raw.githubusercontent.com/srhady/vipsports/refs/heads/main/alpha_live.json"

M3U_SOURCES = [
    "https://raw.githubusercontent.com/abusaeeidx/CricHd-playlists-Auto-Update-permanent/refs/heads/main/ALL.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u"
]

# =========================
# YOUR CUSTOM CHANNELS
# =========================
custom_channels = """
#EXTM3U

#EXTINF:-1 group-title="PROMO",STABLE-SPORTS TV
http://198.195.239.50:8095/StarSports2/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="SPORTS",T Sports
http://198.195.239.50:8095/Tsports/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="BANGLA",BTV
https://owrcovcrpy.gpcdn.net/bpk-tv/1709/output/index.m3u8
"""

# =========================
# FETCH JSON
# =========================
def fetch_json_channels():
    try:
        r = requests.get(JSON_URL, timeout=20)
        data = r.json()

        output = ""

        for ch in data:
            name = ch.get("name", "Unknown")
            logo = ch.get("logo", "")
            url = ch.get("url", "")

            output += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n'
            output += f'{url}\n'

        print("Loaded JSON")
        return output

    except Exception as e:
        print("JSON Error:", e)
        return ""

# =========================
# FETCH M3U
# =========================
def fetch_m3u(url):
    try:
        r = requests.get(url, timeout=20)

        if r.status_code == 200:
            lines = r.text.splitlines()

            return "\n".join(
                line for line in lines
                if line.strip() != "#EXTM3U"
            )

        return ""

    except Exception as e:
        print("M3U Error:", e)
        return ""

# =========================
# BUILD PLAYLIST
# =========================
output = "#EXTM3U\n\n"

# 1. Your channels
output += custom_channels + "\n"

# 2. JSON channels
output += fetch_json_channels() + "\n"

# 3. Auto-update M3U links
for source in M3U_SOURCES:
    output += fetch_m3u(source) + "\n"

# 4. Your channels again
output += custom_channels + "\n"

# =========================
# SAVE
# =========================
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ STABLE-SPORTS TV.m3u Updated Successfully")
