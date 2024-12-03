import re

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

total = 0
isEnabling = True

with open("day 3/full.txt") as f:
    for line in f:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                isEnabling = True
            elif match == "don't()":
                isEnabling = False
            elif isEnabling:
                values = match.split("(")[1].split(")")[0].split(",")
                total += int(values[0]) * int(values[1])


print(total)
