# Big O analysis of each solution

## Task0

Since this task only involves reading from a list the time complexity is O(1).

Space complexity is not worth considering as no data is stored in memory.

## Task1

The time complexity of len() is O (1)
The time complexity of the set() method is O(len()), which is still contant time.
The conversion of the pandas Dataframe to a list is likely O(n) as it involves iterating over the entire dataframe.

The overall time complexity is O(n) as the list conversion method is the bottleneck.

Space complexity is O(n) as the list is stored in memory.

## Task2

The time complexity of the for loop is O(n) as it iterates over all values in the dictionary.
The dictionary lookups are O(1) as they are hash lookups.
The max() method is O(n) as it iterates over all values in the dictionary to find the maximum.

Thus, the overall time complexity is O(n) as the max() method and for loop are the bottlenecks.

Space complexity is O(n) as the dictionary is stored in memory.

## Task3

### Part A

The get_ordered_prefixes() method is O(n log n) as it uses the sorted() method which is a Timsort implementation. It also includes a for loop, which is O(n), but this is faster relatively speaking compared to the sorting method. The sorting method is also not nested in the for loop, so it is not executed n times.
The print_prefixes() method has a time complexity of O(n) as it iterates over all values in the list.

The overall time complexity is O(n log n) as the sorting method is the bottleneck.

The space complexity is O(n) as the list is stored in memory.

### Part B

All methods in this solution are only accessing data and doing Math calculations, so the time complexity is O(1).

The space complexity is not worth considering as no data is stored in memory.

## Task4

The time complexity of converting a set to a list is linear in the number of list elements. So, if the set has n elements, the asymptotic complexity is O(n).
The time complexity of the sorted() method is O(n log n) as it uses the Timsort implementation.
The print_possible_telemarketers() method has a time complexity of O(n) as it iterates over all values in the list.

Once again, the overall time complexity is O(n log n) as the sorting method is the bottleneck.

The space complexity is O(n) as the list is stored in memory.
