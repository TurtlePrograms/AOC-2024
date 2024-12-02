data = []


def up(row):
    for i in range(len(row) - 1):
        if row[i] > row[i + 1]:
            return False
        diff = abs(row[i] - row[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def down(row):
    for i in range(len(row) - 1):
        if row[i] < row[i + 1]:
            return False
        diff = abs(row[i] - row[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def isSave(row):
    if row[0] < row[1]:
        return up(row)
    else:
        return down(row)


with open("day 2/input1.txt") as f:
    for line in f:
        chars = line.strip().split()
        data.append(chars)

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

saveCount = 0
for i in range(len(data)):
    if isSave(data[i]):
        saveCount += 1

print(saveCount)
