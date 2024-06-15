import steamreviews

# This is the Steam ID for the game Elden Ring
app_id = 1245620  

# Parameters for fetching the reviews
request_params = {
    'language': 'english',        # Language of the reviews
    'review_type': 'all',         # Type of reviews (positive or negative)
    'purchase_type': 'all',       # Type of purchase (direct or gift)
    'day_range': '100'            # Reviews from the last 100 days
}

# Fetch the reviews for the game
review_dict, query_count = steamreviews.download_reviews_for_app_id(
    app_id, chosen_request_params=request_params
)

# Specify the file path to save the reviews
file_path = 'path/to/directory/comentarios_juego_{}.txt'.format(app_id)

# List to store the reviews
archivo = []

# Create and write to the file
with open(file_path, 'w', encoding="utf-8") as f:
    num = 0
    # Iterate through the reviews
    for reviews in review_dict.values():
        for review in reviews:
            if num <= 34962:
                # Extract the review text
                review_text = reviews[review]['review']
                # Add the review text to the list
                archivo.append(review_text)
                # Write the review text to the file
                f.write(review_text + '\n')
            num += 1