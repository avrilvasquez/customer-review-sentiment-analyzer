import string

review = input("Enter a customer review: ").strip()

if not review:
        print("Please enter a review.")
        raise SystemExit

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

print("Positive words found:", positive_count)
print("Negative words found:", negative_count)

if positive_count > negative_count:
     print("Sentiment: Positive")
elif negative_count > positive_count:
     print("Sentiment: Negative")
elif positive_count > 0:
      print("Sentiment: Mixed")
else:
      print("Sentiment: No sentiment words detected")
