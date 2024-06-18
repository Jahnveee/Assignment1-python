# Write a program in python that counts the frequency of each character in a string
def char_frequency(text):
  char_counts = {}
  for char in text:
    char = char.lower()
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts


text = "Mission"
char_counts = char_frequency(text)
for char, count in char_counts.items():
  print(f"{char}: {count}")
