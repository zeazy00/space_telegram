# Скачивание и отправка фото в telegram

Скачивание картинок раз в сутки с сайтов NASA и SpeceX и отправка фото в telegram

### Как установить

Для работы кода необходимо создать файл .env и поместить туда ключ API NASA, ключ API TELEGRAM, и чат ID TELEGRAM.
```
NASA_API_KEY=bfSjLfaaGlBDOjzUgGUdFgbTCXvNa4bOehyGTfkl
TELEGRAM_TOKEN=2121456781:AAH7f5-Emgli7FfN5Ls-78kKKxua70xMLvo
CHAT_ID=@soxvezdie
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### Пример работы

```
(env) C:\Users\Zeazy\Desktop\python\devman\space_telegram>python space_telegram.py
no spasex links
1) nasa_photos 2) Messier 2.jpg 3) https://apod.nasa.gov/apod/image/1904/potw1913aa.jpg
1) nasa_photos 2) Strawberry Moon over the Temple of Poseidon.jpg 3) https://apod.nasa.gov/apod/image/1906/StrawberryMoon_Chasiotis_2000.jpg
1) nasa_photos 2) The Galactic Center Across the Infrared.jpg 3) https://apod.nasa.gov/apod/image/0007/gcatlas_2mass_big.jpg
1) nasa_photos 2016-02-09 error
1) nasa_photos 2) NGC 604 Giant Stellar Nursery.jpg 3) https://apod.nasa.gov/apod/image/0211/ngc604_hst_full.jpg
1) nasa_photos 2) A Blue Bridge of Stars between Cluster Galaxies.jpg 3) https://apod.nasa.gov/apod/image/1407/clusterlens_hubble_1280.jpg
1) nasa_photos 2) N11B Star Cloud of the LMC.jpg 3) https://apod.nasa.gov/apod/image/0407/n11_hst_big.jpg
1) nasa_photos 2) Arp 272.jpg 3) https://apod.nasa.gov/apod/image/1109/arp272HLA_pugh.jpg
1) nasa_photos 2) Noctilucent Clouds, Reflections, and Silhouettes.jpg 3) https://apod.nasa.gov/apod/image/1906/NoctilucentNetherlands_Simmering_5766.jpg
1) nasa_photos 2) Anticrepuscular Rays Converge Opposite the Sun.jpg 3) https://apod.nasa.gov/apod/image/1906/AnticrepuscularRays_Patekar_5600.jpg
1) nasa_photos 2) Night on a Spooky Planet.jpg 3) https://apod.nasa.gov/apod/image/1310/hverirVetter1300.jpg
1) nasa_photos 2) Gemini's Meteors.jpg 3) https://apod.nasa.gov/apod/image/2012/GeminidMeteorsStePelle.jpg
1) nasa_photos 2) Meteor Storm Sights and Sounds.gif 3) https://apod.nasa.gov/apod/image/0111/leonidfire_raymundo.gif
1) nasa_photos 2) Biking to the Moon.jpg 3) https://apod.nasa.gov/apod/image/2010/IMG_7493Colour.jpg
1) nasa_photos 2) Phobos from Mars Express.jpg 3) https://apod.nasa.gov/apod/image/1003/phobos1_marsexpress_big.jpg
1) nasa_photos 2) In the Center of the Trifid Nebula.jpg 3) https://apod.nasa.gov/apod/image/2011/Trifid_HubbleGendler_2400.jpg
1) nasa_photos 2) Arcs and Jets in Herbig Haro 34.jpg 3) https://apod.nasa.gov/apod/image/9911/hh34_vlt_big.jpg
1) nasa_photos 2) NGC 4631 The Whale Galaxy.jpg 3) https://apod.nasa.gov/apod/image/0401/n4631zeiders_big.jpg
1) nasa_photos 2012-03-20 error
1) nasa_photos 2) NGC 1360 The Robin's Egg Nebula.jpg 3) https://apod.nasa.gov/apod/image/1805/NGC1360-Final5D-Cc2.jpg
1) nasa_photos 2) The Frothy Milky Way.jpg 3) https://apod.nasa.gov/apod/image/9704/iras_waller1_big.jpg
1) nasa_photos 2) The Orion Nebula in Hydrogen.jpg 3) https://apod.nasa.gov/apod/image/0011/m42hargb_gendler_big.jpg
1) nasa_photos 2) New Moons For Saturn.jpg 3) https://apod.nasa.gov/apod/image/0011/saturnnewmoon_eso_big.jpg
1) nasa_photos 2) The Southern Cliff in the Lagoon.jpg 3) https://apod.nasa.gov/apod/image/2105/M8_rim2geminicrop1024.jpg
1) nasa_photos 2) LMC X-1 A Black Hole Candidate.gif 3) https://apod.nasa.gov/apod/image/lmcX1_rosat_big.gif
1) nasa_photos 2020-03-15 error
1) nasa_photos 2) Martian Dunes and the Shadow of Opportunity.jpg 3) https://apod.nasa.gov/apod/image/0903/windmars_opportunity_big.jpg
1) nasa_photos 2) M78 Stardust and Starlight.jpg 3) https://apod.nasa.gov/apod/image/1310/M78_hallas.jpg
1) nasa_photos 2) Valles Marineris from Mars Express.jpg 3) https://apod.nasa.gov/apod/image/0401/marscolormap_marsexpress_full.jpg
1) nasa_photos 2) SN 1006 Supernova Remnant.jpg 3) https://apod.nasa.gov/apod/image/1407/sn1006c.jpg
1) epic_photos 2) epic_1b_20220127000831.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127000831.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 00:03:42
1) epic_photos 2) epic_1b_20220127015633.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127015633.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 01:51:44
1) epic_photos 2) epic_1b_20220127034435.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127034435.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 03:39:47
1) epic_photos 2) epic_1b_20220127053238.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127053238.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 05:27:49
1) epic_photos 2) epic_1b_20220127072040.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127072040.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 07:15:51
1) epic_photos 2) epic_1b_20220127090842.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127090842.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 09:03:53
1) epic_photos 2) epic_1b_20220127105644.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127105644.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 10:51:56
1) epic_photos 2) epic_1b_20220127124446.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127124446.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 12:39:58
1) epic_photos 2) epic_1b_20220127143248.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127143248.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 14:28:00
1) epic_photos 2) epic_1b_20220127162051.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127162051.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 16:16:02
1) epic_photos 2) epic_1b_20220127180853.png 3) https://api.nasa.gov/EPIC/archive/natural/2022/01/27/png/epic_1b_20220127180853.png?api_key=bfSjLfaaGlbDOyzUgGUdFgbTCXvNa4bOehyGTfkl
 2022-01-27 18:04:04
{'id': 2121456781, 'username': 'kdcsozvezdie_bot', 'first_name': '\u200eКГБОУ КДЦ "Созвездие"'}
```