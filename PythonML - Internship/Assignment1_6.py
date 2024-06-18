#Write a program that reads the content of a text file and prints it to the console
filename = "my_file.txt"
try:
  with open(filename, "r") as file:
    print(file.read())
except FileNotFoundError:
  print(f"Error: File '{filename}' not found.")
