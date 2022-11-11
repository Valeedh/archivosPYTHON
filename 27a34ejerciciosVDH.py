#ejercicio27
num=float(input("escribe un numero con muchos decimales:"))
print(num*2)

#ejercicio28
num=float(input("escribe un numero con muchos decimales:"))
respuesta=num*2
print(respuesta)
print(round(respuesta,2))

#ejercicio29
import math
num=int(input("escribe un numero mayor a 500:"))
respuesta=math.sqrt(num)
print(round(respuesta,2))

#ejercicio30
import math
print(round(math.pi,5))

#ejercicio32
import math
radio=int(input("escribe el radio de un circulo:"))
profundidad=int(input("escribe la profundidad:"))
area=math.pi(radio**2)
volumen=area*profundidad
print(round(volumen,3))

#ejercicio33
num1=int(input("escribe un numero:"))
num2=int(input("escribe otro numero:"))
respuesta1=num1//num2
respuesta2=num1%num2
print(num1, "dividido por", num2, "is," respuesta1, "con", respuesta 2, "sobrante")

#ejercicio34
print ("1) cuadrado")
print ("2) Triangulo")
print ()
menuselection = int (input ("introduce un numero:") )
if menuselection == 1:
side = int (input ("Introduce longitud de un lado:"))
area = side*side
print ("El area de tu eleccion es", area)
elif menuselection == 2:
base = int (input ("Introducir longitud de base:"))
height = int (input ("Introduce altura del triangulo:"))
area = (base*height)/2
print ("El area de tu eleccion es",area)
else:
print ("Selección de opción de incorrecta")