def get_book_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    counts = {}

    for ch in text:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


def sort_characters(char):
    sorted = []

    for ch, count in char.items():
        sorted.append({"char": ch, "num": count})

        sorted.sort(key=lambda item: item["num"], reverse=True)

    return sorted
