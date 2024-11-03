"""
Plota N retângulos de 5x5 pixels de cores e posições aleatórias na tela, regenerando a cada 10 frames

O valor de N é determinado durante a chamada do script:

python random_numbers {N}
"""

import py5
from random import randint
from sys import argv

WIDTH, HEIGHT = 600, 600

n = int(argv[1])

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.rect_mode(py5.CENTER)
    py5.frame_rate(10)

def draw():
    py5.background(255)

    for i in range(n):
        rgb = [randint(0, 255) for _ in range(3)]
        xy = [randint(0, WIDTH-1), randint(0, HEIGHT-1)]

        py5.fill(rgb[0], rgb[1], rgb[2])
        py5.stroke_weight(0)
        py5.rect(xy[0], xy[1], 5, 5)

py5.run_sketch()