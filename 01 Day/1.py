file = open("input1.txt", "r")

lines = file.readlines()

max = 0
sum = 0
for line in lines:
    if line == "\n":
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += int(line)
    
print(max)  