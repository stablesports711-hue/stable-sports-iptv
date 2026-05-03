import requests

# সোর্স লিঙ্ক (যেখান থেকে ডাটা আসবে)
source_url = "https://raw.githubusercontent.com/munim-sah75/Cofs_TV/refs/heads/main/fancode.m3u"

# আপনার ফাইল (যেখানে ডাটা জমা হবে)
output_file = "STABLE-SPORTS TV.m3u"

def update_m3u():
    try:
        response = requests.get(source_url)
        if response.status_code == 200:
            content = response.text
            # ফাইলটি নতুন করে লিখবে (পুরানো ডাটা রিপ্লেস হবে)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully updated the playlist.")
        else:
            print(f"Failed to fetch. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    update_m3u()

