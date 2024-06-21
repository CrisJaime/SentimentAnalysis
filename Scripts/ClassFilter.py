import os


class CommentFilter:
    def __init__(self, input_file, output_directory):
        self.input_file = input_file
        self.output_directory = output_directory
        self.comments = self.read_comments()

    def read_comments(self):
        """Read comments from the input file."""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            return f.readlines()

    def filter_comments(self, word):
        """Filter comments that contain a specific word."""
        filtered = []
        removed = []
        for line in self.comments:
            if word in line:
                removed.append(line)
            else:
                filtered.append(line)
        return filtered, removed

    def filter_comments_by_length_and_characters(self, comments):
        """Filter comments based on length and specific character conditions."""
        filtered = []
        removed = []
        for comment in comments:
            size = len(comment)
            if size < 5:
                if len(comment) != 0 and len(comment) <= 2:
                    removed.append(comment)
                elif len(comment) > 2 and ord(comment[0]) < 63:
                    removed.append(comment)
                elif len(comment) > 2 and ord(comment[0]) > 63:
                    if (ord(comment[0]) > 63 and ord(comment[0]) <= 90) or (ord(comment[0]) > 95 and ord(comment[0]) <= 122):
                        filtered.append(comment)
                    else:
                        removed.append(comment)
            else:
                filtered.append(comment)
        return filtered, removed

    def filter_comments_by_unicode(self, comments):
        """Filter comments based on Unicode values and specific characters."""
        filtered = []
        removed = []
        for line in comments:
            if len(line) > 0:
                x = line[0]
                if ord(x) >= 800:
                    removed.append(line)
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 46:
                    removed.append(line)
                elif ord(x) >= 128 and ord(x) <= 255:
                    removed.append(line)
                else:
                    filtered.append(line)
        return filtered, removed

    def save_filtered_comments(self, filtered_comments, output_filename):
        """Save filtered comments to a specified output file."""
        output_file_path = os.path.join(self.output_directory, output_filename)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(filtered_comments)
        print("[INFO] Filtered comments saved to:", output_file_path)

    def process_comments(self, word, first_output_filename, second_output_filename, third_output_filename):
        """Process comments through multiple filters and save the results."""
        print("===" * 10)
        print("[INFO] Number of comments:", len(self.comments))
        print("===" * 10)

        # First filter
        filtered_comments, removed_comments = self.filter_comments(word)
        print("[INFO] Total number of comments that passed the first filter:", len(
            filtered_comments))
        print("[INFO] Total number of comments eliminated in the first filter:", len(
            removed_comments))
        print("===" * 10)
        self.save_filtered_comments(filtered_comments, first_output_filename)

        # Second filter
        filtered_comments, removed_comments = self.filter_comments_by_length_and_characters(
            filtered_comments)
        print("[INFO] Total number of comments that passed the second filter:", len(
            filtered_comments))
        print("[INFO] Total number of comments eliminated in the second filter:", len(
            removed_comments))
        print("===" * 10)
        self.save_filtered_comments(filtered_comments, second_output_filename)

        # Third filter
        filtered_comments, removed_comments = self.filter_comments_by_unicode(
            filtered_comments)
        print("[INFO] Total number of comments that passed the third filter:", len(
            filtered_comments))
        print("[INFO] Total number of comments eliminated in the third filter:", len(
            removed_comments))
        print("===" * 10)
        self.save_filtered_comments(filtered_comments, third_output_filename)

        # Print remaining comments after filtering
        print("[INFO] Remaining comments after filtering:",
              len(filtered_comments))


# Example usage
input_file = 'CommentsTXT/comentarios_juego_1245620.txt'
output_directory = 'CommentsTXT/'
first_output_filename = 'filtered_Braille_comments_Class.txt'
second_output_filename = 'filtered_Short_comments_Class.txt'
third_output_filename = 'filtered_Extra_comments_Class.txt'
word_to_filter = "⣿"

comment_filter = CommentFilter(input_file, output_directory)
comment_filter.process_comments(
    word_to_filter, first_output_filename, second_output_filename, third_output_filename)
