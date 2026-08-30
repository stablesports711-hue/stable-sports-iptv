import requests

OUTPUT_FILES = [
    "STABLE-SPORTS TV.m3u"
]

sources = [
    "https://raw.githubusercontent.com/stablesports711-hue/stable-sports-toffee/refs/heads/main/toffee.m3u",
    "https://raw.githubgdhshgshgehhshusercontent.com/srhady/Hady/refs/heads/main/akash_live.m3u",
    "https://raw.githubusercontent.com/stablesports711-hds/main/cr.m3u"
]

# =========================
# CUSTOM CHANNELS (TOP)
# =========================

custom_channels = """#EXTM3U
#EXTINF:-1 tvg-logo="https://i.postimg.cc/qq01x2J2/20260829-210915.png" group-title="LIVE SPORTS",Womens Asia Cup 2026
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=290e09c837da78d5cd961978d390515c:b748836c71e6a4ca68ef5b5652db6247
https://otte.cache.aiv-cdn.net/iad-nitro/live/clients/dash/enc/tll6uwepxa/out/v1/a7f67cbb33df46539312956427343886/cenc.mpd

#EXTINF:-1 tvg-logo="https://i.postimg.cc/qq01x2J2/20260829-210915.png" group-title="LIVE SPORTS",Womens Asia Cup 2026
http://103.185.24.134:3001/TSportsHD/index.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/qq01x2J2/20260829-210915.png" group-title="LIVE SPORTS",Womens Asia Cup 2026
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_1.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/qq01x2J2/20260829-210915.png" group-title="LIVE SPORTS",Womens Asia Cup 2026 HINDI
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_3.m3u8

#KODIPROP:inputstream.adaptive.license_type=clearkey#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQujBtPOgUpOHILwHzxdBP5T8Q4sgCfxOGrHdlJCHp2Rfd4Ep2UFJLSLbRP&s=10" group-title="LIVE SPORTS", European T20 Premier League
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow2.m3u8


#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEVxUsJZGBtq8vbAF56bV0YbEaic9ES6RwRi8EwvQfbgu1eQJG82SPZ7SL&s=10.png" group-title="LIVE SPORTS",DP WORLD TOUR Live
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=9590ea43d0f770c24205e23440d8af8c:b127454380d8fffc3acd12575b2b4adb
https://dash-ott.bia-cf.live.pv-cdn.net/iad-nitro/live/clients/dash/enc/mnxueephr4/out/v1/b0eeb77d4e1f4b02b4e3325fd712267e/cenc.mpd

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League (Fast)
https://live05.meung.app/live/33982309.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League (Fast)
https://playback.livetl001.com/live/69be75e0a0a45974afb67776_1080p.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League (Fast)
https://playback.livetl001.com/live/69cf6331585c5992182f4160_1080p.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League (Fast)
https://playback.livetl001.com/live/69aa9525f5ec459ae275b43f_1080p.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League
https://andro.226503.xyz/checklist/androstreamlivebs3.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League
http://2756d46c.akciatv.ru/iptv/7FRNF6CY9A9TG3/9334/index.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League
https://raw.githubusercontent.com/IPTVFlixBD/OopsTv/refs/heads/main/asia/1424311.m3u8

#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League


#EXTINF:-1 tvg-logo="https://imgcdn.espos.id/@espos/images/2022/08/logo-liga-inggris.jpg?quality=60" group-title="LIVE SPORTS",English Premier League
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSS_1.m3u8
https://a9#KODIPROP:inputstream.adaptive.license_type=clearkey6aivottlinear-a.akamaihd.net/OTTB/iad-nitro/live/clients/dash/enc/rhf2dwosdt/out/v1/ee550d2a68d846c797e6ce4de2e8b76d/cenc.mpd

#EXTINF:-1 tvg-logo="https://brandingstyleguides.com/wp-content/guidelines/2024/12/motogp-online.jpg" group-title="LIVE SPORTS",MOTO GP
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=82dfca238e8c4b430a3269db71965db9:a00b28caf4ac628e77a553d440c0ddca
https://otte.cache.aiv-cdn.net/iad-nitro/live/clients/dash/enc/b3b3fkmrbl/out/v1/1084d5c9a97a4c5b9f9554c88f486646/cenc.mpd

#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=e03f302ec4dabcccca82cc9f76731ec9:53ea1027d2bf2893a552cf15bc0366de
https://a40live-emt-pv-ta-amazon.akamaized.net/$T$2D3RhEOhAQWhBFgkYWY3NDZlZjAtYzM0OC00MGM1LWFjN2UtYTVhZWIzNjhiNjA0WJCnAWpwcmltZXZpZGVvBBpqpPkEBhpqkTKEA2Zha2FtYWkCeClzc2lkOjIzZGYwMDAwLTUxNzAtNDRkNy04NjFlLTI5MTI4OTc4MmJmMhkBOKEFoQJ4My9zMDVnaGwyYnplL291dC92MS8zMGYzYWQ5YmEyYzM0MDczOWVhMjk0M2YyOWQ0NGIzMhkBPIFiVVNYILJ6NpO79L3nK059TfPcRGnrS77k7itq2Nq8ElzsLlFR/PDX/709b3c4313a9405ab5e8634864c7cc3b/v1/dash/590183725645/imdb_amagi_amzn1_dv_live_csid_5357cf2a-51c8-4fa5-b996-cd307e0b7edc_us-west-2_pdx_dash_h264/startover/clients/dash/manipulated-manifest-pdx-prod/enc/s05ghl2bze/out/v1/30f3ad9ba2c340739ea2943f29d44b32/fc4b2d48-7e13-4cc3-bdde-9a83d219cfb5-cenc.mpd?aws.sessionId=d5920555-de6c-4bf5-9e6e-ad630bc17a30


#EXTINF:-1 group-title="PROMO" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhBdK9UlnKlH97BTRb08BItz6h67i6vJ05O2MEJj-zxhSVqZLquvfvdEc&s=10.png",TECNO | SAFF CHAMPIONSHIP BANGLADESH 2026[COMMING SOON]
https://res.cloudinary.com/qleik3si/video/upload/v1785235285/VN20260728_161756_ev6pow.mp4

#EXTINF:-1 group-title="Sports Video" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRug1sv4kDm3YHt7RDjQUfhJPUoFsFvFl23Vfv0vTgm82Q9H0iZOmjqZSs&s=10.png",FIFA Final Match
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-toffee/refs/heads/main/final.m3u8

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/13XVVyg3/1773936967533.png",110.STABLE-SPORTS TV™
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=69a5aa835a061ce64a630d1046727e40:d02feac8a999bd06bf4059bf33411749
https://a96aivottlinear-a.akamaihd.net/OTTB/iad-nitro/live/clients/dash/enc/rhf2dwosdt/out/v1/ee550d2a68d846c797e6ce4de2e8b76d/cenc.mpd
#https://res.cloudinary.com/qleik3si/video/upload/v1785235285/VN20260728_161756_ev6pow.mp4

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1676193184888_2.png&w=1080&q=75",111.SANGSAD BANGLADESH
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/songsodtv-world.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE3J33gFY0MZ-B60vhItbVad_Ox1t645Ahi0hz_Yhjgg&s=10.png",112.BTV
https://akash-by-hady.srhady.workers.dev/live/122.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.btvlive.gov.bd/_next/image?url=https%3A%2F%2Fd38ll44lbmt52p.cloudfront.net%2Fcms%2Fchannel_poster%2F1735648543857_Poster.jpg&w=1080&q=75",113.BTV News
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/btvbd-office-sg.stream/index.m3u8
http://103.165.93.31:8095/btv/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH0LsRdDHYdFgUA6Uus-wPC6V5G59KENdmzhDy3mhX_TGU0YAEX1NBTzs_&s=10.png" group-title="BANGLA",114.BTV CTG
https://tvsen6.aynaott.com/TjGR1GcxKetHNVcMVxbq/index.m3u8
#http://fastshare1.com:8080//live/25711345/late8airline/3818.ts

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Xi_Ga5oBNnOkwJLWkhKP/posters/ef2899d5-1ae0-4fee-aee5-45f9b0b3ba80.png",115.Somoy TV
http://172.17.50.112:84/ant1008/video.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1713/output/index.m3u8


#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/ES_cZZsBNnOkwJLW1Oz1/posters/b872b8f5-cb6b-45a1-a1cd-7609df51d614.png",116.Independent TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/independent-8-org.stream/tracks-v1a1/mono.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1704/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PiL635oBEef-9-uV2uCe/posters/36f380e0-6c71-4b27-a73b-2afb3ce7e982.png",117.Jamuna TV
http://103.165.93.31:8095/jamunaTv/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770186895850.png",118.News 24 HD
https://tvsen6.aynaott.com/cdgr3tw6WoG7JyRnLbi0/tracks-v1a1/mono.ts.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1708/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770189826301.png",119.Star News
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/starnewsbd.stream/tracks-v1a1/mono.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1710/output/index.m3u8

#EXTINF:-1 tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1781163068414.png" group-title="BANGLA",120.Channel 1
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel1bd.stream/tracks-v1a1/mono.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1702/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://i.postimg.cc/1t1P0VMt/images-(1).jpg",121.DBC News
https://tvsen6.aynaott.com/pF66Tkz0qFwP2aMMqHyt/tracks-v1a1/mono.ts.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1728/output/1728.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/PS_La5oBNnOkwJLWLRN_/posters/e8c444fd-ee3b-4bf3-bb0a-f969bc295f82.png",122.Ekattor TV
http://103.165.93.31:8095/ekattorTv/tracks-v1a1/mono.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1705/output/index.m3u8

#EXTINF:-1 group-title="News" tvg-logo="https://yt3.googleusercontent.com/8Q8MCd6ypr2Hzbp60VE_stJPl063kQYfeTxdIQkAXRfhdzxByLl0sJYHsk43uTM4W_cOzwcbPQ=s160-c-k-c0x00ffffff-no-rj",123.Channel 24
https://stream.ottplus.live/live/channel_24_abr/index.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1703/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770187361105.png",124.SATV HD
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
#https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/satvoff5666.stream/playlist.m3u8
https://tvsen6.aynaott.com/rELXiuUXqbgzPb06Npom/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1770188008067.png",125.Channel 9 HD
https://owrcovcrpy.gpcdn.net/bpk-tv/1729/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://yt3.googleusercontent.com/ZBW3QTVsP4woeK2-sVqWPZTiUECW5BCkY-fO4q0IJ70-jrPhgn-LG0BGVckENkCS0aQK_193GA=s900-c-k-c0x00ffffff-no-rj",126.ATN News
http://103.165.93.31:8095/atnNews/video.m3u8
#https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnws-sg.stream/tracks-v1a1/mono.m3u8


#EXTINF:-1 tvg-logo="https://s6.gifyu.com/images/image27cfa7002786c232.png" group-title="BANGLA",127.ATN Bangla
http://103.165.93.31:8095/atnBangla/index.m3u8
https://tvsen5.aynaott.com/P3y2URgG7LDe/tracks-v1a1/mono.ts.m3u8
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
#https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnbd-8-org.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcL5B2kjt9gVkv6UW_xtSxlWADze_mnkt8nqgrlN3oQoWSRFOF3M4NAko&s=10.png" group-title="BANGLA",128.Ananda TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/


#EXTINF:-1 group-title="BANGLA" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaPR38fHKwxReRab3F-GAneyjy8zFYySIhHCfhPqL3al-wiIvnniFdq_IQ&s=10.png",129.NTV
https://tvsen5.aynaott.com/xV4jEKf3D9zc/tracks-v1a1/mono.ts.m3u8
#https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/NTV.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1716/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://yt3.googleusercontent.com/ytc/AIdro_lznWhV194D6rfuuCsBIe8SS11AMjZ3H-AbQxhpuxfys8M=s900-c-k-c0x00ffffff-no-rj",130.BanglaVision
https://tvsen5.aynaott.com/tgUzpPc9r6xw/tracks-v1a1/mono.ts.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1715/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/MyK__poBEef-9-uVmf5l/posters/1eadef5b-28e7-4dc2-b42f-c67a3357c9a0.png",131.Asian TV
https://tvsen6.aynaott.com/pKb5k6NnzxsKpWUs6E8M/index.m3u8

#EXTINF:-1 tvg-id="mytv" tvg-name="MY TV" tvg-logo="https://i.postimg.cc/HxGF4V2b/20250529_103226.png" group-title="BANGLA",132.MY TV
#https://tvsen6.aynaott.com/mytv/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mytv-up-off.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://yt3.googleusercontent.com/4G-Aw-9Y2BiYRKQWIkTYWMp68o1XFiPn67SiKacsElkUnizh-75w9jLV7DKZWa6D4C5W8aicYA=s900-c-k-c0x00ffffff-no-rj",133.Ekushey TV
http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/o3v235oBcqxnFHJBkAdC/posters/159af631-796d-4342-a2a7-c272f32bcd32.png",134.Ekhon TV
#EXTVLCOPT:http-referrer=https://www.jagobd.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://static.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/globaltv.stream/playlist.m3u8?wmsAuthSign=|Referer=https://www.jagobd.com/

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/0y_tDJsBNnOkwJLWNrdE/posters/2ff058e1-630f-4657-8dc6-b677e65642c5.png",135.Global TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/qnv835oBcqxnFHJBuQcB/posters/348dfac3-c1e0-485d-a72b-3d282c9e2c73.png",136.Channel I
https://tvsen6.aynaott.com/FNHpYvGZ7FkCE10PwTHm/tracks-v1a1/mono.ts.m3u8
#https://owrcovcrpy.gpcdn.net/bpk-tv/1723/output/index.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlCvG4DXypXNarh-qyjTrspdDecr1FzN-jE0TkkQXBxA&s=10.png",137.Deepto TV
https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8

#EXTINF:-1 tvg-logo="https://yt3.googleusercontent.com/YHOtAuLJzkb9qzX2S2r_EvXUINm5hwRq9MvaNcY9Psv_Hjjqi5GeZDqkY45HO0gm538tSDsMfw=s900-c-k-c0x00ffffff-no-rj" group-title="BANGLA",138.Boishakhi TV
https://boishakhi.sonarbanglatv.com/boishakhi/boishakhitv/index.m3u8

#EXTINF:-1 tvg-logo="https://assets-prod.services.toffeelive.com/bns4l5sBcqxnFHJBVZ32/posters/feaf9f3d-cc3b-4a3d-81a3-2cb703e561eb.png" group-title="BANGLA",139.Bijoy TV
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://tvsen6.aynaott.com/N8Xbo5vdwVU6sF43RsW0/index.m3u8

#EXTINF:-1 tvg-logo="https://www.jagobd.com/wp-content/uploads/2024/08/pran-RFL.png" group-title="News",140.Jago News 24
https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6TZF90ZkLIAxbL6M66zH3uUSkJLEUCdYNeiFAC7g6Pw&s=10.png",141.MAASRANGA HD
https://mtv.sunplex.live/MAASRANGA/index.m3u8

#EXTINF:-1 tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/WyPuDJsBEef-9-uVUA_z/posters/ea20055c-a824-443c-8083-ce8e2da8b922.png" group-title="BANGLA",142.CHANNEL S
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://app.ncare.live/live-orgin/channels.stream/playlist.m3u8


#EXTINF:-1 tvg-id="DeshTV" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfHjo6UH5GgOVP49haq7DAGn4vWx7Q6tRDEwarZqJWvDRzWwQl1R5EEI98&s=10.png" group-title="BANGLA",143.Desh TV
#https://bozztv.com/rongo/rongo-DeshTV/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/deshtv.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="mohonatv" tvg-name="Mohona TV" tvg-logo="https://yt3.googleusercontent.com/wXqEY4h1ozodob19G3s6-RCx7H3uJpVKKGJNOVSiOGd--JddX6kMZ649dVG-6XKw_K2YseIPsQ=s900-c-k-c0x00ffffff-no-rj" group-title="BANGLA",144.Mohona TV
#http://103.229.254.25:7001/play/a05t/index.m3u8
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mohonatv.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="banglatv" tvg-name="Bangla TV" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPD3Qo1CSwd9ZcA0b6xTS1I66pctDsOhGt3Uhhf_cQ00L_zf7T1M0MVVY&s=10.png" group-title="BANGLA",145.Bangla TV
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://cdn.ghuddi.live/Bangla_TV/Bangla_TV_BD/playlist.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUSwU91HGAYXxKlJ7u-YlATT8kJp_srlp4X6F5eVh6JQ&s=10.png",146.RTV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/rtv-sg.stream/playlist.m3u8

#EXTINF:-1 tvg-id="nexustv" tvg-name="Nexus TV" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDvCrlb7xmKGKrsrDbJSJ8hGTlvEidzrp29PJz60DT7KjVt4QzG2Yzd7I&s=10.png" group-title="BANGLA",147.Nexus TV
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://stream.ottplus.live/live/nexus_tv_abr/index.m3u8
#https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/nexustv.stream/playlist.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHLLTe_2ddfxYSoXDSD7D54Gbn57FJBuJ-6YV-PydK7_IjOZ-Pdj08iRdY&s=10.png" group-title="BANGLA",148.Green TV
https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/chunks.m3u8

#EXTINF:-1 group-title="BANGLA" tvg-logo="https://www.moumachi.com.bd//images/listings/45416/business/202412-gtv-logo.jpg",149.Gazi TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/gazibdz.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="duronto.bd" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwWX3mqbOFKb2kH1j8t-aLWjRJCTvuKH2Ie8NpbOFG3g&s=10.png" group-title="KIDS",160.Duronto Tv
http://103.165.93.31:8095/duranta/index.m3u8

#EXTINF:-1 tvg-id="Stable-Sports" tvg-logo="https://yt3.googleusercontent.com/M32uDDSlMkH2-XRmZMvcM64uMzotjxbpzngMS-pnmoDoD-ei--PAHiA0EC9tyiW-5lcXfa6Aqg=s900-c-k-c0x00ffffff-no-rj" group-title="KIDS",161.Nick Bangla
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
http://live.balajibroadband.com:3500/live/1341.m3u8
logohttps://jiotvimages.cdn.jio.com/dare_images/images/Nick_Bangla.png

#EXTINF:-1 tvg-id="1345" tvg-name="Sonic Bangla" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sonic_Bangla.png" tvg-language="Bengali" tvg-type="Kids" group-title="KIDS",162.Sonic Bangla
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
http://live.balajibroadband.com:3500/live/1345.m3u8

#EXTINF:-1 group-title="KIDS" tvg-logo="https://tstatic.akash-go.com/cms-ui/images/custom-content/1746005940155.png",163.SRK TV
https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/yBYRgLt/20240813-063955.png" group-title="KIDS",164.RONGEEN TV
https://server.thelegitpro.in/rongeentv/rongeentv/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://i.postimg.cc/8553wC1r/20260811-172504.png",170.Saudi Quran TV
http://m.live.net.sa:1935/live/quran/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://i.postimg.cc/rwkP3jVm/20260811-171415.png",171Saudi Sunnah TV
http://m.live.net.sa:1935/live/sunnah/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://saudiradio.faulio.com/storage/mediagallery/eb/42/fullhd_ef572438fffe8669b91c090d495bee55e7a4808c.png",172.Holy Quran Radio
https://live.kwikmotion.com/sbrksaquranradiolive/srpksaquranradio/playlist.m3u8

#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://i.postimg.cc/SsJHZNLp/20260811-125845.png",173.Al- Quran Live
https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/playlist.m3u8


#EXTINF:-1 group-title="ISLAMIC" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUe2QR6r4xB5LE3fSbB6jSPb9O0bhN9YzzM29ROOBhMP8-wwfBLK-3NE8&s=10.png",174.Madani TV Bangla
https://streaming.madanichannel.tv/static/streaming-playlists/hls/d3e49b76-ac06-4689-a641-9200445b647f/master.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5Q5sUvkWqFPoTRZl6pQoednylG3Pz92Tjaw&s.png",180.Enter 10 Bangla
https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_720p/chunks.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/xi6xX5UBv9knK3AH9aMk/posters/f4db1c12-b10f-46e8-a09b-e0efb8820970.png",181.Sony Aath
https://playyonogames.in/sliv/stream.m3u8?id=1000009255|Referer=https://playyonogames.in/

#EXTINF:-1 group-title="Indian Hindi" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/Ay52-JQBv9knK3AHFDWt/posters/00afb30b-3c19-4c4c-abd8-891db94e4767.webp",182.Sony Max HD
https://playyonogames.in/sliv/stream.m3u8?id=1000009247|Referer=https://playyonogames.in/

#EXTINF:-1 tvg-logo="https://i.postimg.cc/3wxxS1ss/20260812-102214.png" group-title="Indian Hindi",183.SONY MAX 2
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 16) ExoPlayerLib/2.14.1
https://sony.dongobd247.workers.dev/stream.m3u8?id=1000044878|referer=https://playyonogames.in/sliv/stream.m3u8?id=100044878


#EXTINF:-1 group-title="BANGLA" tvg-id="NAGORIK HD" tvg-logo="https://fcnchbd.xyz/iptv/logo/nago.png",199.NAGORIK HD
https://flussonic.defineatoz.com/backup/tracks-v1a1/mono.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://s3.aynaott.com/storage/dbc585f70a60b9855b6e13a8ce4cb6f4",200.T Sports ISP
http://103.185.24.134:3001/TSportsHD/index.m3u8
#http://172.17.50.112:84/ant1009/video.m3u8
#http://103.102.27.173:84/tvfeed1002/index.m3u8


#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",201.T Sports
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/LPL.m3u8
#http://172.17.50.112:84/ant1004/video.m3u8


#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",202.T Sports HD
http://103.185.24.134:3001/TSportsHD/index.m3u8
#http://172.17.50.112:84/ant1007/video.m3u8

#EXTINF:-1 tvg-id="tsportshd" tvg-name="T Sports" tvg-logo="https://ashtv.com.bd/assets/img/tsports.jpeg" group-title="SPORTS",203.T Sports FHD
http://103.185.24.134:3001/TSportsHD/index.m3u8
#https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-TSports1.m3u8

#EXTINF:-1 tvg-logo="https://i.postimg.cc/8C2gLZX9/SS-Fancode.png" group-title="SPORTS",Fancode 1
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=82dfca238e8c4b430a3269db71965db9:a00b28caf4ac628e77a553d440c0ddca
https://otte.cache.aiv-cdn.net/iad-nitro/live/clients/dash/enc/b3b3fkmrbl/out/v1/1084d5c9a97a4c5b9f9554c88f486646/cenc.mpd

#EXTINF:-1 tvg-logo="https://i.postimg.cc/8C2gLZX9/SS-Fancode.png" group-title="SPORTS",Fancode 2
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=1994b1df7dfd2e8a8d7b9bf3fb900285:22a1444b3da18e139191665b3d652835
https://otte.cache.aiv-cdn.net/iad-nitro/live/clients/dash/enc/avqlywnuzx/out/v1/aefca6420f944a9482e117f315de535f/cenc.mpd

#EXTINF:-1 tvg-logo="https://abusaeeidx.github.io/Tv-Channel-Logo/CricHD/runded/12-by-xfireflix.png" group-title="SPORTS",204.A Sports HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-ASports.m3u8
#http://fastshare1.com:8080//live/25711345/late8airline/43447.ts

#EXTINF:-1 tvg-logo="https://ev-img-cdn-lb.shoq.com.pk/prd-peg-data/default/images/logos/live/PTV-Sports.png" group-title="SPORTS",205.PTV Sports
#http://premiumtvs.space/live/YqXTywueEV/damp2purchase/89.ts
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-PTVSports.m3u8


#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/3N8gLCsG/images-(2).jpg",206.GEO SUPER HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-GeoSuper.m3u8
http://premiumtvs.space/live/YqXTywueEV/damp2purchase/101.ts


#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/T14Y66P2/20260710-111541.png",WILLOW CRICKET HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow1.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/dV8vWdGq/20260710-112953.png",WILLOW CRICKET 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Willow2.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/8kH3VHXZ/20260802-185517.png",WILLOW SPORTS HD
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=290e09c837da78d5cd961978d390515c:b748836c71e6a4ca68ef5b5652db6247
https://otte.live.fly.ww.aiv-cdn.net/pdx-nitro/live/clients/dash/enc/tll6uwepxa/out/v1/a7f67cbb33df46539312956427343886/cenc.mpd
#http://skylikem.com/live/2VZWJC3W/B7D7XK4T/1195167.ts

#EXTINF:-1 tvg-name="AU: Fox Sports 501" tvg-logo="https://i.postimg.cc/q72PSbWm/20260601-214906.png" group-title="SPORTS",Fox Sports 501
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/FOX501HD.m3u8

#EXTINF:-1 tvg-name="SKY SPORTS CRICKET" tvg-logo="https://i.postimg.cc/3Rz4bwGz/images-(1).jpg" group-title="SPORTS",SKY SPORTS CRICKET
https://bl.rutube.ru/livestream/7c13a51576b9ff2601f08f5d57dd5169/index.m3u8?s=uiXES2ePt7xTpQnbJxn7Dg&e=2074684474&scheme=https|user-agent=Mozilla
#://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SkySCric.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://images.seeklogo.com/logo-png/42/1/cricbuzz-logo-png_seeklogo-429413.png",CRICBUZZ HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Cricbuzz.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/NF489yZJ/STABLE-SPORTS1.png",CRICBUZZ 1 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Cricbuzz1.m3u8

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/tRhBGJvV/STABLE-SPORTS2.png",CRICBUZZ 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Cricbuzz2.m3u8

#EXTINF:-1 tvg-logo="https://akamaividz2.zee5.com/image/upload/w_720,h_405,c_scale,f_webp,q_auto:eco/resources/0-9-zeecafehd/list/1920x1080list60cd7fc8b57c4e1baf1cd4f603413540.jpg" group-title="SPORTS", Unite8 Sports 1 FHD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Unite8S1.m3u8

#EXTINF:-1 tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-20/images_9bd5db31bbc4d98defd1cb51a5606d9c_playmist_unite_sports_2.jpg" group-title="SPORTS", Unite8 Sports 2 FHD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-Unite8S2.m3u8



#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 1 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_1.png" group-title="SPORTS",SONY SPORTS 1 HD
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 16) ExoPlayerLib/2.14.1
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_1.m3u8
#http://stalker.hakunamata.workers.dev/play/1101/index.m3u8

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 2 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_2.png" group-title="SPORTS",SONY SPORTS 2 HD
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 16) ExoPlayerLib/2.14.1
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_2.m3u8
#https://b4uplay.com/sliv/stream.m3u8?id=1000009277|referer=https://b4uplay.com/

#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 3 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Ten_3.png" group-title="SPORTS",SONY SPORTS 3 HD
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 16) ExoPlayerLib/2.14.1
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_3.m3u8


#EXTINF:-1 tvg-id="ext" tvg-name="SONY SPORTS 5 HD" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Sony_Six_SD.png" group-title="SPORTS",SONY SPORTS 5 HD
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 16) ExoPlayerLib/2.14.1
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-SonyTen_5.m3u8
#http://live.balajibroadband.com:3500/live/155.m3u8


#EXTINF: -1 tvg-logo="https://tatalogo.pages.dev/78.png" group-title="SPORTS", Star Sports 1 HD
#http://skylikem.com/live/2VZWJC3W/B7D7XK4T/778413.ts
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSports1.m3u8
#http://114.130.57.233:8080/StarSports1/tracks-v1a1/mono.m3u8?token=SkQuhAXZxgBan1

#EXTINF: -1 tvg-id="235" tvg-logo="https://tatalogo.pages.dev/235.png" group-title="SPORTS", Star Sports 2 HD
#http://skylikem.com/live/2VZWJC3W/B7D7XK4T/778412.ts
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSports2.m3u8
#http://103.151.60.204:881/StarSports2/tracks-v1a1/mono.m3u8?token=Cv90Fr-lyiZYh2


#EXTINF: -1 tvg-id="235" tvg-logo="https://tatalogo.pages.dev/235.png" group-title="SPORTS", Star Sports 3 HD
http://line.umetop.pro:80/play/live.php?mac=00:1A:79:8F:BA:8A&stream=1104675&extension=m3u8
#http://skylikem.com/live/2VZWJC3W/B7D7XK4T/132081.ts

#EXTINF:-1 tvg-id="StarSportsSelectHD1.in" tvg-name="STAR SPORTS SELECT 1 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-1-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 1 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSS_1.m3u8
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276734.ts

#EXTINF:-1 tvg-id="StarSportsSelectHD2.in" tvg-name="STAR SPORTS SELECT 2 HD" tvg-logo="https://raw.githubusercontent.com/AsimDipto/Logo-box/refs/heads/main/India/star-sports-select-2-hd-in.png" group-title="SPORTS",STAR SPORTS SELECT 2 HD
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/IPTV/SS-StarSS_2.m3u8
#http://tvportal4k.xyz:80/live/Rachideddib26/d41g5hkc1b/276735.ts

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/Dw8YJJ39/stablesportstv-tnt1.png",TNT SPORTS 1
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=69a5aa835a061ce64a630d1046727e40:d02feac8a999bd06bf4059bf33411749
https://otte.cache.aiv-cdn.net/bom-nitro/live/clients/dash/enc/rhf2dwosdt/out/v1/ee550d2a68d846c797e6ce4de2e8b76d/cenc.mpd

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/26pJfzMN/stablesportstv-tnt2.png",TNT SPORTS 2
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=f3df7843080ae743bf865dc5fdf64c68:567c863bc12eb74788ea74888c042e1b
https://otte.cache.aiv-cdn.net/bom-nitro/live/clients/dash/enc/puehlftk5j/out/v1/f7f0da1ee112481ca0024e6d4dd97f4a/cenc.mpd

#EXTINF:-1 group-title="SPORTS" tvg-logo="https://i.postimg.cc/SQc4RPfP/stablesportstv-tnt3.png",TNT SPORTS 3
#KODIPROP:inputstream=inputstream.adaptive
#KODIPROP:inputstream.adaptive.manifest_type=mpd
#KODIPROP:inputstream.adaptive.license_type=clearkey
#KODIPROP:inputstream.adaptive.license_key=cc91508324ce9dcaf425a43d58f1d9d4:643e5474d9edd87c7d9091c8c97994ca
https://otte.cache.aiv-cdn.net/bom-nitro/live/clients/dash/enc/dev1hjwzh9/out/v1/a5f0ee7ad7b24906b14f43bebbbe4678/cenc.mpd

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYYLijjughYF51FVjWeUtGKFckDYqm8B1elAgERP4HIDMf8KpDYC7LpZ4&s=10" group-title="MUSIC", Sangeet Bangla
https://cdn-4.pishow.tv/live/1143/master.m3u8

#EXTINF:-1 tvg-id="zoom" tvg-name="zoom" tvg-logo="http://dugdugilive.com/img/channels/zoom.png" group-title="MUSIC",ZOOM
http://live.balajibroadband.com:3500/live/592.m3u8

#EXTINF:-1 group-title="MUSIC" tvg-logo="https://i.postimg.cc/RZJmcSt6/9XM.jpg",9X Music
http://live.balajibroadband.com:3500/live/587.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co.com/9qc3x8F/images-1.jpg" group-title="MUSIC",Music India
#https://cdn-2.pishow.tv/live/226/master.m3u8
http://live.balajibroadband.com:3500/live/250.m3u8
#http://103.180.212.191:3500/live/250.m3u8 

#EXTINF:-1 tvg-id="3428" tvg-name="Discovery HD Bengali" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/DiscoveryHDBen.png" tvg-language="Bengali" group-title="Infotainment", Discovery HD Bengali
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/DiscoveryBD.m3u8

#EXTINF:-1 tvg-id="573" tvg-name="Discovery Bengali" tvg-logo="https://jiotvimages.cdn.jio.com/dare_images/images/Discovery_Channel_Bengali.png" tvg-language="Bengali" group-title="Infotainment", Discovery Bangla
#EXTVLCOPT:http-user-agent=oxoo/1.3.9.d (Linux;Android 7.1.2) ExoPlayerLib/2.14.1
https://raw.githubusercontent.com/stablesports711-hue/stable-sports-movie/refs/heads/main/BANGLA/DiscoveryBD.m3u8

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_OahSFGXf5G7iN2KaGuhe3j_8GerDS1MqEjCwiMi8bA&s=10.png" group-title="FM",বাংলাদেশ বেতার (100.0FM)
https://as1.digitalsynapsebd.com/proxy/bbdkka/stream

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMPNmDKEUnR3BgOJobIx436QI_Uw-N_YvBXrqL-QsCL26g1py-pQhFi1rG&s=10.png" group-title="FM",জাগো এফএম (94.4FM)
http://139.59.86.99:12496/stream

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://images.tuneyou.com/images/logos/500_500/95/12695/RadioBhumi92.8FM.png" group-title="FM",রেডিও ভূমি (92.8FM)
https://stream.zeno.fm/ybf1umk1k18uv

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://yt3.googleusercontent.com/7N6iIzlaBnxxtZ7lRyKHSUPLlp8QPmNjBdeyuDG4PaL-KsbIQOxxPuA-RrSVZvV7fyYJ_DgF=s900-c-k-c0x00ffffff-no-rj" group-title="FM",ঢাকা এফএম (90.4FM)
https://stream.zeno.fm/u9mphfk604zuv

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://cdn-profiles.tunein.com/s122537/images/logog.png" group-title="FM",রেডিও ফুর্তি (88.0FM)
https://radiofoorti.fm/api/stream

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://www.codagecorp.com/wp-content/uploads/radio-today.png" group-title="FM",রেডিও টুডে (89.6FM)
https://stream.zeno.fm/8wv4d8g4344tv

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzlD0ZKI2jNSOkQqPA-mswY1AXvEuUEsTmrmMjv98rZ0TVEU2D-CFHaIz2&s=10.png" group-title="FM",পিপলস রেডিও (91.6FM)
https://s3.myradiostream.com:14498/;

#EXTINF:-1 tvg-id="STABLE-SPORTS" tvg-logo="https://spicefmbd.com/logospice.png" group-title="FM",স্পাইসি এফএম (96.4FM)
https://stream.spicefmbd.com/stream.m3u8

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/DzBr7HcM/1773936983038.png",STABLE-SPORTS TV
https://res.cloudinary.com/qleik3si/video/upload/v1785235285/VN20260728_161756_ev6pow.mp4

#EXTINF:-1 group-title="PROMO" tvg-logo="https://i.postimg.cc/141tq9B1/dc092590a65fc2ac5bd58ccf59cecb51-fgraphic.png",Toffee {premium}
https://res.cloudinary.com/qleik3si/video/upload/v1785235285/VN20260728_161756_ev6pow.mp4

XTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.ibb.co.com/9m9SqPMy/images-2.jpg",Prince [2026]
ttps://yellow-flower-41fc.cinepixserver00.workers.dev/1:/22-5-26/ottboxbd.COM%20-%20Prince%20Once%20Upon%20a%20Time%20in%20Dhaka%202026%20Bengali%20ORG%201080p%20WEB-DL%20x264.mkv

#XTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.postimg.cc/DfqzmXQ6/Domm-stablesportstv.jpg",Domm [2026]
ttps://yellow-flower-41fc.cinepixserver00.workers.dev/1:/21-5-26/Domm%202026%20Bengali%20(ORG)%201080p%20WEB-DL%20x264%20ESubs.mkv

EXTINF:-1 group-title="MOVIE 2026" tvg-logo="https://i.postimg.cc/ryBMGFjw/Rakkhosh-stablesportstv.jpg",Rakkhosh [2026]
ttp://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/RAKKHOSH%20Bangla%20Movie%20SIAM/Rakkhosh%20(2026)%20Bengali%20720p%20HD-Camrip.mp4

EXTINF:-1 group-title="MOVIE 2026" tvg-logo="http://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/Bonolota%20Express%20(2026)/MV5BZmY0M2I1NjYtODU4Zi00MmIyLTk0OWUtMDlhN2JmNzFmOWI1XkEyXkFqcGc@._V1_SX300.jpg",Bonolota Express [2026]
ttp://103.203.93.4/Dhallywood%20(Bangladeshi)/2026/Bonolota%20Express%20(2026)/Bonolota%20Express%20(2026)%20Bengali%20Amazon%20WEB-DL%20H264%20AAC%20720p.mkv

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
