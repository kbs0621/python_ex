import math
p1 = (0, 0)
p2 = (3, 4)

p1_1, p1_2 = p1
p2_1, p2_2 = p2

c1 = p2_1 - p1_1
c2 = p2_2 - p1_2

c = math.pow(c1, 2) + math.pow(c2, 2)
d = math.sqrt(c)

print(f"거리는 {d}")