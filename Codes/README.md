Steam Reviews Downloader
This script downloads reviews for a specific game from Steam and saves them to a text file.

How It Works
Set Up Parameters: The script sets up the game ID (app_id) and request parameters (request_params) to specify the language, review type, purchase type, and day range for the reviews.

Download Reviews: It uses the steamreviews library to fetch the reviews for the specified game based on the parameters.

Save Reviews to File: The script writes the reviews to a text file located at a specified directory path. Each review is written on a new line.
