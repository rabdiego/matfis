"""
Nesse algoritmo de hash, implementei para apenas arquivos de texto:

Converto todos os caracteres para seus códigos ASCII, aplico então a verdadeira função de hash,
que escolhi uma que dá para achar a inversa, para decriptar o arquivo depois, e guardo em um arquivo
encriptado.
"""

def foo(x):
    return 2*x - 1

new_lines = []

with open('file.txt', 'r') as f:
    for line in f.readlines():
        new_line = []
        for character in line:
            new_line.append(foo(ord(character)))
        new_lines.append(new_line)
    

with open('encrypted_file.txt', 'w') as f:
    for line in new_lines:
        for element in line:
            f.write(f'{element} ')
        f.write('\n')