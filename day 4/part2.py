# failed
data = []
with open("day 4/full.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        data.append(row)


def testForXmas(data, x, y):
    validPatterns = [
        [
            ["S", "X", "S"],
            [
                "X",
                "A",
                "X",
            ],  # to keep auto format from messing up the pattern we write this comment
            ["M", "X", "M"],
        ],
        [
            ["M", "X", "S"],
            [
                "X",
                "A",
                "X",
            ],  # to keep auto format from messing up the pattern we write this comment
            ["M", "X", "S"],
        ],
        [
            ["S", "X", "M"],
            [
                "X",
                "A",
                "X",
            ],  # to keep auto format from messing up the pattern we write this comment
            ["S", "X", "M"],
        ],
        [
            ["S", "X", "M"],
            [
                "X",
                "A",
                "X",
            ],  # to keep auto format from messing up the pattern we write this comment
            ["S", "X", "M"],
        ],
    ]
    try:
        string = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        string[0][0] = data[y - 1][x - 1]
        string[0][2] = data[y - 1][x + 1]
        string[1][1] = data[y][x]
        string[2][0] = data[y + 1][x - 1]
        string[2][2] = data[y + 1][x + 1]
        print(string)
        if string in validPatterns:
            return True
        else:
            return False
    except IndexError:
        return False


count = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "A":
            if testForXmas(data, x, y):
                count += 1
print(count)
