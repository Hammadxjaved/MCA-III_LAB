def count_digits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

number = 12345
print("Total number of digits:", count_digits(number))
