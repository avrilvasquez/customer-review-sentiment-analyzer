import string

review = input("Enter a customer review: ")
print("You wrote:", review)

review_lower = review.lower()

positive_words = ["great", "good", "amazing", "excellent", "love"]
negative_words = ["bad", "terrible", "awful", "poor", "hate"]

positive_count = 0
negative_count = 0

for word in review_lower.split():
    word = word.strip(string.punctuation)

    if word in positive_words:
          positive_count += 1
    elif word in negative_words:
          negative_count += 1

if positive_count > negative_count:
     print("Sentiment: Positive")
elif negative_count > positive_count:
     print("Sentiment: Negative")
else:
     print("Sentiment: Neutral")
