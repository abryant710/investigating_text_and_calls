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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_non_telemarketers():
    all_texts = texts["text_inc_num"].tolist() + texts["text_ans_num"].tolist()
    all_in_calls = calls["call_ans_num"].tolist()
    return list(set(all_texts + all_in_calls))


def get_possible_telemarketers():
    non_telemarketers = get_non_telemarketers()
    all_out_calls = calls["call_inc_num"].tolist()
    filtered = filter(lambda num: num not in non_telemarketers, all_out_calls)
    return sorted(list(set(filtered)))


def print_possible_telemarketers():
    print("These numbers could be telemarketers: ")
    for num in get_possible_telemarketers():
        print(num)


print_possible_telemarketers()
