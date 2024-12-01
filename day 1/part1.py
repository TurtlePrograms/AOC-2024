leftList = []
rightList = []
with open("day 1/input1.txt") as f:
    for line in f:
        line = line.strip()
        values = line.split("   ")
        leftList.append(values[0])
        rightList.append(values[1])

leftList.sort()
rightList.sort()

distance = 0
for i in range(len(leftList)):
    distance += abs(int(leftList[i]) - int(rightList[i]))

print(leftList)
print(rightList)
print(distance)
