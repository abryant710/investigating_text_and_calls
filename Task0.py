"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text_inc_num, text_ans_num, text_time = texts[0]
print(f"First record of texts, {text_inc_num} texts {text_ans_num} at time {text_time}")

call_inc_num, call_ans_num, call_time, call_len_s = calls[-1]
print(
    f"Last record of calls, {call_inc_num} calls {call_ans_num} at time {call_time}, lasting {call_len_s} seconds"
)
