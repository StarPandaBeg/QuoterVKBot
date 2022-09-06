from fuzzywuzzy import process

from func import load_json

QUOTES = load_json('quotes.json')

def load_by_index(i):
    return QUOTES[i-1]

def load_fuzzy(s):
    q = process.extractOne(s, QUOTES)
    if q[1] < 35:
        raise Exception
    return q[0]