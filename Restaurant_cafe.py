
# Q10: Restaurant and Cafe Review Analysis

reviews = [
    ("Momo Magic", 5, "Delicious momo and friendly staff, very clean place"),
    ("Momo Magic", 4, "Tasty food but slow service"),
    ("Thakali Kitchen", 2, "Food was cold and the place was dirty"),
    ("Thakali Kitchen", 3, "Good dal bhat but expensive and slow"),
    ("Lakeside Cafe", 5, "Amazing view, delicious coffee, friendly owner")
]

positive = {"delicious", "friendly", "clean", "tasty", "good", "amazing"}
negative = {"slow", "cold", "dirty", "expensive", "rude"}

# Place anusar ratings store garne dictionary
place_ratings = {}

word_counts = {}

# Positive ra negative words ko combined set
opinion_words = positive.union(negative)

# Each review process garne
for place, rating, review in reviews:

    # Review lai lowercase banauna
    clean_review = review.lower()

    # Comma hatauna
    clean_review = clean_review.replace(",", "")

    # Review lai words ko list banauna
    words = clean_review.split()

    # Words lai set banauna
    review_words = set(words)

    # Positive ra negative words count garna
    pos_count = len(review_words.intersection(positive))
    neg_count = len(review_words.intersection(negative))

    # Review ko mood decide garne
    if pos_count > neg_count:
        mood = "Positive"
    elif pos_count < neg_count:
        mood = "Negative"
    else:
        mood = "Mixed"

    # Review ko result print garna
    print(f"{place:<16} {rating}* pos={pos_count} neg={neg_count} -> {mood}")

    # Place dictionary ma chaina bhane empty list banauna
    if place not in place_ratings:
        place_ratings[place] = []

    # Rating list ma add garne
    place_ratings[place].append(rating)

    # Opinion words ko frequency count garna
    for word in words:

        if word in opinion_words:

            # Word pahila dictionary ma chaina bhane zero bata suru
            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1


print("Average rating:")

for place, ratings in place_ratings.items():

    average = sum(ratings) / len(ratings)

    print(f"  {place:<16} {average:.1f} from {len(ratings)} reviews")


# Opinion words lai frequency descending ra alphabetical ascending sort garne
top_words = sorted(
    word_counts.items(),
    key=lambda item: (-item[1], item[0])
)

print("Top opinion words:", top_words[:3])
