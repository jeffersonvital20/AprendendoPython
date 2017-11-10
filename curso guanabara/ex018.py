import math
angulo = float(input('Qual o valor do ângulo?'))
cosa = math.cos(math.radians(angulo))
sena = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O cosseno é igual a {:.2f}, o seno é igual a {:.2f} e a tangente é {:.2f}'.format(cosa, sena, tan))