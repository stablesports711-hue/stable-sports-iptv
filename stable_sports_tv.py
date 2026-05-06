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

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1735648543857_Poster.jpg&w=1080&q=75",BTV News
https://www.btvlive.gov.bd/live/37f2df30-3edf-42f3-a2ee-6185002c841c/BD/d96eb7f4-83c2-4472-9597-3568390a8ebf/index.m3u8

#EXTINF:-1 tvg-logo="https://www.btvlive.gov.bd/_next/static/media/btv-logo.d937bde9.svg" group-title="BANGLA",BTV CTG
https://www.btvlive.gov.bd/live/37f2df30-3edf-42f3-a2ee-6185002c841c/BD/a707f2dc-9704-413a-a67c-17c64a77c350/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Xi_Ga5oBNnOkwJLWkhKP/posters/ef2899d5-1ae0-4fee-aee5-45f9b0b3ba80.png",Somoy TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1702/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770186895850.png",News 24 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1708/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770189826301.png",Star News
https://owrcovcrpy.gpcdn.net/bpk-tv/1710/output/index.m3u8

#EXTINF:-1 group-title="Entertainment" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770187361105.png",SATV HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1720/output/index.m3u8

#EXTINF:-1 group-title="Entertainment" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770188008067.png",Channel 9 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1729/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://i.postimg.cc/1t1P0VMt/images-(1).jpg",DBC News
https://owrcovcrpy.gpcdn.net/bpk-tv/1728/output/1728.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PS_La5oBNnOkwJLWLRN_/posters/e8c444fd-ee3b-4bf3-bb0a-f969bc295f82.png",Ekattor TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1705/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://yt3.googleusercontent.com/8Q8MCd6ypr2Hzbp60VE_stJPl063kQYfeTxdIQkAXRfhdzxByLl0sJYHsk43uTM4W_cOzwcbPQ=s160-c-k-c0x00ffffff-no-rj",Channel 24
https://owrcovcrpy.gpcdn.net/bpk-tv/1703/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/ES_cZZsBNnOkwJLW1Oz1/posters/b872b8f5-cb6b-45a1-a1cd-7609df51d614.png",Independent TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1704/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PiL635oBEef-9-uV2uCe/posters/36f380e0-6c71-4b27-a73b-2afb3ce7e982.png",Jamuna TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1701/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://dl.dropbox.com/s/4ldi1dp09s8o6bm/atn_news_bd.png",ATN News
https://owrcovcrpy.gpcdn.net/bpk-tv/1706/output/index.m3u8

#EXTINF:-1 tvg-logo="https://s6.gifyu.com/images/image27cfa7002786c232.png" group-title="BANGLA",ATN Bangla
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnbd-8-org.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 tvg-logo="https://tvassets.roarzone.info/images/2.png",ATN Bangla
#EXTVLCOPT:http-user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
https://bozztv.com/rongo/rongo-ATNBangla/index.m3u8

#EXTINF:-1 tvg-logo="https://www.jagobd.com/wp-content/uploads/2018/04/Anandatvupdate-150x150.jpg" group-title="BANGLA",Ananda TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 tvg-logo="https://i.imgur.com/jkbo7Qe.png",Ananda TV
#EXTVLCOPT:http-user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
https://bozztv.com/rongo/rongo-AnandaTV/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.ntvbd.com/sites/default/files/aggregator/2020/02/17/ntv-channel_0.jpg",NTV
https://owrcovcrpy.gpcdn.net/bpk-tv/1716/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s4.gifyu.com/images/image5c0bfa6b281be803.png",BanglaVision
https://owrcovcrpy.gpcdn.net/bpk-tv/1715/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/MyK__poBEef-9-uVmf5l/posters/1eadef5b-28e7-4dc2-b42f-c67a3357c9a0.png",Asian TV
http://103.229.254.25:7001/play/a063/index.m3u8

#EXTINF:-1 tvg-id="mytv" tvg-name="MY TV" tvg-logo="https://i.postimg.cc/HxGF4V2b/20250529_103226.png" group-title="Bangladesh",MY TV
#https://tvsen6.aynaott.com/mytv/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mytv-up-off.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s4.gifyu.com/images/image534fa27d7683f33d.png",Ekushey TV
http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/o3v235oBcqxnFHJBkAdC/posters/159af631-796d-4342-a2a7-c272f32bcd32.png",[BD] Ekhon TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/globaltv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/0y_tDJsBNnOkwJLWNrdE/posters/2ff058e1-630f-4657-8dc6-b677e65642c5.png",Global TV
http://sm-monirul.top/AyNa/play.php?id=0ac6af3d-acce-4d9d-9ce5-32d4b53f9326&e=.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/qnv835oBcqxnFHJBuQcB/posters/348dfac3-c1e0-485d-a72b-3d282c9e2c73.png",Channel I
https://owrcovcrpy.gpcdn.net/bpk-tv/1723/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Deepto%20TV.jpeg",Deepto TV
https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8

#EXTINF:-1 tvg-logo="https://s3.aynaott.com/storage/58658d4594ca1ff3c5031c9d8e3d9fc0" group-title="Bangla",Boishakhi TV
https://boishakhi.sonarbanglatv.com/boishakhi/boishakhitv/index.m3u8

#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Bijoy%20TV.png" group-title="Bangla",Bijoy TV
https://bozztv.com/rongo/rongo-BijoyTV/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-logo="https://www.jagobd.com/wp-content/uploads/2024/08/pran-RFL.png" group-title="Bangladesh",Jago News 24
https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s3.aynaott.com/storage/1b5cb8c7901739cd7d201a38d2ab4737",MAASRANGA HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1722/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.deshitv.com/images//bangla_logo/DeshTV24-BanglaLogo.png",Deshi TV
#https://deshitv.deshitv24.net/live/myStream/playlist.m3u8
http://208.86.19.13:81/514.stream/index.m3u8

#EXTINF:-1 tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/WyPuDJsBEef-9-uVUA_z/posters/ea20055c-a824-443c-8083-ce8e2da8b922.png" group-title="Bangladesh",CHANNEL S
#https://app.ncare.live/live-orgin/channels.stream/playlist.m3u8
http://103.229.254.25:7001/play/a060/index.m3u8
"""

output += custom

# Save file
with open("STABLE-SPORTS TV.m3u", "w", encoding="utf-8") as f:
    f.write(output)

print("Sports playlist updated!")
