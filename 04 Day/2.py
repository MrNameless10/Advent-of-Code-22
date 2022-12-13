import re

file = open("input4", "r")
lines = file.read().splitlines()

assignments = []

for line in lines:
            a, b, c, d = map(int, re.findall(r"\d+", line))
            assignments.append([(a, b), (c, d)])

counter = 0

for assignment in assignments:
    if assignment[0][0] <= assignment[1][0] <= assignment[0][1]:
        counter += 1
    elif assignment[1][0]<= assignment[0][0] <= assignment[1][1] :
        counter += 1
print(counter)
