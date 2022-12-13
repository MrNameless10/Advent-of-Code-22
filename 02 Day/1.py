file = open("input2.txt", "r")

lines = file.readlines()

plays = {
    'A': {
        'X\n': 3+1,
        'Y\n': 6+2,
        'Z\n': 0+3
    },

    'B': {
        'X\n': 0+1,
        'Y\n': 3+2,
        'Z\n': 6+3
    },

    'C': {
        'X\n': 6+1,
        'Y\n': 0+2,
        'Z\n': 3+3
    }
}

score = 0
for line in lines:
    play = line.split(' ')
    score += plays[play[0]][play[1]]
print(score)