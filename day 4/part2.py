data = []
with open("day 4/full.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        data.append(row)


def testForXmas(data, x, y):
    patterns = [
        [("M", -1, -1), ("S", -1, 1), ("M", 1, -1), ("S", 1, 1)],
        [("S", -1, -1), ("M", -1, 1), ("S", 1, -1), ("M", 1, 1)],
        [("M", -1, -1), ("M", -1, 1), ("S", 1, -1), ("S", 1, 1)],
        [("S", -1, -1), ("S", -1, 1), ("M", 1, -1), ("M", 1, 1)],
    ]

    try:
        if data[y][x] != "A":
            return False

        for pattern in patterns:
            if all(data[y + dy][x + dx] == char for char, dy, dx in pattern):
                return True

        return False
    except IndexError:
        return False


count = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "A":
            if testForXmas(data, x, y):
                print(testForXmas(data, x, y), y, x)
                count += 1
print(count)
