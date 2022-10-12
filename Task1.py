"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import pandas as pd

text_col_names = ["text_inc_num", "text_ans_num", "text_time"]
texts = pd.read_csv("texts.csv", names=text_col_names)
call_col_names = ["call_inc_num", "call_ans_num", "call_time", "call_len_s"]
calls = pd.read_csv("calls.csv", names=call_col_names)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
all_nums = set(
    texts["text_inc_num"].tolist()
    + texts["text_ans_num"].tolist()
    + calls["call_inc_num"].tolist()
    + calls["call_ans_num"].tolist()
)
print(f"There are {len(all_nums)} different telephone numbers in the records.")
