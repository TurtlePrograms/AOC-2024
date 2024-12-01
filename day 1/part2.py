leftList = []
rightList = []
with open("day 1/input2.txt") as f:
    for line in f:
        line = line.strip()
        values = line.split("   ")
        leftList.append(values[0])
        rightList.append(values[1])

simularity = 0
for i in range(len(leftList)):
    occurences = rightList.count(leftList[i])
    simularity += occurences * int(leftList[i])

print(simularity)
