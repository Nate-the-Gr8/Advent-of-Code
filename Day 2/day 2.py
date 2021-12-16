# Part 1
"""
with open("input.txt", "r", encoding="utf-8") as file:
    depth, horizontal = 0, 0
    for line in file.readlines():
        line = line.split()
        line = line[0], int(line[1])
        if line[0] == "forward":
            horizontal += line[1]
        elif line[0] == "down":
            depth += line[1]
        else:
            depth -= line[1]
print(depth*horizontal)
"""

# Part 2
# """
with open("input.txt", "r", encoding="utf-8") as file:
    depth, horizontal, aim = 0, 0, 0
    for line in file.readlines():
        line = line.split()
        line = line[0], int(line[1])
        if line[0] == "forward":
            horizontal += line[1]
            depth += aim*line[1]
        elif line[0] == "down":
            aim += line[1]
        else:
            aim -= line[1]
print(depth*horizontal) 
# """