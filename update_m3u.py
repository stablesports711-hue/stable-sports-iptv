import requests

# আপনার দেওয়া সোর্স লিস্ট (সিরিয়াল অনুযায়ী)
urls = [
    "https://raw.githubusercontent.com/srhady/tapmad-bd/refs/heads/main/tapmad_bd.m3u",
    "https://raw.githubusercontent.com/srhady/Fancode-bd/refs/heads/main/main_playlist.m3u",
    "https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u",
    "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u",
    "https://raw.githubusercontent.com/srhady/crichd-speical-live-event/refs/heads/main/playlist.m3u"
]

def create_playlist():
    master_content = "#EXTM3U\n"
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                # প্রথম লাইন (#EXTM3U) বাদ দিয়ে বাকিটুকু নেওয়া
                content = "\n".join(lines[1:]) if lines[0].startswith("#EXTM3U") else "\n".join(lines)
                master_content += content + "\n"
        except Exception as e:
            print(f"Error loading {url}: {e}")

    with open("Test.m3u", "w", encoding="utf-8") as f:
        f.write(master_content)

if __name__ == "__main__":
    create_playlist()
