import re
from nltk import word_tokenize, sent_tokenize
from nltk.lm.preprocessing import pad_both_ends

def tokenize(text, n):
    tokens = list()
    s_t_text = sent_tokenize(text)
    for s in s_t_text:
        # To clean out the text. Get rid of the puntuation and lowercase all the letters.
        cleaned_text = re.sub(r"\W+", ' ', s).lower()
        # Add the pads at the begining and the end of the setences.
        tokens.extend(pad_both_ends(word_tokenize(cleaned_text), n))
    return tokens

def detokenize(tokens):
    # Get rid of the pads to make the text human readable.
    s = ' '.join(tokens)
    return s
