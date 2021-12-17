from functools import partial


# Part 1
"""
with open("input.txt", "r", encoding="utf-8") as file:
    gamma, epsilon = "", ""
    lines = file.readlines()
    for column in range(len(lines[0])-1):
        mostcommon = sum([int(line[column]) for line in lines])
        if mostcommon > len(lines)/2:
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
    o2key, co2key = "", ""
    file = " " + " ".join(lines)
    for column in range(len(lines[0])-1):
        mostcommon = sum([int(line[column]) for line in lines])
        if mostcommon >= len(lines)/2:
            o2key += "1"
            co2key += "0"
        else:
            o2key += "0"
            co2key += "1"
        if file.count(" " + o2key) == 1:
            o2filter = lines[file.find(" " + o2key)//(len(lines[0])+1)]
        if file.count(" " + co2key) == 1:
            co2filter = lines[file.find(" " + co2key)//(len(lines[0])+1)]
print(int(o2filter, 2)*int(co2filter, 2))
# """
