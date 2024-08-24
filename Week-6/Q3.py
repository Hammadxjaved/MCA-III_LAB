def sum_of_squares(num):
    first_two = int(str(num)[:2])
    last_two = int(str(num)[-2:])
    return first_two**2 + last_two**2

number = 1233
print("Sum of squares:", sum_of_squares(number))
