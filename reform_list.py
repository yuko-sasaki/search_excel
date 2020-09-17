import re


def reform_words(words):
    new_words = []
    for word in words:
        if type(word) is str:
            new_words.append(re.sub('[\n 　]', '', word))
        else:
            new_words.append(word)
    return new_words

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]
