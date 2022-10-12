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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""


def get_uniq_called_from_bangalore():
    from_bangalore = calls.drop(calls[calls.call_inc_num.str[:5] != "(080)"].index)
    return from_bangalore.call_ans_num.unique()


def get_ordered_prefixes(unique_called):
    unique_codes = []
    for num in unique_called:
        if num[:2] == "140":
            unique_codes.append(num[:3])
        elif num[0] == "(":
            unique_codes.append(num[1 : num.find(")")])
        elif num[0] in ["7", "8", "9"]:
            unique_codes.append(num[:4])
    return sorted(set(unique_codes))


def print_prefixes(prefixes):
    print("The numbers called by people in Bangalore have codes:")
    for prefix in prefixes:
        print(prefix)


print_prefixes(get_ordered_prefixes(get_uniq_called_from_bangalore()))

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_percent_from_bangalore_to_bangalore():
    from_bangalore = calls.drop(calls[calls.call_inc_num.str[:5] != "(080)"].index)
    from_bangalore_to_bangalore = from_bangalore.drop(
        from_bangalore[from_bangalore.call_ans_num.str[:5] != "(080)"].index
    )
    return round(len(from_bangalore_to_bangalore) / len(from_bangalore) * 100, 2)


print(
    f"{get_percent_from_bangalore_to_bangalore()} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
)
