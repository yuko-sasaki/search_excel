import pandas as pd
import pprint
import re
import sys


EXCEL_NAME = "data/saimu_data.xlsx"
BS_SHEET = "BS"
PL_SHEET = "PL"
TAX_LATE_SHEET = "軽減税率・経過措置対象コード"
GROUP_SHEET = "特例子会社のグループ認定制度"
COM_HOUSE_SHEET = "社宅関連"
SHEET_NAMES = [BS_SHEET, PL_SHEET, TAX_LATE_SHEET, GROUP_SHEET, COM_HOUSE_SHEET]

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

ngram_words = []
for key in args[1:]:
    if len(key) <= 2:
        ngram_words.append({key: key})
        continue
    search_words = []
    for i in range(len(key) - 1):
        search_words.append(key[i:i+2])
    ngram_words.append({key:search_words})

print(ngram_words)

def search_or(keywords):
    searched_rows_dict = {}
    for key in keywords:
        searched_row = []
        for sheet_name in SHEET_NAMES:
            for index, row in df[sheet_name].iterrows():
                for cell in row:
                    if type(cell) is str and key in cell:
                        searched_row.append([sheet_name, row.values.tolist()])
        searched_rows_dict[key] = searched_row
    return searched_rows_dict

def search_and(keywords):
    print(type(df[BS_SHEET]))
    print(df[BS_SHEET].iloc[1,:]) # .iloc[0]
    print("****************")

    new_df = {}
    for sheet_name in SHEET_NAMES:
        new_df[sheet_name] = df[sheet_name].values.tolist()

        sheet_rows = []
        for index, row in df[sheet_name].iterrows():
            sheet_rows.append(row.values.tolist())
        new_df[sheet_name] = sheet_rows

    print(new_df[BS_SHEET][1])

    for key in keywords:
        for sheet_name in SHEET_NAMES:
            sheet_row_list = []
            for row in new_df[sheet_name]:
                for cell in row:
                    if type(cell) is str and key in cell:
                        sheet_row_list.append(reform_words(row))
                        continue
            sheet_row_list = get_unique_list(sheet_row_list)
            new_df[sheet_name] = sheet_row_list

    return new_df

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

or_searched_dict = search_or(args[1:])
#pprint.pprint(or_searched_dict)
and_serched_dict = search_and(args[1:])
pprint.pprint(and_serched_dict)


"""
for search_words in ngram_words:
    for key, n_words in search_words.items():
        for n_word in n_words:
            for sheet_name in SHEET_NAMES:
                print(df[sheet_name])
"""
