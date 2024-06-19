import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the necessary NLTK data files
# Stopwords: Common words that are usually removed in text processing (e.g., "the", "and")
# Punkt: A tokenizer that divides text into a list of sentences
# VADER (Valence Aware Dictionary and sEntiment Reasoner): A sentiment analysis tool
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('vader_lexicon')

# Define the path to the input file
file_path = 'CommentsTXT/filtered_Extra_comments.txt'

# Open the file and read its contents as a list of lines
with open(file_path, 'r', encoding='utf-8') as f:
    lineas_archivo = f.readlines()

# Combine all lines into a single string
text = " ".join(lineas_archivo)

# Get the set of English stopwords
stopWords = set(stopwords.words('english'))

# Tokenize the text into words
word_tokens = word_tokenize(text)

# Filter out stopwords and non-alphabetic tokens
filtered_sentence = [
    w for w in word_tokens if not w.lower() in stopWords and w.isalpha()]

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()
valuesNLTK = []

# Lists to store words based on their sentiment
wordspositiveNLTK = []
wordsnegativeNLTK = []
wordsneutralNLTK = []

# Analyze the sentiment of each word in the filtered sentence
for filtered in filtered_sentence:
    sentimientoSia = sia.polarity_scores(filtered)
    compound_score = sentimientoSia['compound']
    valuesNLTK.append(compound_score)

    # Positive sentiment is represented by compound_score > 0
    if compound_score > 0:
        wordspositiveNLTK.append(filtered)
    # Negative sentiment is represented by compound_score < 0
    elif compound_score < 0:
        wordsnegativeNLTK.append(filtered)
    # Neutral sentiment is represented by compound_score == 0
    else:
        wordsneutralNLTK.append(filtered)

# Print the total number of words in each sentiment category
percentage_positive = round(
    (len(wordspositiveNLTK) / len(valuesNLTK)) * 100, 2)
percentage_negative = round(
    (len(wordsnegativeNLTK) / len(valuesNLTK)) * 100, 2)
percentage_neutral = round((len(wordsneutralNLTK) / len(valuesNLTK)) * 100, 2)

print("Total Positive Words: ", len(
    wordspositiveNLTK), " ", percentage_positive, '%')
print("Total Negative Words: ", len(
    wordsnegativeNLTK), " ", percentage_negative, '%')
print("Total Neutral Words: ", len(
    wordsneutralNLTK), " ", percentage_neutral, '%')
print("Total Words: ", len(valuesNLTK))
