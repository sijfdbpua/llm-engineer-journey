with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()
def count_words(text):
    words_counts={}
    low_text=text.lower().split(" ")
    for char in low_text:
        if char not in words_counts:
            words_counts[char]=1
        else:
            words_counts[char]+=1
    text_tupeling=words_counts.items()
    return sorted(text_tupeling, key=lambda x: x[1],reverse=True)

def print_top(sorted_tuples):
    for elem in sorted_tuples[0:5]:
        word,count=elem
        print(f"{word} встретилось {count} раз")

print_top(count_words(text))