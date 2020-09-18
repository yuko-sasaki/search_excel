import pandas as pd
import pprint
import sys

from config import EXCEL_NAME, BS_SHEET
from search import ngram_search
from search import basic_search
import reform_list as rl

# read excel
df = pd.read_excel(EXCEL_NAME, sheet_name = None , header = None)
"""
print(type(df[BS_SHEET]))
print(df[BS_SHEET].iloc[0])
print(df[BS_SHEET].iloc[1])
print(df[BS_SHEET].iloc[2])
print(df[BS_SHEET].iloc[2,0])

print("******************")

for key in df:
    print(key)

print("******************")
"""
args = sys.argv

# n-gram
ngram_words = ngram_search.make_2_words(args[1:])
print(ngram_words)

for word_dic in ngram_words:
    for word in word_dic.values():
        or_searched_dict = basic_search.search_or(word, df)
        pprint.pprint(or_searched_dict)
"""
and_serched_dict = basic_search.search_and(args[1:], df)
pprint.pprint(and_serched_dict)"""
