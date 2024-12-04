data = []
with open("day 4/full.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        data.append(row)


def testForXmas(data, x, y):
    validPatterns = ["MMASS", "SSAMM", "MSAMS", "SMASM"]
    try:
        string = ""
        string += data[y - 1][x - 1]
        string += data[y - 1][x + 1]
        string += data[y][x]
        string += data[y + 1][x - 1]
        string += data[y + 1][x + 1]
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
