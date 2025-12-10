'''
# Ejercicio 3: Mínimo, máximo y cambio de tipos

1. Declara una variable base como un número entero.
2. Declara otra variable multiplicador como un float.
3. Calcula los siguientes valores:
   - op1 = base ** 2
   - op2 = multiplicador * base / 2
   - op3 = base // 2
    - op4 = float(base)
4. Crea dos variables: valor_min y valor_max, que sean el mínimo y el máximo de (op1, op2, op3, op4).
5. Muestra en pantalla valor_min y valor_max, junto con su tipo usando type().
'''

base = 2
multiplicador = 3.

op1 = base ** 2
op2 = multiplicador * base / 2
op3 = base // 2
op4 = float(base)

valor_min = 100
valor_max = -100

for i in (op1, op2, op3, op4):
    if (i < valor_min):
        valor_min = i
    if (i > valor_max):
        valor_max = i

print(valor_min)
print(valor_max)