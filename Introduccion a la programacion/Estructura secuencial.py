'''
ESTRUCTURA SECUENCIAL
'''

#1.1
def opuesto_e_inverso(n):
    opuesto = -n
    inverso = 1/n
    return opuesto, inverso
print(opuesto_e_inverso(-8))

#1.2
def sueldo(v, h):
    sueldo = (v * (h * 5)) + (v * (h/2))
    return sueldo
print(sueldo(120, 8))

#1.3
def angulo(a1, a2):
    angulo = 180 - a1 - a2
    return angulo
print(angulo(40, 60))

#1.4
def operaciones(n1, n2):
    suma, resta, multiplicacion, division = n1 + n2, n1 - n2, n1 * n2, n1 / n2
    return suma, resta, multiplicacion, division
print(operaciones(3, 4))

#1.5
def promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio
print(promedio(3, 8, 2))

#1.6
def centigrados_a_fahrenheit(t):
    fahrenheit = (t * 1.8) + 32
    return fahrenheit
print(centigrados_a_fahrenheit(20))

#1.7
def main():
    print("Bienvenido a Vendedor")
    sueldo_mensual = 8000
    
    while True:
        rta_0 = input("Agregar un artículo: a / terminar: t\n")
        
        if rta_0 != "a" and rta_0 != "t":
            print("Escribí a o t según corresponda")
        
        elif rta_0 == "a":
            cantidad = float(input("Ingrese la cantidad vendida: "))
            precio = float(input("ingrese el precio unitario: "))
            sueldo_mensual = sueldo_mensual + ((cantidad * precio) * 0.14)
        
        else:
            print("El sueldo es:", sueldo_mensual) 
            break
main()

#1.8
def terreno(a, l, v):
    valor_terreno = (a * l) * v
    metros_alambre = ((a + l) * 2) * 3
    return valor_terreno, metros_alambre
print(terreno(20, 14, 1200))

#1.9
def home_deco(price):
    price1 = round(price * 0.9, 2)
    price2 = round(price * 1.1, 2)
    price3 = round(price * 1.15, 2)
    price4 = round(price * 1.25, 2)
    contado2 = round(price2 / 2, 2)
    contado3 = round(price3 / 4, 2)
    cuotas2 = round(price2 / 4, 2)
    cuotas3 = round((price3 - price3 / 4) / 5, 2)
    cuotas4 = round(price4 / 8, 2)
    print("Plan 1, contado:", price1)
    print("Plan 2, contado:", contado2, ". Y 2 cuotas de:", cuotas2)
    print("Plan 3, contado:", contado3, ", y 5 cuotas de:", cuotas3)
    print("Plan 4, 8 cuotas de:", cuotas4)
home_deco(100)

#1.10
def segundos(t):
    dias = int(t/86400)
    horas = int(int(t%86400)/3600)
    minutos = int(int(int(t%86400)%3600)/60)
    segundos = int(int(int(t%86400)%3600)%60)
    return "d:", dias, "h:", horas, "m:", minutos, "s:", segundos
print(segundos(1000000))

#1.11
def mayus(string):
    return string.upper()
print(mayus("hola bro"))

#1.12
def perimetro(m2):
    perimetro = round((m2**(1/2))*4, 2)
    return perimetro
print(perimetro(81))

#1.13
def dar_vuelta(a, b, c):
    dado_vuelta = f'{c} {b} {a}'
    length = len(a) + len(b) + len(c)
    return dado_vuelta, length
print(dar_vuelta("hola","como","andas"))

#1.14
def decimales(r1, r2):
    cociente = r1 / r2
    redondeado = round(r1 / r2)
    truncado = int(r1 / r2)
    return cociente, redondeado, truncado
print(decimales(3.2, 1.25))

#1.15
def pitagoras(c1, c2):
    hipotenusa = round((c1**2 + c2**2) ** (1/2), 2)
    return hipotenusa
print(pitagoras(3, 4))

#1.16
import random
def aleatorio(n):
    aleatorio = random.randint(1, n+1)
    return aleatorio
print(aleatorio(20))

#1.17
def oracion(string):
    oracion = string[0].upper() + string[1:].lower() + "."
    return oracion
print(oracion("nO te SalUdO pOrqUe Mi FamiLiA Es JuRiO"))

#1.18
def suma_cifras(string_number):
    suma = int(string_number[0]) + int(string_number[1]) + int(string_number[2])
    return suma
print(suma_cifras("123"))

'''
FIN
'''