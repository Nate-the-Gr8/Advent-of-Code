# Part 1
"""
with open("input.txt", "r", encoding="utf-8") as file:
    increment_count = -1
    previous_line = 0
    for line in file.readlines():
        line = int(line)
        if line > previous_line:
            increment_count += 1
        previous_line = line
print(increment_count)
"""

"""
with open("C:\\Users\\natha\\Desktop\\Python\\Advent-of-Code\\Day 1\\input.txt", "r", encoding="utf-8") as file:
    data = [int(line) for line in file.read().splitlines()]
    increment_count, last = -1, 0
    for i, value in enumerate(data):
        try:
            current = value + data[i+1] + data[i+2]
            if current > last:
                increment_count += 1
            last = current
        except IndexError:
            break
print(increment_count)
"""