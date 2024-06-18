lines = []

while True:
    intake = input('Enter something, dear user (or just press Enter to finish): ')
    if intake == '':
        break
    lines.append(intake)

print('\nYou entered:')
for line in lines:
    print(line)
