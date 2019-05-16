import math
points = [[3,3],[5,-1],[-2,4]]

def get_distance(coord):
    distance = math.sqrt(coord[0]**2 + coord[1]**2)
    return distance
length_list = []
for each in points:
    length_list.append(get_distance(each))
points = [x for _, x in sorted(zip(length_list, points))]
print(points)