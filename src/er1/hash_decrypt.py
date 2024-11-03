def foo(x):
    return (x + 1)/2

new_lines = []

with open('encrypted_file.txt', 'r') as f:
    for line in f.readlines():
        new_line = []
        codes = line.split(' ')
        for code in codes:
            if code != '\n':
                new_line.append(chr(int(foo(int(code)))))
        new_lines.append(new_line)
    
with open('decrypted_file.txt', 'w') as f:
    for line in new_lines:
        for element in line:
            f.write(element)
