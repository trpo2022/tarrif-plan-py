import review.review as r
import json

if __name__ == "__main__":
data = {}

with open('questions.json') as json_file:
data = json.load(json_file)

review = r.Review(data)
review.start()