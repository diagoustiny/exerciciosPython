# import math
from math import radians, sin, cos

angulo = float(input("Digite um angulo que deseja saber o seu seno e coseno \n "))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
print("O seno de {} é {:.2f} e 0 coseno é {:.2f}".format(angulo, seno, coseno))
