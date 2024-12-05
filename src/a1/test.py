from binary_number import BinaryNumber

a = BinaryNumber('0110')
b = BinaryNumber('0101')

print(f'A = {a}')
print(f'B = {b}')
print(f'O inverso de A é {a.inverse()}')
print(f'O complemento de 2 de B é {b.complet_2()}')
print(f'A + B = {a + b}')
print(f'A - B = {a - b}')
print(f'B - A = {b - a}')
print(f'A & B = {a.and_bb(b)}')
print(f'A | B = {a.or_bb(b)}')
print(f'A ^ B = {a.xor_bb(b)}')

# Descomente as próximas linhas para testar a validação
#c = BinaryNumber('1200 13')