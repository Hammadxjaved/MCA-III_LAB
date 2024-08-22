def reverse_digits(num):
    while num > 0:
        digit = num % 10
        print(digit, end="")
        num = num // 10

number = 12345
reverse_digits(number)
