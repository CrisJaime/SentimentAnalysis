Steam Reviews Downloader
This script downloads reviews for a specific game from Steam and saves them to a text file.

How It Works
Set Up Parameters: The script sets up the game ID (app_id) and request parameters (request_params) to specify the language, review type, purchase type, and day range for the reviews.

Download Reviews: It uses the steamreviews library to fetch the reviews for the specified game based on the parameters.

Save Reviews to File: The script writes the reviews to a text file located at a specified directory path. Each review is written on a new line.

Usage
Install steamreviews: Make sure you have the steamreviews library installed. You can install it using pip:

bash
Copiar código
pip install steamreviews
Modify the File Path: Update the file_path variable to specify the directory where you want to save the reviews.

Run the Script: Execute the script to download and save the reviews.
