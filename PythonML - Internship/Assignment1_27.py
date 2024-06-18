def string_to_list(string):
    return list(string)

def main():
    string = input("Enter a string: ")
    char_list = string_to_list(string)
    print("List of characters:", char_list)

if __name__ == "__main__":
    main()
