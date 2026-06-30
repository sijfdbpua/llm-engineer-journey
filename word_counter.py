from collections import Counter
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()
words_counts=Counter(text.split()).most_common(5)
def print_top(tuples):
    for element in tuples:
        word,count=element
        print(f"{word} встретилось {count} раз")
print_top(words_counts)