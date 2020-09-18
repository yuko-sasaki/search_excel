

def make_2_words(keywords):
    ngram_words = []
    for key in keywords:
        if len(key) <= 2:
            ngram_words.append({key: [key]})
            continue
        ngram_words.append({key: [key[i:i+2] for i in range(len(key) - 1)]})
    return ngram_words
