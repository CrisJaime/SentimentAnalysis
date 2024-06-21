# CommentFilter Class

The `CommentFilter` class is designed to filter comments from a text file based on specific criteria. Below is an explanation of how the class works and its main functionalities.

## Usage

1. **Initialize the CommentFilter Object**:

   - Create an instance of the `CommentFilter` class by providing the path to the input file and the output directory where filtered comments will be saved.

2. **Process Comments**:

   - Use the `process_comments` method to filter comments based on multiple criteria sequentially. The method takes four parameters:
     - `word`: The word used as a filter criterion for the initial filter.
     - `first_output_filename`: The filename to save the comments after the first filter.
     - `second_output_filename`: The filename to save the comments after the second filter.
     - `third_output_filename`: The filename to save the comments after the third filter.

3. **Filtered Comments**:
   - After processing, the class provides information about the number of comments passed and eliminated at each filtering stage. It also saves the filtered comments to the specified output files.
