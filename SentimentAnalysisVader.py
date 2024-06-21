from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

# Initialize the Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Define the path to the input file
file_path = 'CommentsTXT/filtered_Extra_comments.txt'

# Open the file and read its contents as a list of lines
with open(file_path, 'r', encoding='utf-8') as f:
    lineas_archivo = f.readlines()

# Combine all lines into a single string
text = " ".join(lineas_archivo)

# Split the text into sentences and remove leading/trailing whitespace
sentences = [sentence.strip()
             for sentence in text.split('.') if sentence.strip()]

# Lists to store sentiment values and categorized sentences
sentiment_values = []
positive_sentences = []
negative_sentences = []
neutral_sentences = []

# Analyze sentiment for each sentence
for sentence in sentences:
    sentiment = analyzer.polarity_scores(sentence)
    compound_score = sentiment['compound']
    sentiment_values.append(compound_score)

    if compound_score > 0:
        positive_sentences.append(sentence)
    elif compound_score < 0:
        negative_sentences.append(sentence)
    else:
        neutral_sentences.append(sentence)

# Determine the color for each sentiment score (g: positive, r: negative, b: neutral)
colors = ['g' if s > 0 else 'r' if s < 0 else 'b' for s in sentiment_values]

# Count the occurrences of each sentiment category
color_counts = Counter(colors)

# Calculate percentages of each sentiment category
percentage_positive = round(
    (len(positive_sentences) / len(sentiment_values)) * 100, 2)
percentage_negative = round(
    (len(negative_sentences) / len(sentiment_values)) * 100, 2)
percentage_neutral = round(
    (len(neutral_sentences) / len(sentiment_values)) * 100, 2)

# Print the total number of sentences in each sentiment category and their percentages
print("Total Positive Sentences: ", len(
    positive_sentences), " ", percentage_positive, '%')
print("Total Negative Sentences: ", len(
    negative_sentences), " ", percentage_negative, '%')
print("Total Neutral Sentences: ", len(
    neutral_sentences), " ", percentage_neutral, '%')
print("Total Sentences: ", len(sentiment_values))

# Save the results to a text file
output_file_path = 'Results/sentiment_analysis_Vader_results.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(f"{len(positive_sentences)}\n")
    output_file.write(f"{len(negative_sentences)}\n")
    output_file.write(f"{len(neutral_sentences)}\n")
    output_file.write(f"{len(sentiment_values)}\n")

print(f"Sentiment analysis results saved to: {output_file_path}")

# Provided data
labels = ['Positive', 'Negative', 'Neutral']
sizes = [len(positive_sentences), len(
    negative_sentences), len(neutral_sentences)]

# Global font size configuration
plt.rc('font', size=14)  # Change the default font size to 14

# Bar Chart
plt.figure(figsize=(10, 6))  # Set the figure size
# Create bar chart with specified colors
plt.bar(labels, sizes, color=['green', 'red', 'blue'])
plt.xlabel('Sentiment', fontsize=16)  # Set the x-axis label font size
plt.ylabel('Number of Sentences', fontsize=16)  # Set the y-axis label font size
plt.title('Number of Sentences by Sentiment using vaderSentiment',
          fontsize=18)  # Set the title font size
# Add data labels above the bars
for i, value in enumerate(sizes):
    plt.text(i, value + 150, str(value), ha='center', va='bottom',
             fontsize=12)  # Set the font size of the values
# Save the bar chart
plt.savefig('Results/bar_chart_vader.png', dpi=200,
            bbox_inches='tight', edgecolor='black')
