# Import the os module to work with file paths
import os

# Function to filter comments
def filtrar_comentarios(comentarios, palabra):
    filtro = []
    eliminados = []
    for line in comentarios:
        if palabra in line:
            eliminados.append(line)
        else:
            filtro.append(line)
    return filtro, eliminados

# Define the path to the input file and output directory
file_path = 'CommentsTXT/comentarios_juego_1245620.txt'
output_directory = 'CommentsTXT/'

# Open the file and read its contents as a list of lines
with open(file_path, 'r', encoding='utf-8') as f:
    lineas_archivo = f.readlines()

# Count the number of comments
num_comments = len(lineas_archivo)

print("==="*10)
# Print the number of comments
print("[INFO] Number of comments:", num_comments)
print("==="*10)

# Eliminate comments with Braille symbols
palabra = "⣿"
primerFiltro, primerEliminados = filtrar_comentarios(lineas_archivo, palabra)

print("[INFO] Total number of comments that passed the filter:", len(primerFiltro))
print("[INFO] Total number of comments eliminated:", len(primerEliminados))
print("==="*10)

# Define the path to the output file
output_file_path = os.path.join(output_directory, 'filtered_Braille_comments.txt')

# Write the filtered comments to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(primerFiltro)

print("[INFO] Filtered comments saved to:", output_file_path)