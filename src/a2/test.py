from vector import Vector

v1 = Vector([1.0, 0.0, -3.0])
v2 = Vector([-5.0, 2.0, 1.0])
u =  Vector([1.0, 1.0, 0.0]).norm()

print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v1 + v2 = {v1 + v2}')
print(f'v1 - v2 = {v1 - v2}')
print(f'-v1 = {-v1}')
print(f'2*v1 = {v1 * 2}')
print(f'v1 . v2 = {v1 * v2}')
print(f'v1 x v2 = {v1.cross(v2)}')
print(f'v2 x v1 = {v2.cross(v1)}')
print(f'v1 projetado em v2 = {v1.project(v2)}')
print(f'v1 refletido em v2 = {v1.reflect(v2)}')
print(f'u = {u}')
print(f'componente de v1 deslizando em u = {v1.slide(u)}')
