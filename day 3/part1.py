import re

pattern = r"mul\(\d+,\d+\)"
total = 0
with open("day 3/input1.txt") as f:
    for line in f:
        matches = re.findall(pattern, line)
        for match in matches:
            values = match.split("(")[1].split(")")[0].split(",")
            total += int(values[0]) * int(values[1])

print(total)
