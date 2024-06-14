# Steam Reviews Downloader

This script downloads reviews for a specific game from Steam and saves them to a text file.

## How It Works

1. **Set Up Parameters**: The script sets up the game ID (`app_id`) and request parameters (`request_params`) to specify the language, review type, purchase type, and day range for the reviews.

2. **Download Reviews**: It uses the `steamreviews` library to fetch the reviews for the specified game based on the parameters.

3. **Save Reviews to File**: The script writes the reviews to a text file located at a specified directory path. Each review is written on a new line.

## Usage

1. **Install `steamreviews`**: Make sure you have the `steamreviews` library installed. You can install it using pip:
   ```bash
   pip install steamreviews
