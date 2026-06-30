from collections import Counter
import sys
filename = sys.argv[1]
try:
    # код, который может упасть
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    # что делать, ЕСЛИ упало именно с FileNotFoundError
    print(f"Файл '{filename}' не найден. Проверьте имя файла.")
    sys.exit(1)
def count_words(text):
    return Counter(text.lower().split()).most_common(5)
def print_top(tuples):
    for element in tuples:
        word,count=element
        print(f"{word} встретилось {count} раз")
print_top(count_words(text))