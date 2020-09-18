from config import SHEET_NAMES
import reform_list as rl

# r:{keyword:[[sheet_name,row], ...], keyword:[[sheet_name,row], ...], ...}
def search_or(keywords, data_frame):
    searched_rows_dict = {}
    for key in keywords:
        searched_row = []
        for sheet_name in SHEET_NAMES:
            for index, row in data_frame[sheet_name].iterrows():
                if key_in_cell(row, key):
                    searched_row.append([sheet_name, rl.reform_words(row.values.tolist())])
        searched_rows_dict[key] = rl.get_unique_list(searched_row)
    return searched_rows_dict

# r:{sheet_name:[row, row, ...], sheet_name:[row, row, ...], ...}
def search_and(keywords, data_frame):
    new_df = {}
    for sheet_name in SHEET_NAMES:
        new_df[sheet_name] = data_frame[sheet_name].values.tolist()
        sheet_rows = []
        for index, row in data_frame[sheet_name].iterrows():
            sheet_rows.append(row.values.tolist())
        new_df[sheet_name] = sheet_rows
    for key in keywords:
        for sheet_name in SHEET_NAMES:
            sheet_row_list = []
            for row in new_df[sheet_name]:
                if key_in_cell(row, key):
                    sheet_row_list.append(rl.reform_words(row))
            sheet_row_list = rl.get_unique_list(sheet_row_list)
            new_df[sheet_name] = sheet_row_list
    return new_df

def key_in_cell(row, key):
    in_cell = False
    for cell in row:
        if type(cell) is str and key in cell:
            in_cell = True
            break
    return in_cell
