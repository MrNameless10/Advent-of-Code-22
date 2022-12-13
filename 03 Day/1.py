file = open("input3", "r")
lines = file.readlines()

result = 0
for line in lines:
    line = line.strip()
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
    repeated = []
    for letter in first_half:
        if letter in second_half:
            repeated.append(letter)
            if letter.isupper():
                result += ord(letter) - ord('A') + 27
            else:
                result += ord(letter) - ord('a') + 1
            break
print(result)


