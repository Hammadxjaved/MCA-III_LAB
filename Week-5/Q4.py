def merge_odd_even(list1, list2):
    new_list = [x for x in list1 if x % 2 != 0]
    new_list.extend([x for x in list2 if x % 2 == 0])
    return new_list

list1 = [1, 2, 3, 4, 5]
list2 = [10, 15, 20, 25, 30]
print("Merged list:", merge_odd_even(list1, list2))
