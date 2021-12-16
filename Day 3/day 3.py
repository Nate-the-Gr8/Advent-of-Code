# Part 1
"""
with open("input.txt", "r", encoding="utf-8") as file:
    gamma, epsilon = "", ""
    lines = file.readlines()
    for column in range(len(lines[0])-1):
        mostcommon = sum([int(line[column]) for line in lines])
        if mostcommon > 500:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
print(int(gamma, 2)*int(epsilon, 2))
"""

# Part 2
# """
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    o2 = max(set(lines), key=lines.count)
    co2 = min(set(lines), key=lines.count)
print(int(o2, 2)*int(co2, 2))


    
# print(int(gamma, 2)*int(epsilon, 2))
# """