num = int(input("Enter the number: "))
sum_digits = 0

while num > 0:
    rem = num % 10
    sum_digits += rem
    num = num // 10

print('The sum of digits is:', sum_digits)
