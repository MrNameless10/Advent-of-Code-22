
file = open("input1.txt", "r")
lines = file.readlines()
sum = 0
list = []
for line in lines:
    if line == "\n":
        list.append(sum)
        sum = 0
    else:
        sum += int(line)
list.sort(reverse=True)
print(list[0] + list[1] + list[2])


