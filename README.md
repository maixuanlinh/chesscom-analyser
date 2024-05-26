# Chess.com Game Bulk Analyzer

This project fetches and analyzes chess games from Chess.com using their public API. It identifies games where the specified user has an accuracy above 85% and stores links to those games in a text file.

## Current Features

- Fetches all available games for a specified user from Chess.com
- Filters games where the user's accuracy is above 85%
- Stores the links to high-accuracy games in a text file

## Requirements

- Python 3.x
- `requests` library
- `stockfish` library (if using Stockfish for additional analysis)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/maixuanlinh/chesscom-analyser.git
    cd chesscom-analyzer
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install requests stockfish
    ```

4. Install Stockfish (if not already installed):
    ```bash
    brew install stockfish  # For macOS
    ```

## Configuration

1. Set the path to the Stockfish binary in your script:
    ```python
    stockfish_path = "/path/to/stockfish"  
    ```

## Usage

1. Ensure your virtual environment is activated:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Run the script:
    ```bash
    python analyze_chess.py
    ```

## Script Overview

The script consists of several main functions:

- `fetch_archives(username)`: Fetches the list of game archives for the specified user.
- `fetch_games_from_archive(archive_url)`: Fetches games from a specific archive URL.
- `process_games(games, username, links)`: Processes and filters games with high accuracy for the specified user.
- `fetch_all_games(username)`: Main function that fetches and processes all games for the specified user.

### Example Output

The script will create a file `high_accuracy_games.txt` with links to the high-accuracy games, formatted as:

https://www.chess.com/analysis/game/live/1234567890/?tab=review
https://www.chess.com/analysis/game/live/0987654321/?tab=review


## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
