#Write a python program that returns the minimum and maximum values in a list of numbers
def find_min_max(numbers):
    if not numbers:
        return None, None  # Return None for both if the list is empty

    min_val = numbers[0]
    max_val = numbers[0]

    for number in numbers:
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number

    return min_val, max_val

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_val, max_val = find_min_max(numbers)
print(f"The minimum value is {min_val}")
print(f"The maximum value is {max_val}")
