# Import the os module to work with file paths
import os

# Function to filter comments


def filtar_commentarios(comentarios):
    segundoFiltro = []
    segundosEliminados = []

    # Filter comments by length and characters
    for comment in comentarios:
        tamano = len(comment)
        # Filter comments shorter than 5 characters
        if tamano < 5:
            if len(comment) != 0 and len(comment) <= 2:
                segundosEliminados.append(comment)
            elif len(comment) > 2 and ord(comment[0]) < 63:
                segundosEliminados.append(comment)
            elif len(comment) > 2 and ord(comment[0]) > 63:
                # Keep comments where the first character is a letter (A-Z, a-z)
                if (ord(comment[0]) > 63 and ord(comment[0]) <= 90) or (ord(comment[0]) > 95 and ord(comment[0]) <= 122):
                    segundoFiltro.append(comment)
                else:
                    segundosEliminados.append(comment)
        else:
            segundoFiltro.append(comment)

    return segundoFiltro, segundosEliminados


# Define the path to the input file and output directory
file_path = 'CommentsTXT/filtered_Braille_comments.txt'
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

comentariosFiltrados, comentariosEliminados = filtar_commentarios(
    lineas_archivo)

print("[INFO] Total number of comments that passed the filter:",
      len(comentariosFiltrados))
print("[INFO] Total number of comments eliminated:", len(comentariosEliminados))

output_file_path = os.path.join(
    output_directory, 'filtered_Short_comments.txt')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(comentariosFiltrados)

print("[INFO] Filtered comments saved to:", output_file_path)
