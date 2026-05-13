import requests
import json

OUTPUT_FILE = "Test.m3u"

# তোমার Main m3u
MAIN_M3U = "https://raw.githubusercontent.com/stablesports711-hue/stable-sports-iptv/refs/heads/main/Test.m3u"

# JSON source
JSON_SOURCE = "https://raw.githubusercontent.com/srhady/vipsports/refs/heads/main/alpha_live.json"


def fetch_text(url):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.text


def convert_json_to_m3u(data):
    m3u = ""

    for item in data:
        name = item.get("name", "Unknown")
        logo = item.get("logo", "")
        group = item.get("group", "VIP SPORTS")
        url = item.get("url", "")

        if url:
            m3u += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
            m3u += f"{url}\n"

    return m3u


output = "#EXTM3U\n\n"

# ১. তোমার existing Test.m3u
try:
    main = fetch_text(MAIN_M3U)
    for line in main.splitlines():
        if line.strip() != "#EXTM3U":
            output += line + "\n"
    print("✅ Main M3U Loaded")
except Exception as e:
    print("Main M3U Error:", e)

# ২. JSON convert করে add
try:
    json_text = fetch_text(JSON_SOURCE)
    data = json.loads(json_text)

    output += "\n# ===== AUTO JSON CHANNELS =====\n"
    output += convert_json_to_m3u(data)

    print("✅ JSON Added")
except Exception as e:
    print("JSON Error:", e)

# Save
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Test.m3u Updated Successfully")
