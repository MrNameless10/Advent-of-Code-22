file = open("input3", "r")
lines = file.read().splitlines()

def get_priority(x: str) -> int:
    return ord(x) - ord("a") + 1 if x.islower() else ord(x) - ord("A") + 27

sum = 0
for i in range(0, len(lines), 3):
    common = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
    sum += get_priority(common.pop())
print(sum)







