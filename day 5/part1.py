import math

rules = []

foundAllRules = False
total = 0

with open("day 5/full.txt") as f:
    for line in f:
        if line.strip() == "":
            foundAllRules = True
            continue
        if not foundAllRules:
            ruleLine = line.strip().split("|")
            rule = (ruleLine[0].strip(), ruleLine[1].strip())
            rules.append(rule)
        else:
            values = line.strip().split(",")
            isGood = True
            for rule in rules:
                if rule[0] in values and rule[1] in values:
                    first = values.index(rule[0])
                    second = values.index(rule[1])
                    if first > second:
                        isGood = False
                        break
            if isGood:
                middle = values.__len__() // 2
                total += int(values[middle])
print(total)
