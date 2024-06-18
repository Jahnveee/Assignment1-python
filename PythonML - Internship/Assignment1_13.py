#Write a program that asks the user for their birth year and calculates their age
birth_year = int(input("What is your birth year? "))
curr_year = int(input("Which year is this? "))
age = curr_year - birth_year
print("Your age is: ", age)
