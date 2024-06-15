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
2. **Modify the File Path**: Update the `file_path` variable to specify the directory where you want to save the reviews.
3. **Run the Script**: Execute the script to download and save the reviews.


# Filter Braille Comments

This Python script filters out Braille comments from a text file and saves the filtered comments to another file. The script is designed to handle Braille symbols in the comments and removes lines that contain specific Braille symbols.

## How It Works

The script follows these steps to filter Braille comments:

1. **Open File:** It opens the specified text file that contains comments, including Braille symbols.

2. **Filter Comments:** Using a filtering function, it separates comments that contain Braille symbols from those that don't. The filtering is based on a specific keyword or Braille symbol.

3. **Save Filtered Comments:** The comments that pass the filter (i.e., those without Braille symbols) are saved to a new file, while the comments containing Braille symbols are excluded.

## Usage

1. Clone this repository to your local machine.

2. Ensure you have Python installed on your system.

3. Run the `filtrar_comentarios.py` script, providing the path to the text file containing the comments.

    ```bash
    python filtrar_comentarios.py
    ```

    Make sure to set the `file_path` variable in the script to the correct path of your input file.

4. The script will filter out Braille comments and save the filtered comments to a file named `filtered_Braille_comments.txt` in the same directory as the input file.

## Dependencies

The script uses the `os` module to handle file paths.
