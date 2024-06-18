def sumOfList(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

list1 = [1, 2, 3, 4]

combined_list = list1
print("The sum is:", sumOfList(combined_list))