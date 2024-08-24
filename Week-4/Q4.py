def iterate_lists(lst1, lst2):
    for item1, item2 in zip(lst1, reversed(lst2)):
        print(item1, item2)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
iterate_lists(list1, list2)
