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

This Python script filters comments from a text file based on the presence of Braille symbols and saves the filtered comments to another file.

## How It Works

The script performs the following steps:

1. **Open the File:** Reads the contents of a specified text file containing comments.

2. **Filter Comments:** Filters out comments that contain a specified Braille symbol.

3. **Save Filtered Comments:** Saves the comments that do not contain the Braille symbol to a new file.
This Python script filters out Braille comments from a text file and saves the filtered comments to another file. The script is designed to handle Braille symbols in the comments and removes lines that contain specific Braille symbols.

## How It Works

The script follows these steps to filter Braille comments:

1. **Open File:** It opens the specified text file that contains comments, including Braille symbols.

2. **Filter Comments:** Using a filtering function, it separates comments that contain Braille symbols from those that don't. The filtering is based on a specific keyword or Braille symbol.

3. **Save Filtered Comments:** The comments that pass the filter (i.e., those without Braille symbols) are saved to a new file, while the comments containing Braille symbols are excluded.

## Usage

1. **Clone this repository** to your local machine.

2. **Ensure you have Python installed** on your system.

3. **Place your input text file** containing comments in the specified path.
2. Ensure you have Python installed on your system.

4. **Run the script `filtrar_comentarios.py`:**
3. Run the `filtrar_comentarios.py` script, providing the path to the text file containing the comments.

    ```bash
    python filtrar_comentarios.py
    ```

5. **Set the `file_path` variable** in the script to the correct path of your input file.
    Make sure to set the `file_path` variable in the script to the correct path of your input file.

6. **The script will filter out Braille comments** and save the filtered comments to a file named `filtered_Braille_comments.txt` in the same directory as the input file.



# Filter Short Comments

This Python script filters comments from a text file based on their length, specifically targeting comments shorter than 5 characters. It saves the filtered comments to another file.

## How It Works

The script performs the following steps:

1. **Open the File:** Reads the contents of a specified text file containing comments.

2. **Filter Comments by Length:** Filters out comments that are shorter than 5 characters. Additional filtering criteria are applied based on the length and the Unicode value of the first character of each comment.

3. **Save Filtered Comments:** Saves the comments that pass the filter to a new file.

## Usage

1. **Clone this repository** to your local machine.

2. **Ensure you have Python installed** on your system.

3. **Place your input text file** containing comments in the specified path.

4. **Run the script `filtrar_comentarios.py`:**

    ```bash
    python filtrar_comentarios.py
    ```

5. **Set the `file_path` variable** in the script to the correct path of your input file.

6. **The script will filter out short comments** and save the filtered comments to a file named `filtered_Short_comments.txt` in the same directory as the input file.
4. The script will filter out Braille comments and save the filtered comments to a file named `filtered_Braille_comments.txt` in the same directory as the input file.

## Dependencies

The script uses the `os` module to handle file paths.
