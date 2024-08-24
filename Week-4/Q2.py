def is_first_last_same(lst):
    return lst[0] == lst[-1] if lst else False

numbers = [10, 20, 30, 10]
print("First and last are the same:", is_first_last_same(numbers))
