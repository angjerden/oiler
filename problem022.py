__author__ = 'anders'

namesfile = open('resources/names.txt', 'r')
names_raw = str(namesfile.readline())
names_raw = names_raw.split(",")
names = []
for name in names_raw:
    name = name[1:-1]
    names.append(name)
names.sort()

total_score = 0

for rank in range(0, len(names)):
    name_score = 0
    output = str(names[rank]) + ": "
    for letter in names[rank]:
        letter_score = ord(letter) - 64
        output += ' + ' + str(letter_score)
        name_score += letter_score
    output += ' = ' + str(name_score) + " * " + str(rank + 1) + " = "
    name_score *= (rank + 1)
    output += str(name_score)
    total_score += name_score
    print output + " - Total score: " + str(total_score)
