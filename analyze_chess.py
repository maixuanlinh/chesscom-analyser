import requests
import json

# Fetch list of archives for the user
def fetch_archives(username):
    archive_url = f"https://api.chess.com/pub/player/{username}/games/archives"
    # This header is needed to avoid 403 Forbidden error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(archive_url, headers=headers)
    response.raise_for_status()
    return response.json().get('archives', [])

# Fetch games from a specific archive
def fetch_games_from_archive(archive_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(archive_url, headers=headers)
    response.raise_for_status()
    return response.json().get('games', [])

# Process and store IDs of games with high accuracy
def process_games(games, username, links):
    for game in games:
        accuracies = game.get('accuracies', None)
        if accuracies:
            white_player = game['white']['username']
            black_player = game['black']['username']
            if white_player.lower() == username.lower():
                user_accuracy = accuracies.get('white', 0)
            elif black_player.lower() == username.lower():
                user_accuracy = accuracies.get('black', 0)
            else:
                continue  # Skip if the current user is neither white nor black

            if user_accuracy > 85:
                game_url = game['url']
                game_id = game_url.split('/')[-1]
                review_link = f"https://www.chess.com/analysis/game/live/{game_id}/?tab=review"
                links.append(f"{len(links) + 1}. {review_link}")

# Main function to fetch all games for the user and process them
def fetch_all_games(username):
    try:
        archives = fetch_archives(username)
        print(f"Found {len(archives)} archives for {username}")
        
        links = []
        for archive_url in archives:
            games = fetch_games_from_archive(archive_url)
            print(f"Fetched {len(games)} games from {archive_url}")
            process_games(games, username, links)

        # Write links to a text file
        with open('high_accuracy_games.txt', 'w') as file:
            file.write("\n".join(links))
        print(f"Stored {len(links)} high accuracy game links to high_accuracy_games.txt")

    except Exception as e:
        print(f"Error fetching games: {e}")

if __name__ == "__main__":
    username = "chessprince_tiger"  # This is my chess username, replace with yours :D 
    fetch_all_games(username)
