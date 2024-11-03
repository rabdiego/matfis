from math import log2

class Set:
    def __init__(self, data: list) -> None:
        self.data = data.copy()
    

    def __str__(self) -> str:
        return self.data.__str__()
    

def set_union(s1: Set, s2: Set) -> Set:
    s3_data = s1.data.copy()

    for element in s2.data:
        if element not in s3_data:
            s3_data.append(element)
    
    return Set(s3_data)


def intersect(s1: Set, s2: Set) -> Set:
    s3_data = list()
    hs = dict()

    for element in s1.data:
        if element not in hs.keys():
            hs[element] = 0
        hs[element] += 1
    
    for element in s2.data:
        if element not in hs.keys():
            hs[element] = 0
        hs[element] += 1
    
    for key, value in hs.items():
        if value > 1:
            s3_data.append(key)
    
    return Set(s3_data)


def set_difference(s1: Set, s2: Set) -> Set:
    s3_data = s1.data.copy()

    for element in s2.data:
        if element in s3_data:
            s3_data.remove(element)
    
    return Set(s3_data)


def cartesian_product(s1: Set, s2: Set) -> Set:
    s3_data = [s1.data.copy(), s2.data.copy()]
    return Set(s3_data)


def power_set(s: Set) -> Set:
    ps = [[]]

    for element in s.data:
        nss = [ss + [element] for ss in ps]
        ps.extend(nss)
    
    return Set(ps)


a = Set([2, 0, 3, 1, 4, 8])
b = Set([2, 0, 1, 6, 3])
c = Set([1, 5, 4])

print(f'Conjunto A: {a}')
print(f'Conjunto B: {b}')
print(f'União de A com B: {set_union(a, b)}')
print(f'Intersseção de A com B: {intersect(a, b)}')
print(f'Diferença de A com B: {set_difference(a, b)}')
print(f'Diferença de B com A: {set_difference(b, a)}')
print(f'Produto cartesiano de A com B: {cartesian_product(a, b)}')
print(f'Conjunto das partes de C: {power_set(c)}')