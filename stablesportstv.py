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
#EXTINF:-1 tvg-id="tapmad-14131" tvg-logo="https://d34080pnh6e62j.cloudfront.net/images/channels/mobile_large/17809370631020x576.jpg" group-title="LIVE SPORTS", Bangladesh vs Australia | Australia Tour of Bangladesh 2026
https://premierleagpl23.akamaized.net/hls/live/2107108/tapmad-P2s6L_FiN@L-UrU/master.m3u8 


#EXTINF:-1 tvg-chno="402" tvg-logo="https://www.fancode.com/skillup-uploads/cms-media/Aus-vs-Ban_Web-match-card_1780908762762.png",Bangladesh vs Australia 
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=5689304538fa9f3bb3da99c939a2ad4f:6907c88ed8ebdd35a2fa80b9684715e1
https://otte.live.fly.ww.aiv-cdn.net/sin-nitro/live/clients/dash-sd/enc/v8g0dlo4z8/out/v1/946019f85dc64ae99ff9ce64a9727a62/cenc-sd.mpd

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://www.fancode.com/skillup-uploads/cms-media/Aus-vs-Ban_Web-match-card_1780908762762.png",Bangladesh vs Australia 
http://stalker.hakunamata.workers.dev/play/1099/index.m3u8

#EXTINF:-1 tvg-logo="https://www.fancode.com/skillup-uploads/cms-media/Aus-vs-Ban_Web-match-card_1780908762762.png" group-title="LIVE SPORTS",Bangladesh vs Australia (Local ISP)
http://103.59.176.72:8083/live1/tracks-v1a1/mono.m3u8?token=123

#EXTINF:-1 tvg-logo="https://i.postimg.cc/d3SwnmmH/20260613-055610.jpg"group-title="LIVE SPORTS" group-title="",FIFA World Cup 2026 (Fast HD)
https://d1voy022wjnlk0.bioscopelive.com/out/v1/0bbe405e711143b8af5ee21b80b5b0cc/index.m3u8|x-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzJkYjE1MjJmMDU0ZDg1Yzc3NmFmZjlkNDU2NjcxODNlNmZlNWNjYWUwYjAwNWI1OTVhMTAxY2RmNDNlYmIyY2YzMTBiZDExMTZlOTQ4YjEiLCJpYXQiOjE3ODA3OTcxMzEuNTQwNDAxLCJuYmYiOjE3ODA3OTcxMzEuNTQwNDAzLCJleHAiOjE4MTIzMzMxMzEuNTM1MDMyLCJzdWIiOiIxODAwMDA4NDg5MDA2NjUzNDQiLCJzY29wZXMiOlsibWFuYWdlX3Byb2ZpbGVzIl19.a6GUyqbwLfixROwUhNTzaYrrYBgVR6FHI_40FpjZ9l7P20WHcv-7AbEz-XPYhGnb1Q9JHAKdMA9pBY1Od2UZsYeEw6f7Myjc0VK2kqqXdagwHTlIHvHwxkoTVfpagQNiJF4ffJZ_6j87aCR6PEUEuTWQwjnLjbnvBpu0cgLUr5p56sHGm0mGV_vbIFirvZHVYwxLZGjBmo-njpfZcvuQPq5sUT3n-j4VNX4sh8tsvaAJaqlXLnq-DIGTBGNu9efsHNTiMzFUk5gEOYlWnNGewcbsuDsP3QFINeUBRzjBP9bPXjHfv5tmvKfQaExPZgFpxpWpZyQ5PZnmuxvWawNMKLBGV3qWqNPeVc1Fphhac3vloTNtMK5UP7EZtDRUQoJWra1irCMYn0ao1oEzfrtinhw038aNSe9z5EmF_tCi0XnQigVJM_XLwmgWbVxsWq92iC3HU2dHcelqMNiFk9gMleKIgGVA2sDeLfNsM0pco8656R7TySgSBycVvTyyU4_G1QVafpmPp5Lcmhi4KxVBAOAhY5iy0ZLDC4jO366wy_5yguY7sVPb6JWiUATVcBsLbvIPmgM9laQEZttxLMPHpnlPwUGljip5J61E235GXAV-WStahGaagjgja7dDRFwPVzvlMzSX9S7MpyVyRejmre60x8HvXkgCLhEfEn027YM

#EXTINF:-1 tvg-logo="https://i.postimg.cc/RFYx7cfR/20260612-205410.jpg"group-title="LIVE SPORTS" group-title="",FIFA World Cup 2026 (4K)
http://starhub.pro/live/farhat-3379/67897-913379/745270.ts

#EXTINF:-1 tvg-logo="https://i.postimg.cc/hjQwQXST/20260613-104845.jpg" group-title="LIVE SPORTS",FIFA World Cup 2026 (HD)
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=549ab7cd35a64bb6bb479ecead04d69d:829799ed534d11fcadeb4b192467e050
https://qp-pldt-live-bpk-ucd-prod.akamaized.net/bpk-tv/ch299/default/index.mpd

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/4NWsyqfM/20260607-190818.jpg",FIFA World Cup 2026🅰️
http://103.59.176.72:8083/live1/tracks-v1a1/mono.m3u8?token=123

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/4NWsyqfM/20260607-190818.jpg",FIFA World Cup 2026🅱️
https://amitomar.bdixbd.net/hoichoi.pro1/tracks-v1a1/index.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/7LW7Jnw0/20260612-094836.jpg",FIFA World Cup 2026(Tapmad)
https://premierleagpl23.akamaized.net/hls/live/2107108/tapmad-P2s6L_FiN@L-UrU/master.m3u8


#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/Y903JSq8/20260612-095648.jpg",FIFA World Cup 2026 HD
https://1nyaler.streamhostingcdn.top/stream/23/index.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/KvpgH5gb/20260612-095057.jpg",FIFA World Cup 2026 HD
https://1nyaler.streamhostingcdn.top/stream/32/index.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/zfjBKhMd/20260612-205515.jpg",FIFA World Cup 2026 🇦🇷
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=a7d11d37a1f7611ee88d4db880171f32:68f96d618b0b956b008c445896a25a79
https://otte.live.fly.ww.aiv-cdn.net/gru-nitro/live/clients/dash/enc/ubehitlwzo/out/v1/8e09c381a51f4366a19e979418112e8f/cenc.mpd

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/pdpNmLGj/20260607-191102.jpg",FIFA World Cup 2026 🇦🇷
#http://daleplaytv.vip:80//live/4nd9wbtu/c5hrn9eFhfsa/81252.ts
http://cdn.tv-rds.workers.dev/TYCSPT.m3u8
#https://amg26268-amg26268c14-freelivesports-emea-10267.playouts.now.amagi.tv/ts-us-e2-n2/playlist/amg26268-sportsstudio-tycsports-freelivesportsemea/playlist.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/NjnJP7D0/20260607-191116.jpg",FIFA World Cup 2026 🇧🇷
https://dfr80qz435crc.cloudfront.net/MNOP/Amagi/Caze/Caze_TV_BR/1080p-vtt/index.m3u8
#https://dfr80qz435crc.cloudfront.net/MNOP/Amagi/Caze/Caze_TV_BR/Caze_TV.m3u8


#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/K83r4XPs/20260607-191047.jpg",FIFA World Cup 2026 🇮🇳
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=fbbfd9ce4bbe4d818b16df7dfe89f05b:1e96d0f88ef740e982d6f6105721c8bc
https://d1g8wgjurz8via.cloudfront.net/bpk-tv/Zeebanglacinema/default/manifest.mpd

#https://zati5.hasanhabibmottakin.workers.dev/0-9-zeecafehd/index.m3u8


#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/YqZY5nck/20260607-191024.jpg",FIFA World Cup 2026 🇮🇳
https://zati5.hasanhabibmottakin.workers.dev/0-9-channel_2105335046/index.m3u8
#http://66.102.126.10:8000/play/a022/index.m3u8

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/rFPRDbK0/20260612-205544.jpg",FIFA World Cup 2026 🇮🇳
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=fbbfd9ce4bbe4d818b16df7dfe89f05b:1e96d0f88ef740e982d6f6105721c8bc
https://d1g8wgjurz8via.cloudfront.net/bpk-tv/Zeebanglacinema/default/manifest.mpd

#EXTINF:-1 group-title="LIVE SPORTS" tvg-logo="https://i.postimg.cc/cLzP2BbN/20260604-213137.jpg",FIFA World Cup 2026 🇵🇰
http://198.195.239.50:8095/ptv/index.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/7ZRGLxFh/images-(1).jpg" group-title="LIVE SPORTS",FIFA World Cup 2026 
https://a62dad94.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/UmFrdXRlblRWLWV1X0ZJRkFQbHVzRW5nbGlzaF9ITFM/playlist.m3u8

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/13XVVyg3/1773936967533.png",STABLE-SPORTS TV
https://feed.hasanhabibmottakin.workers.dev/edge1/1/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1676193184888_2.png&w=1080&q=75",SANGSAD BANGLADESH
https://owrcovcrpy.gpcdn.net/bpk-tv/1709/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://ssl.com.bd/sites/default/files/BTV%20Logo%20Gallery.png",BTV
https://feed.hasanhabibmottakin.workers.dev/edge1/3/index.m3u8


#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1735648543857_Poster.jpg&w=1080&q=75",BTV News
http://premimum.online/live/jen12345/jen54321/998.ts

#EXTINF:-1 tvg-logo="https://www.btvlive.gov.bd/_next/static/media/btv-logo.d937bde9.svg" group-title="BANGLA",BTV CTG
https://www.btvlive.gov.bd/live/37f2df30-3edf-42f3-a2ee-6185002c841c/BD/a707f2dc-9704-413a-a67c-17c64a77c350/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Xi_Ga5oBNnOkwJLWkhKP/posters/ef2899d5-1ae0-4fee-aee5-45f9b0b3ba80.png",Somoy TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1702/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770186895850.png",News 24 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1708/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770189826301.png",Star News
https://owrcovcrpy.gpcdn.net/bpk-tv/1710/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770187361105.png",SATV HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1720/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770188008067.png",Channel 9 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1729/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://i.postimg.cc/1t1P0VMt/images-(1).jpg",DBC News
https://owrcovcrpy.gpcdn.net/bpk-tv/1728/output/1728.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PS_La5oBNnOkwJLWLRN_/posters/e8c444fd-ee3b-4bf3-bb0a-f969bc295f82.png",Ekattor TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1705/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://yt3.googleusercontent.com/8Q8MCd6ypr2Hzbp60VE_stJPl063kQYfeTxdIQkAXRfhdzxByLl0sJYHsk43uTM4W_cOzwcbPQ=s160-c-k-c0x00ffffff-no-rj",Channel 24
https://owrcovcrpy.gpcdn.net/bpk-tv/1703/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/ES_cZZsBNnOkwJLW1Oz1/posters/b872b8f5-cb6b-45a1-a1cd-7609df51d614.png",Independent TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1704/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PiL635oBEef-9-uV2uCe/posters/36f380e0-6c71-4b27-a73b-2afb3ce7e982.png",Jamuna TV
https://owrcovcrpy.gpcdn.net/bpk-tv/1701/output/index.m3u8

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
https://owrcovcrpy.gpcdn.net/bpk-tv/1716/output/index.m3u8

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
http://116.204.149.16/globaltv/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/qnv835oBcqxnFHJBuQcB/posters/348dfac3-c1e0-485d-a72b-3d282c9e2c73.png",Channel I
https://owrcovcrpy.gpcdn.net/bpk-tv/1723/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Deepto%20TV.jpeg",Deepto TV
https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8

#EXTINF:-1 tvg-logo="https://s3.aynaott.com/storage/58658d4594ca1ff3c5031c9d8e3d9fc0" group-title="BANGLA",Boishakhi TV
https://boishakhi.sonarbanglatv.com/boishakhi/boishakhitv/index.m3u8

#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Bijoy%20TV.png" group-title="BANGLA",Bijoy TV
http://main.epgmaker.com/live/y49sz6KMQs/6115263489/581.ts

#EXTINF:-1 tvg-logo="https://www.jagobd.com/wp-content/uploads/2024/08/pran-RFL.png" group-title="News",Jago News 24
https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://s3.aynaott.com/storage/1b5cb8c7901739cd7d201a38d2ab4737",MAASRANGA HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1722/output/index.m3u8

#EXTINF:-1 tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/WyPuDJsBEef-9-uVUA_z/posters/ea20055c-a824-443c-8083-ce8e2da8b922.png" group-title="BANGLA",CHANNEL S
#https://app.ncare.live/live-orgin/channels.stream/playlist.m3u8
http://103.229.254.25:7001/play/a060/index.m3u8

#EXTINF:-1 tvg-id="DeshTV" tvg-logo="https://i.postimg.cc/wvBbd56q/Desh-TV.jpg" group-title="BANGLA", Desh TV
#https://bozztv.com/rongo/rongo-DeshTV/index.m3u8
https://bozztv.com/rongo/rongo-DeshTV/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="mohonatv" tvg-name="Mohona TV" tvg-logo="https://www.jagobd.com/wp-content/uploads/2016/02/mohona.jpg" group-title="BANGLA",Mohona TV
#http://103.229.254.25:7001/play/a05t/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mohonatv.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="banglatv" tvg-name="Bangla TV" tvg-logo="https://i.imgur.com/DLGjTfI.png" group-title="BANGLA",Bangla TV
http://116.204.149.16/banglatv/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/RTV.png",RTV
#http://tvn3.chowdhury-shaheb.com/rtv/index.m3u8
http://116.204.149.16/rtvhd/index.m3u8

#EXTINF:-1 tvg-id="nexustv" tvg-name="Nexus TV" tvg-logo="https://www.jagobd.com/wp-content/uploads/2021/07/nexustv.png" group-title="BANGLA",Nexus TV
http://103.158.133.62:8080/nexustv/index.m3u8

#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Green%20TV.png" group-title="BANGLA",Green TV
https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/chunks.m3u8


#EXTINF:-1 tvg-id="duronto.bd" tvg-logo="https://i.postimg.cc/zBCLNtGZ/Duronto.jpg" group-title="KIDS", Duronto 
http://103.204.43.87:8080/live/1/1/290.m3u8
#https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/duronto.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="duronto.bd" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Nick_Bangla.png" group-title="KIDS",NICK BANGLA
http://103.204.43.87:8080/live/1/1/275.m3u8

#EXTINF:-1 tvg-id="1345" tvg-name="Sonic Bangla" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sonic_Bangla.png" tvg-language="Bengali" tvg-type="Kids" group-title="KIDS", Sonic Bangla
http://103.204.43.87:8080/live/1/1/274.m3u8

#EXTINF:-1 group-title="KIDS" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1746005940155.png",SRK TV
https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/yBYRgLt/20240813-063955.png" group-title="KIDS",RONGEEN TV
https://server.thelegitpro.in/rongeentv/rongeentv/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://yt3.ggpht.com/ytc/AMLnZu_Gxy8ywjMY6_YPX-1uYtUGA56F0fDoBsH62-ekNA=s900-c-k-c0x00ffffff-no-rj",Makka🔴Live
http://m.live.net.sa:1935/live/quran/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://images-na.ssl-images-amazon.com/images/I/71CywdrFaZL.png",Madina 🔴Live
http://m.live.net.sa:1935/live/sunnah/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="http://103.144.89.251/assets/images/MADANI TV HD1745044303.png",Madani TV Bangla
http://103.204.43.87:8080/live/1/1/304.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Enter%2010%20Bangla.jpeg",Enter 10 Bangla
https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_720p/chunks.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/xi6xX5UBv9knK3AH9aMk/posters/f4db1c12-b10f-46e8-a09b-e0efb8820970.png",Sony Aath
#https://bldcmprod-cdn.toffeelive.com/cdn/live/sonyaath/playlist.m3u8
#http://stvlive.net:8080/sonyaath/index.m3u8
http://198.195.239.50:8095/SonyAath/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="Indian Hindi" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Ay52-JQBv9knK3AHFDWt/posters/00afb30b-3c19-4c4c-abd8-891db94e4767.webp",Sony Max HD
http://198.195.239.50:8095/SonyMAX/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-logo="http://ottcasomsapi.maxdigitaltv.com/uploads/channels/channel_147_1737270122_thumb.png" group-title="Indian Hindi", SONY MAX 2
http://maxotts.maxdigitaltv.com/x-media/C111/master.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://static.wikia.nocookie.net/logopedia/images/6/60/Gtvhd.png",Gazi TV
https://tvsen1.aynaott.com/Ravc7gPCZpxk/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-id="NAGORIK HD" tvg-logo="http://103.144.89.251/assets/images/NAGORIK1745042776.png",NAGORIK HD
http://198.195.239.50:8095/nagorik/index.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://s3.aynaott.com/storage/dbc585f70a60b9855b6e13a8ce4cb6f4",T Sports ISP
http://103.59.176.72:8083/live1/tracks-v1a1/mono.m3u8?token=123

#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",T Sports
#https://autumn-shape-b04a.soft-disk-1347.workers.dev/?url=http://stvlive.net:8080/tsports1/tracks-v1a1/mono.m3u8
#https://kamrul.anik-islam14.workers.dev/?url=http://stvlive.net:8080/tsports1/tracks-v1a1/mono.m3u8
#https://futbollive.online/T-Sports/tracks-v1a1/mono.m3u
http://172.20.21.22/live/skyfeed1005/index.m3u8

#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",T Sports HD
http://198.195.239.50:8095/Tsports/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-logo="https://abusaeeidx.github.io/Tv-Channel-Logo/CricHD/runded/12-by-xfireflix.png" group-title="SPORTS",A Sports HD
http://103.204.43.87:8080/live/1/1/309.m3u8
#http://103.229.254.25:7001/play/a087/index.m3u8
#http://198.195.239.50:8095/Eurosport/index.m3u8

#EXTINF:-1 tvg-logo="https://ev-img-cdn-lb.shoq.com.pk/prd-peg-data/default/images/logos/live/PTV-Sports.png" group-title="SPORTS",PTV Sports
http://198.195.239.50:8095/ptv/index.m3u8
#http://main.epgmaker.com/live/y49sz6KMQs/6115263489/498.ts

#EXTINF:-1 tvg-id="ext" tvg-name="Willow" tvg-logo="https://raw.githubusercontent.com/subirkumarpaul/Logo/refs/heads/main/Willow%20TV.jpeg" group-title="SPORTS",Willow 
http://main.epgmaker.com/live/y49sz6KMQs/6115263489/517.ts
#https://tvsen5.aynaott.com/willowhd/index.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/V6nscV99/20260601-214906.png" group-title="SPORTS",FOX SPORTS 501 HD
http://sewv654wfcsdwfi87fwvgbngh.siauliairsavlt.pw/iptv/VCQ4ADX96VH4G8PY7URBWRQU/19146/index.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/6Q9sKNFm/skysports-C-stablesportstv.jpg",SKY SPORTS CRICKET
http://sewv654wfcsdwfi87fwvgbngh.siauliairsavlt.pw/iptv/VCQ4ADX96VH4G8PY7URBWRQU/9258/index.m3u8

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 1 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_1.png" group-title="SPORTS",SONY SPORTS 1HD
http://stalker.hakunamata.workers.dev/play/1101/index.m3u8

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 2 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_2.png" group-title="SPORTS",SONY SPORTS 2 HD 🅰️
https://b4uplay.com/sliv/stream.m3u8?id=1000009277|referer=https://b4uplay.com/
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276739.ts

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 2 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_2.png" group-title="SPORTS",SONY SPORTS 2 HD 🅱️
http://main.epgmaker.com/live/y49sz6KMQs/6115263489/513.ts

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 5 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sony_Six_SD.png" group-title="SPORTS",SONY SPORTS 5 HD
http://66.102.126.10:8000/play/a010/index.m3u8

#EXTINF:-1 tvg-chno="402" tvg-logo="https://iili.io/KWn2Z0u.png",FANCODE
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=5689304538fa9f3bb3da99c939a2ad4f:6907c88ed8ebdd35a2fa80b9684715e1
https://otte.live.fly.ww.aiv-cdn.net/sin-nitro/live/clients/dash-sd/enc/v8g0dlo4z8/out/v1/946019f85dc64ae99ff9ce64a9727a62/cenc-sd.mpd

#EXTINF: -1 tvg-id="78" tvg-logo="https://tatalogo.pages.dev/78.png" group-title="Sports", Star Sports 1 HD
http://stalker.hakunamata.workers.dev/play/1088/index.m3u8

#EXTINF: -1 tvg-id="235" tvg-logo="https://tatalogo.pages.dev/235.png" group-title="Sports", Star Sports 2 HD
http://stalker.hakunamata.workers.dev/play/1446/index.m3u8

#EXTINF:-1 tvg-id="StarSportsSelectHD1.in" tvg-name="STAR SPORTS SELECT 1 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-1-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 1 HD
http://103.204.43.87:8080/live/1/1/244.m3u8
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276734.ts

#EXTINF:-1 tvg-id="StarSportsSelectHD2.in" tvg-name="STAR SPORTS SELECT 2 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-2-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 2 HD
http://103.204.43.87:8080/live/1/1/243.m3u8
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
http://103.159.180.34:5001/live/3428.m3u8

#EXTINF:-1 tvg-id="573" tvg-name="Discovery Bengali" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Discovery_Channel_Bengali.png" tvg-language="Bengali" group-title="Infotainment", Discovery Bengali
http://103.159.180.34:5001/live/573.m3u8

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
