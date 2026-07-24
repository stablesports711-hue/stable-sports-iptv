import requests

OUTPUT_FILES = [
    "STABLE-SPORTS TV.m3u",
    " Nahid.m3u",
    "Siam.m3u"
]

sources = [
    "https://raw.githubusercontent.com/stablesports711-hue/stable-sports-toffee/refs/heads/main/toffee.m3u",
    "https:.//cdn-data-margify-tv-for-user.pages.dev/playlist.m3u",
    "https:.//raw.githubusercontent.com/abusaeeidx/BDxTV/refs/heads/main/roar-zone-playlist.m3u"
]

# =========================
# CUSTOM CHANNELS (TOP)
# =========================

custom_channels = """#EXTM3U
#EXTINF:-1 tvg-logo="https://i.postimg.cc/q7Jfk310/20260723-214501.png" group-title="LIVE SPORTS",GLOBAL League 2026 (ENGLISH)
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-ASports.m3u8

https://i.postimg.cc/q7Jfk310/20260723-214501.png
#EXTINF:-1 tvg-id="tapmad-15407" tvg-logo="https://d34080pnh6e62j.cloudfront.net/images/channels/mobile_large/17847038331020x576.jpg" group-title="Volleyball", Uzbekistan vs Bangladesh | CAVA Men's Volleyball Championship 2026
https://serieAleague.akamaized.net/hls/live/2107107/tap-BK-PSL-D1-E/master.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/0NLNmXLJ/Lanka-Premier-League-T20-2026.png" group-title="LIVE SPORTS",Lanka Premier League 2026 (ENGLISH)
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow2.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/0NLNmXLJ/Lanka-Premier-League-T20-2026.png" group-title="LIVE SPORTS",Lanka Premier League 2026 (ENGLISH)
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports2.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/0NLNmXLJ/Lanka-Premier-League-T20-2026.png" group-title="LIVE SPORTS",Lanka Premier League 2026 (ENGLISH)
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-ASports.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/0NLNmXLJ/Lanka-Premier-League-T20-2026.png" group-title="LIVE SPORTS",Lanka Premier League 2026 (ENGLISH)
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=7e9239c1982d984a002df3ed049d0756:1b8a17598129a3618535c8fb05f103fe
https://otte.cache.aiv-cdn.net/iad-nitro/live/clients/dash/enc/fdb3pubmek/out/v1/aefca6420f944a9482e117f315de535f/cenc.mpd


#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/13XVVyg3/1773936967533.png",STABLE-SPORTS TV
http://sm-monirul.top/ott/iscreen/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1676193184888_2.png&w=1080&q=75",SANGSAD BANGLADESH
https://owrcovcrpy.gpcdn.net/bpk-tv/1709/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://ssl.com.bd/sites/default/files/BTV%20Logo%20Gallery.png",BTV
https://owrcovcrpy.gpcdn.net/bpk-tv/1725/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1735648543857_Poster.jpg&w=1080&q=75",BTV News
http://fastshare1.com:8080//live/25711345/late8airline/998.ts

#EXTINF:-1 tvg-logo="https://www.btvlive.gov.bd/_next/static/media/btv-logo.d937bde9.svg" group-title="BANGLA",BTV CTG
http://fastshare1.com:8080//live/25711345/late8airline/3818.ts

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Xi_Ga5oBNnOkwJLWkhKP/posters/ef2899d5-1ae0-4fee-aee5-45f9b0b3ba80.png",Somoy TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1713/output/index.m3u8
#https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/SomoyTv.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/ES_cZZsBNnOkwJLW1Oz1/posters/b872b8f5-cb6b-45a1-a1cd-7609df51d614.png",Independent TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1704/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PiL635oBEef-9-uV2uCe/posters/36f380e0-6c71-4b27-a73b-2afb3ce7e982.png",Jamuna TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1701/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770186895850.png",News 24 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1708/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770189826301.png",Star News
https://owrcovcrpy.gpcdn.net/bpk-tv/1710/output/index.m3u8

#EXTINF:-1 tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1781163068414.png" group-title="BANGLA",Channel 1
https://owrcovcrpy.gpcdn.net/bpk-tv/1702/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://i.postimg.cc/1t1P0VMt/images-(1).jpg",DBC News
https://owrcovcrpy.gpcdn.net/bpk-tv/1728/output/1728.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PS_La5oBNnOkwJLWLRN_/posters/e8c444fd-ee3b-4bf3-bb0a-f969bc295f82.png",Ekattor TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1705/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://yt3.googleusercontent.com/8Q8MCd6ypr2Hzbp60VE_stJPl063kQYfeTxdIQkAXRfhdzxByLl0sJYHsk43uTM4W_cOzwcbPQ=s160-c-k-c0x00ffffff-no-rj",Channel 24
https://owrcovcrpy.gpcdn.net/bpk-tv/1703/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770187361105.png",SATV HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1720/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770188008067.png",Channel 9 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1729/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://dl.dropbox.com/s/4ldi1dp09s8o6bm/atn_news_bd.png",ATN News
https://owrcovcrpy.gpcdn.net/bpk-tv/1706/output/index.m3u8

#EXTINF:-1 tvg-logo="https://s6.gifyu.com/images/image27cfa7002786c232.png" group-title="BANGLA",ATN Bangla
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnbd-8-org.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 tvg-logo="https://i.imgur.com/jkbo7Qe.png" group-title="BANGLA",Ananda TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/


#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.ntvbd.com/sites/default/files/aggregator/2020/02/17/ntv-channel_0.jpg",NTV
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/NTV.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1716/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s4.gifyu.com/images/image5c0bfa6b281be803.png",BanglaVision
https://owrcovcrpy.gpcdn.net/bpk-tv/1715/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/MyK__poBEef-9-uVmf5l/posters/1eadef5b-28e7-4dc2-b42f-c67a3357c9a0.png",Asian TV
https://mtlivestream.com/hls/asian/ytlive/index.m3u8

#EXTINF:-1 tvg-id="mytv" tvg-name="MY TV" tvg-logo="https://i.postimg.cc/HxGF4V2b/20250529_103226.png" group-title="BANGLA",MY TV
#https://tvsen6.aynaott.com/mytv/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mytv-up-off.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s4.gifyu.com/images/image534fa27d7683f33d.png",Ekushey TV
http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/o3v235oBcqxnFHJBkAdC/posters/159af631-796d-4342-a2a7-c272f32bcd32.png",Ekhon TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/globaltv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/0y_tDJsBNnOkwJLWNrdE/posters/2ff058e1-630f-4657-8dc6-b677e65642c5.png",Global TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/qnv835oBcqxnFHJBuQcB/posters/348dfac3-c1e0-485d-a72b-3d282c9e2c73.png",Channel I
https://owrcovcrpy.gpcdn.net/bpk-tv/1723/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Deepto%20TV.jpeg",Deepto TV
https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8

#EXTINF:-1 tvg-logo="https://s3.aynaott.com/storage/58658d4594ca1ff3c5031c9d8e3d9fc0" group-title="BANGLA",Boishakhi TV
https://boishakhi.sonarbanglatv.com/boishakhi/boishakhitv/index.m3u8

#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Bijoy%20TV.png" group-title="BANGLA",Bijoy TV
https://ftp.assadikb.workers.dev/stream.m3u8?id=/bijoytv

#EXTINF:-1 tvg-logo="https://www.jagobd.com/wp-content/uploads/2024/08/pran-RFL.png" group-title="News",Jago News 24
https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s3.aynaott.com/storage/1b5cb8c7901739cd7d201a38d2ab4737",MAASRANGA HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1722/output/index.m3u8

#EXTINF:-1 tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/WyPuDJsBEef-9-uVUA_z/posters/ea20055c-a824-443c-8083-ce8e2da8b922.png" group-title="BANGLA",CHANNEL S
#https://app.ncare.live/live-orgin/channels.stream/playlist.m3u8
https://ftp.assadikb.workers.dev/stream.m3u8?id=/channel_s

#EXTINF:-1 tvg-id="DeshTV" tvg-logo="https://i.postimg.cc/wvBbd56q/Desh-TV.jpg" group-title="BANGLA", Desh TV
#https://bozztv.com/rongo/rongo-DeshTV/index.m3u8
https://bozztv.com/rongo/rongo-DeshTV/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="mohonatv" tvg-name="Mohona TV" tvg-logo="https://www.jagobd.com/wp-content/uploads/2016/02/mohona.jpg" group-title="BANGLA",Mohona TV
#http://103.229.254.25:7001/play/a05t/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mohonatv.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="banglatv" tvg-name="Bangla TV" tvg-logo="https://i.imgur.com/DLGjTfI.png" group-title="BANGLA",Bangla TV
https://cdn.ghuddi.live/Bangla_TV/Bangla_TV_BD/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/RTV.png",RTV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/rtv-sg.stream/playlist.m3u8

#EXTINF:-1 tvg-id="nexustv" tvg-name="Nexus TV" tvg-logo="https://www.jagobd.com/wp-content/uploads/2021/07/nexustv.png" group-title="BANGLA",Nexus TV
https://ftp.assadikb.workers.dev/stream.m3u8?id=nexus_tv

#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Green%20TV.png" group-title="BANGLA",Green TV
https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/chunks.m3u8


#EXTINF:-1 tvg-id="duronto.bd" tvg-logo="https://i.postimg.cc/zBCLNtGZ/Duronto.jpg" group-title="KIDS", Duronto 
http://180.94.28.28:8097//Duronto-TV/index.fmp4.m3u8

#EXTINF:-1 tvg-id="duronto.bd" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Nick_Bangla.png" group-title="KIDS",NICK BANGLA
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://madanitv.assadikb.workers.dev/live.php?id=1341&e=.m3u8

#EXTINF:-1 tvg-id="1345" tvg-name="Sonic Bangla" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sonic_Bangla.png" tvg-language="Bengali" tvg-type="Kids" group-title="KIDS", Sonic Bangla
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://madanitv.assadikb.workers.dev/live.php?id=1345&e=.m3u8

#EXTINF:-1 group-title="KIDS" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1746005940155.png",SRK TV
https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/yBYRgLt/20240813-063955.png" group-title="KIDS",RONGEEN TV
https://server.thelegitpro.in/rongeentv/rongeentv/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://yt3.ggpht.com/ytc/AMLnZu_Gxy8ywjMY6_YPX-1uYtUGA56F0fDoBsH62-ekNA=s900-c-k-c0x00ffffff-no-rj",Makka🔴Live
http://m.live.net.sa:1935/live/quran/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://images-na.ssl-images-amazon.com/images/I/71CywdrFaZL.png",Madina 🔴Live
http://m.live.net.sa:1935/live/sunnah/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="http://103.144.89.251/assets/images/MADANI TV HD1745044303.png",Madani TV Bangla
https://streaming.madanichannel.tv/static/streaming-playlists/hls/d3e49b76-ac06-4689-a641-9200445b647f/master.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Enter%2010%20Bangla.jpeg",Enter 10 Bangla
https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_720p/chunks.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/xi6xX5UBv9knK3AH9aMk/posters/f4db1c12-b10f-46e8-a09b-e0efb8820970.png",Sony Aath
http://live.balajibroadband.com:3500/live/697.m3u8

#EXTINF:-1 group-title="Indian Hindi" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Ay52-JQBv9knK3AHFDWt/posters/00afb30b-3c19-4c4c-abd8-891db94e4767.webp",Sony Max HD
http://live.balajibroadband.com:3500/live/476.m3u8

#EXTINF:-1 tvg-logo="http://ottcasomsapi.maxdigitaltv.com/uploads/channels/channel_147_1737270122_thumb.png" group-title="Indian Hindi", SONY MAX 2
http://live.balajibroadband.com:3500/live/483.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://static.wikia.nocookie.net/logopedia/images/6/60/Gtvhd.png",Gazi TV
http://180.94.28.28:8097//GAZI-TV/index.fmp4.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-id="NAGORIK HD" tvg-logo="http://103.144.89.251/assets/images/NAGORIK1745042776.png",NAGORIK HD
http://103.102.27.173:84/NAGORIK-TV/index.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://s3.aynaott.com/storage/dbc585f70a60b9855b6e13a8ce4cb6f4",T Sports ISP
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports2.m3u8
http://103.102.27.173:84/tvfeed1002/index.m3u8


#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",T Sports
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports.m3u8

#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",T Sports HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports1.m3u8

#EXTINF:-1 tvg-logo="https://abusaeeidx.github.io/Tv-Channel-Logo/CricHD/runded/12-by-xfireflix.png" group-title="SPORTS",A Sports HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-ASports.m3u8
#http://fastshare1.com:8080//live/25711345/late8airline/43447.ts

#EXTINF:-1 tvg-logo="https://ev-img-cdn-lb.shoq.com.pk/prd-peg-data/default/images/logos/live/PTV-Sports.png" group-title="SPORTS",PTV Sports
http://103.102.27.173:84/PTV-SPORTS-HD/index.m3u8
#http://fastshare1.com:8080//live/25711345/late8airline/61674.ts

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/3N8gLCsG/images-(2).jpg",GEO SUPER HD
https://raw.githubusercontent.com/IPTVFlixBD/OopsTv/refs/heads/main/sps1/373118.m3u8

#EXTM3U x-tvg-url="http://fastshare1.com:8080/xmltv.php?username=25711345&password=late8airline"

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/T14Y66P2/20260710-111541.png",WILLOW CRICKET HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow1.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/dV8vWdGq/20260710-112953.png",WILLOW CRICKET 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow2.m3u8

#EXTINF:-1 tvg-id="foxsports501hd.au" tvg-name="AU: Fox Sports 501" tvg-logo="https://i.postimg.cc/q72PSbWm/20260601-214906.png" group-title="SPORTS",Fox Sports 501
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/FOX501HD.m3u8

#EXTINF:-1 tvg-id="skysportscricket.uk" tvg-name="SKY SPORTS CRICKET" tvg-logo="https://i.postimg.cc/3Rz4bwGz/images-(1).jpg" group-title="SPORTS",SKY SPORTS CRICKET
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SkySCric.m3u8


#EXTINF:-1 tvg-logo="https://akamaividz2.zee5.com/image/upload/w_1284,h_723,c_scale,f_webp,q_auto:eco/resources/0-9-channel_2105335046/list/1920x1080list88f79d7c74df4d998da1bbd448f465ff.jpg" group-title="SPORTS", Unite8 Sports 2 FHD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Unite8S2.m3u8

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 1 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_1.png" group-title="SPORTS",SONY SPORTS 1 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_1.m3u8
#http://stalker.hakunamata.workers.dev/play/1101/index.m3u8

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 2 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_2.png" group-title="SPORTS",SONY SPORTS 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_2.m3u8
#https://b4uplay.com/sliv/stream.m3u8?id=1000009277|referer=https://b4uplay.com/


#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 5 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sony_Six_SD.png" group-title="SPORTS",SONY SPORTS 5 HD
http://103.102.27.173:84/SONY-SPORTS-TEN-5HD/index.m3u8


#EXTINF: -1 tvg-id="78" tvg-logo="https://tatalogo.pages.dev/78.png" group-title="SPORTS", Star Sports 1 HD
http://103.102.27.173:84/STAR-SPORTS-1-HD/index.m3u8
#https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSports1.m3u8
#http://114.130.57.233:8080/StarSports1/tracks-v1a1/mono.m3u8?token=SkQuhAXZxgBan1

#EXTINF: -1 tvg-id="235" tvg-logo="https://tatalogo.pages.dev/235.png" group-title="SPORTS", Star Sports 2 HD
http://103.102.27.173:84/STAR-SPORTS-2-HD/index.m3u8
#https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSports2.m3u8
#http://103.151.60.204:881/StarSports2/tracks-v1a1/mono.m3u8?token=Cv90Fr-lyiZYh2


#EXTINF:-1 tvg-id="StarSportsSelectHD1.in" tvg-name="STAR SPORTS SELECT 1 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-1-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 1 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSS_1.m3u8
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276734.ts

#EXTINF:-1 tvg-id="StarSportsSelectHD2.in" tvg-name="STAR SPORTS SELECT 2 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-2-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSS_2.m3u8
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276735.ts

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYYLijjughYF51FVjWeUtGKFckDYqm8B1elAgERP4HIDMf8KpDYC7LpZ4&s=10" group-title="MUSIC", Sangeet Bangla
https://cdn-4.pishow.tv/live/1143/master.m3u8

#EXTINF:-1 tvg-id="zoom" tvg-name="zoom" tvg-logo="http://dugdugilive.com/img/channels/zoom.png" group-title="MUSIC",ZOOM
https://d14c63magvk61v.cloudfront.net/strm/channels/zoom/m1.m3u8

#EXTINF:-1 group-title="MUSIC" tvg-logo="https://i.postimg.cc/RZJmcSt6/9XM.jpg",9X Music
https://d35j504z0x2vu2.cloudfront.net/v1/manifest/0bc8e8376bd8417a1b6761138aa41c26c7309312/9xm/23886666-8fc5-470f-aab1-bd637ed607b1/3.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co.com/9qc3x8F/images-1.jpg" group-title="MUSIC",Music India
#https://cdn-2.pishow.tv/live/226/master.m3u8
http://103.180.212.191:3500/live/250.m3u8 

#EXTINF:-1 tvg-id="3428" tvg-name="Discovery HD Bengali" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/DiscoveryHDBen.png" tvg-language="Bengali" group-title="Infotainment", Discovery HD Bengali
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/DiscoveryBD.m3u8

#EXTINF:-1 tvg-id="573" tvg-name="Discovery Bengali" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Discovery_Channel_Bengali.png" tvg-language="Bengali" group-title="Infotainment", Discovery Bangla
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://madanitv.assadikb.workers.dev/live.php?id=573&e=.m3u8

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/DzBr7HcM/1773936983038.png",STABLE-SPORTS TV
http://198.195.239.50:8095/StarSports2/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/141tq9B1/dc092590a65fc2ac5bd58ccf59cecb51-fgraphic.png",Toffee {premium}
http://main.epgmaker.com/live/y49sz6KMQs/6115263489/522.ts

#EXTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.ibb.co.com/9m9SqPMy/images-2.jpg",Prince [2026]
https://yellow-flower-41fc.cinepixserver00.workers.dev/1:/22-5-26/ottboxbd.COM%20-%20Prince%20Once%20Upon%20a%20Time%20in%20Dhaka%202026%20Bengali%20ORG%201080p%20WEB-DL%20x264.mkv

#EXTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.postimg.cc/DfqzmXQ6/Domm-stablesportstv.jpg",Domm [2026]
https://yellow-flower-41fc.cinepixserver00.workers.dev/1:/21-5-26/Domm%202026%20Bengali%20(ORG)%201080p%20WEB-DL%20x264%20ESubs.mkv

#EXTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.postimg.cc/ryBMGFjw/Rakkhosh-stablesportstv.jpg",Rakkhosh [2026]
http://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/RAKKHOSH%20Bangla%20Movie%20SIAM/Rakkhosh%20(2026)%20Bengali%20720p%20HD-Camrip.mp4

#EXTINF:-1 group-title="MOVIE 2026" tvg-logo="http://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/Bonolota%20Express%20(2026)/MV5BZmY0M2I1NjYtODU4Zi00MmIyLTk0OWUtMDlhN2JmNzFmOWI1XkEyXkFqcGc@._V1_SX300.jpg",Bonolota Express [2026]
http://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/Bonolota%20Express%20(2026)/Bonolota%20Express%20(2026)%20Bengali%20Amazon%20WEB-DL%20H264%20AAC%20720p.mkv
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
# SAVE FILES (LOOP)
# =========================

# This loop automatically creates every file inside OUTPUT_FILES list
for filename in OUTPUT_FILES:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"✅ {filename} Updated Successfully")
