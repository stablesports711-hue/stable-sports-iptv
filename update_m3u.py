import requests

urls = [
    "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.m3u",
    "https://raw.githubusercontent.com/IPTVFlixBD/Fancode-BD/refs/heads/main/playlist.m3u",
    "https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u",
    "https://raw.githubusercontent.com/srhady/crichd-speical-live-event/refs/heads/main/playlist.m3u"
]

def create_playlist():
    master_content = "#EXTM3U\n"
    for url in urls:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                lines = r.text.splitlines()
                # প্রথম লাইন যদি #EXTM3U হয় তা বাদ দিয়ে বাকিটুকু নেওয়া
                filtered_lines = [line for line in lines if not line.strip().startswith("#EXTM3U")]
                master_content += "\n".join(filtered_lines) + "\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    with open("Test.m3u", "w", encoding="utf-8") as f:
        f.write(master_content)

if __name__ == "__main__":
    create_playlist()
