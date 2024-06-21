# Sentiment Analysis Using NLTK

## Purpose

The purpose of this script is to perform sentiment analysis on a collection of comments using the NLTK library. The script processes the text, filters out common stopwords, tokenizes the text, and categorizes the words into positive, negative, or neutral sentiment categories using the VADER sentiment analysis tool. It also visualizes the results in a bar chart and saves both the sentiment analysis results and the chart.

## How It Works

1. **Import Libraries**

   - `nltk`: Natural Language Toolkit for text processing.
   - `stopwords` and `word_tokenize` from `nltk.corpus` and `nltk.tokenize`, respectively.
   - `SentimentIntensityAnalyzer` from `nltk.sentiment` for sentiment analysis.
   - `matplotlib.pyplot` for creating visualizations.

2. **Download NLTK Data Files**

   - Downloads the necessary NLTK data files for stopwords, tokenization, and sentiment analysis.

3. **Read Input File**

   - Reads the content of the input file (`filtered_Extra_comments.txt`) and combines all lines into a single string.

4. **Preprocess Text**

   - Retrieves the set of English stopwords.
   - Tokenizes the text into words.
   - Filters out stopwords and non-alphabetic tokens.

5. **Sentiment Analysis**

   - Initializes the Sentiment Intensity Analyzer.
   - Analyzes the sentiment of each word in the filtered sentence.
   - Categorizes words based on their sentiment scores (positive, negative, neutral).

6. **Calculate and Print Sentiment Statistics**

   - Calculates the percentage of words in each sentiment category.
   - Prints the total number of words in each sentiment category along with their percentages.

7. **Save Results to a Text File**

   - Saves the counts of positive, negative, and neutral words, and the total number of words to a text file.

8. **Visualize Results**
   - Creates a bar chart showing the number of words in each sentiment category.
   - Configures the font size and labels for the chart.
   - Saves the bar chart as an image file.

## Usage

1. **Install Required Libraries**:

   ```bash
   pip install nltk matplotlib vaderSentiment
   ```

2. **Download NLTK Data Files**:

   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('vader_lexicon')
   ```

3. **Run the Script**:

   ```bash
   python sentiment_analysis.py
   ```

4. **Check Results**:
   - The sentiment analysis results will be saved in `Results/sentiment_analysis_NLTK_results.txt`.
   - The bar chart will be saved as `Results/bar_chart_NLTK.png`.
