import requests

# Set up the API URL and parameters
url = "https://lichess.org/api/games/user/Hsouna1"
params = {"max": 10} # limit to 10 games for demonstration purposes
headers = {"Authorization": "Bearer lip_vHJA4TlqZMNTOtTT7J12"}

# Make the API request
response = requests.get(url, params=params, headers=headers)

# Check that the request was successful
if response.status_code != 200:
    raise Exception(f"Request failed with status {response.status_code} - {response.text}")

# Extract the game data from the response
games = response.json()

# Display the game data
for game in games:
    print(f"{game['rated']}: {game['winner']} vs {game['loser']}")
