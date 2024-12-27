from vector import Vector

v = Vector([1, 2])
v2 = Vector([2, 3]).norm()
print(v2)
print(v * v2)
print(v2 * 1.6)
print(v.slide(v2))
