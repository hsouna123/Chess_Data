import requests
import json
import csv

username = input("Enter your Chess.com username: ")
url = f"https://api.chess.com/pub/player/{username}/stats"

response = requests.get(url)
data = json.loads(response.text)

if 'chess_blitz' in data:
    blitz_data = data['chess_blitz']
    record = blitz_data.get('record')
    if record and 'games' in record:
        blitz_games = record['games']
        if len(blitz_games) > 0:
            with open(f"{username}_blitz_games.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=blitz_games[0].keys())
                writer.writeheader()
                for game in blitz_games:
                    writer.writerow(game)
                    print(game)
    else:
        print("No blitz games found.")
else:
    print("Blitz data not found.")

print(blitz_data)
print(record)
