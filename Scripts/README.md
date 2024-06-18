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
   ```
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


# Filter Short Comments

This Python script filters comments from a text file based on their length, specifically targeting comments shorter than 5 characters. It saves the filtered comments to another file.

## How It Works

The script performs the following steps:

1. **Open the File:** Reads the contents of a specified text file containing comments.

2. **Filter Comments by Length:** Filters out comments that are shorter than 5 characters. Additional filtering criteria are applied based on the length and the Unicode value of the first character of each comment.

3. **Save Filtered Comments:** Saves the comments that pass the filter to a new file.


# Filter Extra Comments

This script filters comments based on specific criteria related to the ASCII values of the characters. It reads comments from a file, applies the filtering logic, and then writes the filtered comments to a new file.

1. **Function Definition**:

   - `filtrar_comments(comentarios)`: This function processes a list of comments, filtering out those that meet certain criteria based on the ASCII values of their characters.

2. **Reading the Input File**:

   - The script reads comments from `CommentsTXT/filtered_Short_comments.txt` and counts the number of comments.

3. **Applying the Filter**:

   - The comments are processed using the `filtrar_comments` function.

4. **Writing the Output File**:
   - The filtered comments are written to a new file `CommentsTXT/filtered_Extra_comments.txt`.

## Filtering Criteria

The filtering function `filtrar_comments` applies the following rules to filter out comments:

1. **Unicode Value >= 800**:
    - If the first character of the comment has a Unicode value of 800 or higher, the comment is filtered out.

2. **Whitespace Characters**:
    - If the first character is a space (`32`), newline (`10`), or period (`46`), the comment is filtered out.

3. **Extended ASCII Range**:
    - If the first character's ASCII value is between 128 and 255, the comment is filtered out.

4. **Other Characters**:
    - Comments that do not meet any of the above criteria are kept.

## Output

- The script outputs the total number of comments after the initial filter, the total number of comments that passed the filter, and the total number of comments that were eliminated.
- The filtered comments are saved to `CommentsTXT/filtered_Extra_comments.txt`.

