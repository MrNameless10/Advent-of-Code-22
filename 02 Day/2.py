file = open("input2.txt", "r")

lines = file.readlines()

plays = {
    'A': {
        'X\n': 3+0,
        'Y\n': 1+3,
        'Z\n': 2+6
    },

    'B': {
        'X\n': 1+0,
        'Y\n': 2+3,
        'Z\n': 3+6
    },

    'C': {
        'X\n': 2+0,
        'Y\n': 3+3,
        'Z\n': 1+6
    }
}

score = 0
for line in lines:
    play = line.split(' ')
    score += plays[play[0]][play[1]]
print(score)