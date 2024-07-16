def square_digits(num):
    # Your code here
    count = 0
    a = num % 10
    count = count + (a**2)
    num = num // 10

    return int(count)


print(square_digits(98))
Hello Againhello againhello again