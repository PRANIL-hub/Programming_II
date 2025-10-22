"""
CP1404 Practical - Suggested Solution
"""

word_to_count = {}
# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:

    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))
# When we sort a dictionary like this we get a list of the keys in sorted order
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")