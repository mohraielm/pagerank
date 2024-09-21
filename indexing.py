# -------------------------------------------------------------------------
# AUTHOR: Mohraiel Matta
# FILENAME: indexing.py
# SPECIFICATION: This program reads a csv file that includes documents and the document content. From there it will calculate the document term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: 6 hrs
# -----------------------------------------------------------*/

# Importing some Python libraries
import csv
import math

documents = []

# Reading the data in a csv file
with open("collection.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
stopWords = {"i", "and", "she", "her", "they", "their"}
for i, doc in enumerate(documents):
    words = doc.lower().split()
    documents[i] = [word for word in words if word not in stopWords]


# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {"loves": "love", "cats": "cat", "dogs": "dog"}
for i, doc in enumerate(documents):
    documents[i] = [stemming.get(word, word) for word in doc]

# Identifying the index terms.
terms = set()
for doc in documents:
    terms.update(doc)


# Building the document-term matrix by using the tf-idf weights.
docTermMatrix = []


def Uidf(term, documents):
    docC = sum(1 for doc in documents if term in doc)
    return math.log(len(documents) / docC, 10) if docC > 0 else 0


for term in terms:
    idf = Uidf(term, documents)
    tfidf_row = [
        (doc.count(term) / len(doc)) * idf if len(doc) > 0 else 0 for doc in documents
    ]
    docTermMatrix.append(tfidf_row)

# Printing the document-term matrix.
print("tf-idf document-term matrix")
for i, term in enumerate(terms):
    print(f"Term: {term}")
    for j, tfidfVal in enumerate(docTermMatrix[i]):
        print(f"Doc {j + 1}: {round(tfidfVal, 2)}")
    print("\n")
