import requests


# =========================================================
# OUTPUT FILE
# =========================================================

OUTPUT_FILES = [
    "STABLE-SPORTS TV.m3u"
]


# =========================================================
# SOURCES
# =========================================================

# First two sources
SOURCES_BEFORE_CUSTOM = [
    "",

    "",
]


# Sources after custom channels
SOURCES_AFTER_CUSTOM = [
    "https://raw.githubusercontent.com/sm-monirulislam/Toffee-Auto-Update/refs/heads/main/toffee_playlist.m3u",
]


# =========================================================
# CUSTOM CHANNELS
# =========================================================

custom_channels = r"""#EXTM3U

# =========================================================
# ADD YOUR FULL CUSTOM CHANNELS HERE
# =========================================================

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/e/e6/2026_FIFA_ASEAN_Cup.webp?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original" group-title="LIVE SPORTS",FIFA ASEAN CUP 2026
https://r8vx3qkm2ztp7ynj6lpl.rockstreamer.com/v1/019ee554d6cc1567ee93172b12d63f/01a047abffef1ea557842156e6858c/main.m3u8|Referer=https://iscreen.com.bd/

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/e/e6/2026_FIFA_ASEAN_Cup.webp?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original" group-title="LIVE SPORTS",FIFA ASEAN CUP 2026
https://d8j84o343a5m2.cloudfront.net/live/testtapmad3/master.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/e/e6/2026_FIFA_ASEAN_Cup.webp?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original" group-title="LIVE SPORTS",FIFA ASEAN CUP 2026
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports.m3u8

# ---------------------------------------------------------
# ADD THE REST OF YOUR CUSTOM CHANNELS HERE
# ---------------------------------------------------------

"""


# =========================================================
# FUNCTION: LOAD ONE SOURCE
# =========================================================

def load_source(source_url):
    """
    Download an M3U source and return channel data
    without the #EXTM3U header.
    """

    try:
        response = requests.get(
            source_url,
            timeout=20
        )

        if response.status_code == 200:

            lines = response.text.splitlines()

            result = []

            for line in lines:

                # Remove main M3U header
                if line.strip() == "#EXTM3U":
                    continue

                # Remove empty lines
                if not line.strip():
                    continue

                result.append(line)

            print(f"Loaded: {source_url}")

            return "\n".join(result) + "\n"

        else:

            print(
                f"Failed: {source_url} "
                f"(HTTP {response.status_code})"
            )

            return ""

    except Exception as e:

        print(
            f"Error loading source: "
            f"{source_url}"
        )

        print(e)

        return ""


# =========================================================
# BUILD PLAYLIST
# =========================================================

output = "#EXTM3U\n"


# =========================================================
# PART 1
# FIRST TWO SOURCES
# =========================================================

print("")
print("========================================")
print("PART 1 - FIRST TWO SOURCES")
print("========================================")

for source in SOURCES_BEFORE_CUSTOM:

    output += load_source(source)


# =========================================================
# PART 2
# CUSTOM CHANNELS
# =========================================================

print("")
print("========================================")
print("PART 2 - CUSTOM CHANNELS")
print("========================================")

output += custom_channels.strip() + "\n"

print("Custom Channels Added")


# =========================================================
# PART 3
# SOURCES AFTER CUSTOM
# =========================================================

print("")
print("========================================")
print("PART 3 - SOURCES AFTER CUSTOM")
print("========================================")

for source in SOURCES_AFTER_CUSTOM:

    output += load_source(source)


# =========================================================
# SAVE PLAYLIST
# =========================================================

print("")
print("========================================")
print("SAVING PLAYLIST")
print("========================================")

for filename in OUTPUT_FILES:

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(output)

        print(
            f"{filename} Updated Successfully"
        )

    except Exception as e:

        print(
            f"Failed to save {filename}"
        )

        print(e)


# =========================================================
# FINISHED
# =========================================================

print("")
print("========================================")
print("DONE")
print("========================================")

print("Final playlist order:")
print("1. Source 1")
print("2. Source 2")
print("3. Custom Channels")
print("4. Source 3")

print("")
print("Playlist generation completed.")
