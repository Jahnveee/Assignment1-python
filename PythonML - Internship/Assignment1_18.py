#check for anagrams


def is_anagram(str1, str2):

  # Convert both strings to lowercase and remove spaces.
  str1 = str1.lower().replace(" ", "")
  str2 = str2.lower().replace(" ", "")

  # Check if the lengths of the strings are equal.
  if len(str1) != len(str2):
    return False

  # Create a dictionary to store the character counts for str1.
  char_counts = {}
  for char in str1:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  # Iterate through str2 and check if each character exists in the dictionary with a non-zero count.
  for char in str2:
    if char not in char_counts or char_counts[char] == 0:
      return False
    char_counts[char] -= 1

  # If all characters in str2 are found in str1 with matching counts, then they are anagrams.
  return True

# Example usage
str1 = "listen"
str2 = "silent"

if is_anagram(str1, str2):
  print(f"{str1} and {str2} are anagrams.")
else:
  print(f"{str1} and {str2} are not anagrams.")
