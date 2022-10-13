from data_import import texts, calls

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

all_text_nums = [i for list in map(lambda x: x[:2], texts) for i in list]
all_in_call_nums = [i for list in map(lambda x: x[1:2], calls) for i in list]
all_out_call_nums = [i for list in map(lambda x: x[0:1], calls) for i in list]


def get_non_telemarketers():
    return list(set(all_text_nums + all_in_call_nums))


def get_possible_telemarketers():
    non_telemarketers = get_non_telemarketers()
    filtered = filter(
        lambda num: num not in non_telemarketers,
        all_out_call_nums,
    )
    return sorted(list(set(filtered)))


def print_possible_telemarketers():
    print("These numbers could be telemarketers: ")
    for num in get_possible_telemarketers():
        print(num)


print_possible_telemarketers()
