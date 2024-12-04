data = []
with open("day 4/full.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        data.append(row)


def check_direction(data, x, y, dx, dy):
    steps = [(1, "M"), (2, "A"), (3, "S")]
    for step, char in steps:
        nx, ny = x + step * dx, y + step * dy
        if not (0 <= ny < len(data) and 0 <= nx < len(data[ny])):
            return False
        if data[ny][nx] != char:
            return False
    return True


count = 0
directions = {
    "R": (1, 0),  # Right
    "L": (-1, 0),  # Left
    "U": (0, -1),  # Up
    "D": (0, 1),  # Down
    "RU": (1, -1),  # Right Up
    "RD": (1, 1),  # Right Down
    "LU": (-1, -1),  # Left Up
    "LD": (-1, 1),  # Left Down
}

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "X":
            for direction, (dx, dy) in directions.items():
                if check_direction(data, x, y, dx, dy):
                    print(direction, y, x)
                    count += 1
print(count)
