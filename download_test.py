from core.download import Download

url = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/Game_of_Thrones_title_card.jpg/250px-Game_of_Thrones_title_card.jpg'
download = Download(url)
download.start_downloading()
print(download)