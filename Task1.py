from data_import import texts, calls

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

text_nums = [i for list in map(lambda x: x[:2], texts) for i in list]
call_nums = [i for list in map(lambda x: x[:2], calls) for i in list]
all_nums = set(text_nums + call_nums)

print(f"There are {len(all_nums)} different telephone numbers in the records.")
