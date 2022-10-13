# Big O analysis of each solution

## Task0

Since this task only involves reading from a list the time complexity is O(1).

Space complexity is not worth considering as no data is stored in memory.

## Task1

The list mapping and flattening functions are O(n + m) as they involve iterating over the entire combined list of text_nums + call_nums.
The time complexity of len() is O(1)
The time complexity of the set() method is O(n + m).

The overall time complexity is O(n + m) as the mapping, flattening, and set methods are the bottlenecks and have equivalent time complexity.

Space complexity is O(n + m) as the list is stored in memory.

## Task2

The time complexity of the for loop is O(n) as it iterates over all values in the calls dictionary.
The dictionary lookups are O(1) as they are hash lookups and have contstant time.
The max() method is O(n) as it iterates over all values in the dictionary to find the maximum.

Thus, the overall time complexity is O(n) as the max() method and for loop are the bottlenecks.

Space complexity is O(n) as the dictionary is stored in memory.

## Task3

### Part A

The get_uniq_called_from_bangalore() function is O(n) as it uses filter() and set() which both have O(n) time complexity.
The get_ordered_prefixes() method is O(n log n) as it uses the sorted() method which is a Timsort implementation. It also includes a for loop, which is O(n), but this is faster relatively speaking compared to the sorting method.
The print_prefixes() method has a time complexity of O(n) as it iterates over all values in the list.

The overall time complexity is O(n log n) as the sorting method is the bottleneck.

The space complexity is O(n) as the list is stored in memory.

### Part B

This solution uses the filter() method which has a time complexity of O(n).

The space complexity is O(n) as the list is stored in memory.

## Task4

The map() method has a time complexity of O(n) or O(m) as it iterates over all values in one of the lists.
The filter() and set() methods are all O(n + m) as they iterate over all values in the list.
The time complexity of the sorted() method is O((n + m) log (n + m)) as it uses the Timsort implementation and uses a combination of the lists.
The print_possible_telemarketers() method has a time complexity of O(n + m) as it iterates over all values in the combined list.

Once again, the overall time complexity is O((n + m) log (n + m)) as the sorting method is the bottleneck.

The space complexity is O(n + m) as the list is stored in memory.
