#Write a python program that calculates the factorial of a given number.
a = int(input("Enter number: "))
n=1
fact = 1
while n < a:
    fact = a*n
    n = n+1

print("Factoial is: ", fact)