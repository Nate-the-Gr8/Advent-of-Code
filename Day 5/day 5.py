import numpy as np


# solution dynamically expands the array when it needs to
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    area = np.zeros((100, 100), dtype="int16")
    for line in lines:
        coords = line.split(" -> ")
        coords = np.array([coords[0].split(","), coords[1].split(",")]).astype(int)
        if area.shape[0] < coords[:,0].max():
            area = np.pad(area, [(0, coords[:,0].max()-area.shape[0]), (0,0)], mode="constant")
        if area.shape[1] < coords[:,1].max():
            area = np.pad(area, [(0,0), (0, coords[:,1].max()-area.shape[1])], mode="constant")
        area[coords[:,0].min():coords[:,0].max(), coords[:,1].min():coords[:,1].max()] += 1
    print(area.size)
    print(area.size - area[area<2].size)
        
