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
    o2, co2 = lines, lines
    file = " " + " ".join(lines)
    for column in range(len(lines[0])-1):
        o2mostcommon = sum([int(line[column]) for line in o2])
        co2mostcommon = sum([int(line[column]) for line in co2])
        if o2mostcommon >= len(o2)/2:
            o2key += "1"
        else:
            o2key += "0"
        if co2mostcommon >= len(co2)/2:
            co2key += "0"
        else:
            co2key += "1"
        o2 = list(filter(lambda data: data[:len(o2key)] == o2key, o2))
        co2 = list(filter(lambda data: data[:len(co2key)] == co2key, co2))
        if len(o2) == 1:
            o2filter = o2[0]
        if len(co2) == 1:
            co2filter = co2[0]
print(int(o2filter, 2)*int(co2filter, 2))
# """
