# Steam Reviews and Vader Sentiment Analysis

This project analyzes user reviews on Steam using both direct reviews and sentiment analysis with Vader. Below are the conclusions drawn from the analysis.

## Conclusions

- **Steam Reviews:**
  - Total reviews analyzed: 22,556
  - Positive reviews (True): 21,418 (94.89%)
  - Negative reviews (False): 1,138 (5.04%)

- **Vader Sentiment Analysis:**
  - Total comments analyzed: 22,102
  - Positive comments: 12,660 (57.30%)
  - Negative comments: 5,050 (22.84%)
  - Neutral comments: 4,392 (19.86%)

### Observations and Conclusions

- Steam reviews show an overwhelmingly positive majority, indicating high user satisfaction.
- Vader sentiment analysis reveals a lower proportion of positive sentiments compared to direct Steam reviews, highlighting the presence of neutral and negative sentiments that may not have been evident in Steam's binary reviews.
- Combining direct reviews and sentiment analysis provides a more comprehensive view of user perception, crucial for improving products and services.

## Recommendations

Based on these findings, consider the following actions:
- Address any issues highlighted by negative sentiments to improve user satisfaction.
- Use sentiment analysis tools to capture nuanced user feedback beyond binary reviews.
- Continuously monitor and respond to user feedback to enhance overall user experience.

## References

- Steam reviews data: [Link to JSON file used](data/review_1245620.json)
- Vader sentiment analysis results: [Link to results file](Results/sentiment_analysis_Vader_results.txt)