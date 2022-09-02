import json
from fuzzywuzzy import process

with open('quotes.json', 'r', encoding='utf-8') as f:
    QUOTES = json.load(f)

def load_by_index(i):
    return QUOTES[i-1]

def load_fuzzy(s):
    q = process.extractOne(s, QUOTES)
    if q[1] < 35:
        raise Exception
    return q[0]