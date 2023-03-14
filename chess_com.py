import requests
import json
import csv

# Set up API endpoint and headers
username = "Hsouna1"
games_endpoint = f"https://api.chess.com/pub/player/{username}/games"
stats_endpoint = f"https://api.chess.com/pub/player/{username}/stats"
headers = {
    "Accept": "application/json"
}

# Make API request for games
response = requests.get(games_endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Retrieve the game data from the response
    game_data = response.json()

    # Filter blitz games
    blitz_games = [game for game in game_data["games"] if game["time_class"] == "blitz"]
    
    # Make API request for stats
    response = requests.get(stats_endpoint, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve the stats data from the response
        stats_data = response.json()
        
        # Retrieve blitz game stats
        blitz_stats = stats_data.get("chess_blitz", {})
        
        # Retrieve blitz game record
        blitz_record = blitz_stats.get("record", {})
        
        # Retrieve blitz game best
        blitz_best = blitz_stats.get("best", {})
        
        # Retrieve blitz game last
        blitz_last = blitz_stats.get("last", {})
        
        # Create CSV file
        with open("blitz_games.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=blitz_games[0].keys())
            writer.writeheader()
            for game in blitz_games:
                writer.writerow(game)
        
        # Print some stats
        print("Blitz Game Record:")
        print("Wins:", blitz_record.get("win"))
        print("Losses:", blitz_record.get("loss"))
        print("Draws:", blitz_record.get("draw"))
        print("Timeout percentage in last 90 days:", blitz_record.get("timeout_percent"))
        print()
        
        print("Blitz Game Best:")
        print("Date:", blitz_best.get("date"))
        print("Rating:", blitz_best.get("rating"))
        print("Game URL:", blitz_best.get("game"))
        print()
        
        print("Blitz Game Last:")
        print("Date:", blitz_last.get("date"))
        print("Rating:", blitz_last.get("rating"))
        print("RD:", blitz_last.get("rd"))
        print()
    else:
        print("Error retrieving stats. Status code:", response.status_code)
else:
    print("Error retrieving game history. Status code:", response.status_code)
