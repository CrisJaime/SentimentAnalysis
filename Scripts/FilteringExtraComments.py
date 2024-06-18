import os

# Function to filter comments


def filtrar_comments(comentarios):
    tercerfiltro = []
    tercereliminados = []
    for lines in comentarios:
        if len(lines) > 0:
            # Get the first character of the line if it's not empty
            x = lines[0]

        # Filter out lines where the first character has a Unicode value of 800 or higher
        if ord(x) >= 800:
            tercereliminados.append(lines)

        # Filter out lines where the first character is a space (32), newline (10), or period (46)
        elif ord(x) == 32 or ord(x) == 10 or ord(x) == 46:
            tercereliminados.append(lines)

        # Filter out lines where the first character is in the extended ASCII range (128 to 255)
        elif ord(x) >= 128 and ord(x) <= 255:
            tercereliminados.append(lines)
        # Keep lines that don't meet any of the above conditions
        else:
            tercerfiltro.append(lines)

    return tercerfiltro, tercereliminados


# Define the path to the input file and output directory
file_path = 'CommentsTXT/filtered_Short_comments.txt'
output_directory = 'CommentsTXT/'

# Open the file and read its contents as a list of lines
with open(file_path, 'r', encoding='utf-8') as f:
    lineas_archivo = f.readlines()

# Count the number of comments
num_comments = len(lineas_archivo)

print("==="*10)
# Print the number of comments
print("[INFO] Number of comments after first filter:", num_comments)
print("==="*10)

comentariosFiltrados, comentariosEliminados = filtrar_comments(lineas_archivo)

print("[INFO] Total number of comments that passed the filter:",
      len(comentariosFiltrados))
print("[INFO] Total number of comments eliminated:", len(comentariosEliminados))


output_file_path = os.path.join(
    output_directory, 'filtered_Extra_comments.txt')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(comentariosFiltrados)

print("[INFO] Filtered comments saved to:", output_file_path)