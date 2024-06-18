def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
lst = [1, 2, 3, 2, 4, 2, 5, 2]
element = 2
print(f"The element {element} occurs {count_occurrences(lst, element)} times in the list.")