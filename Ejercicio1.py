#Inicializacion, variables, print y type:
print("hola mundo")
## comentarios para que a mi me de una idea de que es lo q estoy haciendo: documentando
""" varios comandos o lineas - comilla doble o triple al inicio """

## booleanos resultado de operaciones logicas True= 1 False = 0, cualquier valor diferente
##de cero lo toma como valor. NUMEROS - CADENAS DE TEXTO - BOOLEANOS

## Numericos: enteros, decimales(float), numeros complejos (plano: vectores) - parte real y parte imaginaria
## CLASES: nombres de datos en python: enteros - int, decimales - float , complejos - complex, texto - str, booleanos - bool


## el interprete le pone el tipo de dato 

num1 = 9
num2 =  16
num3 = 5.6
num4 = 5+8j
texto1 = "Hola mundo"
texto2 = "IDSA"
flag1 = True
flag2 = False
num2 = "casa"

print() ## salto de linea
##
print("DATOS", end = " ")
print("num1:", num1)
print(num2, type(num2))
print(num3, type(num3))
print(num4), type(num4)
print(texto1)
print(texto2)
print(flag1, type(flag1))
print(flag2)

print(type(num1))

print( "hola" + "que" + "tal", num1)
texto3 =  "hola" + "que" + "tal"
print(texto3)