from collections import Counter


def count_words(text):
    # split розбиває текст на слова, Counter рахує кожне слово
    words = text.split()
    return Counter(words)
