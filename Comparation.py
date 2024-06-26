import json
import matplotlib.pyplot as plt

# File paths
json_file = 'data/review_1245620.json'
text_file = 'Results/sentiment_analysis_Vader_results.txt'

# Processing JSON file
print("="*40)
# Open and read the JSON file for Steam reviews
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract 'voted_up' values
voted_up_values = [review_info['voted_up']
                   for review_info in data['reviews'].values()]

# Count 'True' and 'False' values using list count method
true_count = voted_up_values.count(True)
false_count = voted_up_values.count(False)
total_count = len(voted_up_values)

# Print counts with updated messages
print(f"[INFO] True count of values obtained from Steam reviews: {true_count}")
print(
    f"[INFO] False count of values obtained from Steam reviews: {false_count}")
print(
    f"[INFO] Total count of values obtained from Steam reviews: {total_count}")

# Processing text file for Vader Sentiment Analysis results
print("="*40)
# Open and read the text file for Vader Sentiment Analysis results
with open(text_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    # Ensure to strip newlines and convert to integers
    positive_comments = int(lines[0].strip())
    negative_comments = int(lines[1].strip())
    neutral_comments = int(lines[2].strip())
    total_comments = int(lines[3].strip())

# Print values with updated messages indicating Vader Sentiment Analysis
print(
    f"[INFO] Positive Comments from Vader Sentiment Analysis: {positive_comments}")
print(
    f"[INFO] Negative Comments from Vader Sentiment Analysis: {negative_comments}")
print(
    f"[INFO] Neutral Comments from Vader Sentiment Analysis: {neutral_comments}")
print(f"[INFO] Total Comments from Vader Sentiment Analysis: {total_comments}")

"""Graph 1: Comparison of Total Reviews: Steam vs Vader Analysis"""
# Data
total_reviews_steam = total_count  # Total reviews from Steam obtained
total_reviews_vader = total_comments  # Total reviews after Vader analysis

# Calculate the difference
difference = abs(total_reviews_steam - total_reviews_vader)

# Labels and values
labels = ['Steam Reviews', 'Vader Sentiment Analysis']
values = [total_reviews_steam, total_reviews_vader]

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['green', 'red'])
plt.xlabel('Source of Reviews', fontsize=12)
plt.ylabel('Total Reviews', fontsize=12)
plt.suptitle(
    'Comparison of Total Reviews: Steam vs Vader Analysis', fontsize=18)
plt.title(f'Difference: {difference} Reviews', fontsize=14, loc='center')
# Add data labels above the bars
for i, value in enumerate(values):
    plt.text(i, value + 100, str(value), ha='center', va='bottom', fontsize=12)
plt.tight_layout()  # Ensures all elements fit nicely in the plot area
plt.savefig('Results/Comparison_TotalReviews.png', dpi=200,
            bbox_inches='tight', edgecolor='black')

"""Graph 2: Comparison of Total Positive Reviews: Steam vs Vader Analysis"""
# Data
positive_reviews_steam = true_count  # Positive reviews from Steam
# Positive reviews after Vader analysis
positive_reviews_vader = positive_comments

# Calculate the difference
differencePositive = abs(positive_reviews_steam - positive_reviews_vader)

# Labels and values
labels = ['Steam Reviews', 'Vader Analysis']
values = [positive_reviews_steam, positive_reviews_vader]

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['green', 'red'])
plt.xlabel('Source of Reviews', fontsize=12)
plt.ylabel('Total Positive Reviews', fontsize=12)
plt.suptitle(
    'Comparison of Total Positive Reviews: Steam vs Vader Analysis', fontsize=18)
plt.title(f'Difference: {differencePositive} Reviews',
          fontsize=14, loc='center')
# Add data labels above the bars
for i, value in enumerate(values):
    plt.text(i, value + 100, str(value), ha='center', va='bottom', fontsize=12)
plt.tight_layout()  # Ensures all elements fit nicely in the plot area
plt.savefig('Results/Comparison_PositiveReviews.png',
            dpi=200, bbox_inches='tight', edgecolor='black')

"""Graph 3: Comparison of Total Negative Reviews: Steam vs Vader Analysis"""
# Data
negative_reviews_steam = false_count  # Negative reviews from Steam
# Negative reviews after Vader analysis
negative_reviews_vader = negative_comments

# Calculate the difference
differenceNegative = abs(negative_reviews_steam - negative_reviews_vader)

# Labels and values
labels = ['Steam Reviews', 'Vader Analysis']
values = [negative_reviews_steam, negative_reviews_vader]

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['blue', 'green'])
plt.xlabel('Source of Reviews', fontsize=12)
plt.ylabel('Total Negative Reviews', fontsize=12)
plt.suptitle(
    'Comparison of Total Negative Reviews: Steam vs Vader Analysis', fontsize=18)
plt.title(f'Difference: {differenceNegative} Reviews',
          fontsize=14, loc='center')
# Add data labels above the bars
for i, value in enumerate(values):
    plt.text(i, value + 50, str(value), ha='center', va='bottom', fontsize=12)
plt.tight_layout()  # Ensures all elements fit nicely in the plot area
plt.savefig('Results/Comparison_NegativeReviews.png',
            dpi=200, bbox_inches='tight', edgecolor='black')
