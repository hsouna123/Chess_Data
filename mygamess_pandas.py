import pandas as pd

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('Hsouna1_Lichess_GAMES.csv')

# Filter for games where Hsouna1 was a player
player_filter = (df['White'] == 'Hsouna1') | (df['Black'] == 'Hsouna1')
player_games = df[player_filter]

# Calculate number of games played, wins, and draws
num_games = player_games.shape[0]
num_wins = player_games[player_games['Result'] == '1-0'].shape[0] + player_games[player_games['Result'] == '0-1*'].shape[0]
num_draws = player_games[player_games['Result'] == '1/2-1/2'].shape[0]

# Calculate win percentage (rounded to 2 decimal places)
win_percentage = round((num_wins / num_games) * 100, 2)

# Print the results
print(f"Hsouna1 has played {num_games} games, winning {num_wins}, drawing {num_draws}, and losing {num_games - num_wins - num_draws}.")
print(f"Hsouna1's win percentage is {win_percentage}%.")
