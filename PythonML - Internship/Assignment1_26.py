def starts_or_ends_with(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    
    if starts_with_prefix and ends_with_suffix:
        return f"The string '{string}' starts with '{prefix}' and ends with '{suffix}'."
    elif starts_with_prefix:
        return f"The string '{string}' starts with '{prefix}' but does not end with '{suffix}'."
    elif ends_with_suffix:
        return f"The string '{string}' ends with '{suffix}' but does not start with '{prefix}'."
    else:
        return f"The string '{string}' does not start with '{prefix}' or end with '{suffix}'."

def main():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix to check for: ")
    suffix = input("Enter a suffix to check for: ")

    result = starts_or_ends_with(string, prefix, suffix)
    print(result)

if __name__ == "__main__":
    main()
