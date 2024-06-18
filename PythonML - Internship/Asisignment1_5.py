#Write a program that takes a string input from the user and writes it to a text file
text_to_write = input("Enter the text you want to write to the file: ")
with open("my_file.txt", "w") as file:
  file.write(text_to_write)
print("Text written to my_file.txt successfully!")
