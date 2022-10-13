from data_import import calls

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

nums_dict = {}

for call_inc_num, call_ans_num, call_time, call_len_s in calls:
    nums_dict[call_inc_num] = nums_dict.get(call_inc_num, 0) + int(call_len_s)
    nums_dict[call_ans_num] = nums_dict.get(call_ans_num, 0) + int(call_len_s)

max_number = max(nums_dict, key=nums_dict.get)

print(
    f"{max_number} spent the longest time, {nums_dict[max_number]} seconds, on the phone during September 2016."
)
