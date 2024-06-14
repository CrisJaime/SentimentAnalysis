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

# File path to save the reviews
file_path = 'CommentsTXT/comentarios_juego_{}.txt'.format(app_id)

# List to store the reviews
archivo = []

# Create and write to the file
with open(file_path, 'w', encoding="utf-8") as f:
    num = 0
    for reviews in review_dict.values():
        for review in reviews:
            if num <= 34962:
                review_text = reviews[review]['review']
                archivo.append(review_text)
                f.write(review_text + '\n')
            num += 1