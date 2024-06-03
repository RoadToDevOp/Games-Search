import requests
import json 


url = "https://rawg-video-games-database.p.rapidapi.com/games?key=ffbe944544e84b7bba0c133b3ac90b0f"

headers = {
	"X-RapidAPI-Key": "1220e8bca4msh0ae96f8e29fe247p1cc760jsn74cf7b671963",
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.text)
