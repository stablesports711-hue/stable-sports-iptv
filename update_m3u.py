import requests
import os

# সোর্স লিঙ্ক
source_url = "https://raw.githubusercontent.com/munim-sah75/Cofs_TV/refs/heads/main/fancode.m3u"
output_file = "STABLE-SPORTS TV.m3u"

# আপনার নিজের চ্যানেলগুলো (নিচে থাকবে)
my_own_channels = """
#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/13XVVyg3/1773936967533.png",STABLE-SPORTS TV
http://198.195.239.50:8095/StarSports2/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.ibb.co.com/V04pB3mj/1776384168515.png",Bangladesh VS New Zealand 
http://172.20.21.22/live/skyfeed1005/index.m3u8

# (আপনার বাকি সব চ্যানেল এখানে বসান...)

#EXTINF:-1 tvg-id="JalsaMoviesHD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Jalsa_Movies_HD.png" group-title="Movies", Jalsa Movies HD
http://Rochdi@starshare.net:80/live/Suryaaa/SURYAAAA/425.ts
"""

def update_m3u():
    try:
        print("Fetching data from source...")
        response = requests.get(source_url)
        if response.status_code == 200:
            source_content = response.text.strip()
            
            # অটো-আপডেট আগে এবং আপনার লিস্ট পরে সাজানো হচ্ছে
            full_content = source_content + "\n\n" + my_own_channels.strip()
            
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(full_content)
            print("Successfully Updated!")
        else:
            print(f"Error fetching source: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_m3u()
