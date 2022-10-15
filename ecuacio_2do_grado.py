import math

ecuacion = """
Resolución de ecuaciones de segundo grado con la fórmula general. 
Si deseas empezar escribe Si: """
intro = str(input(ecuacion))

if intro == "Si" or intro == "si":
    a = int(input("Escribe el primer término de la expresión (si es negativo colocar signo) (ax2): "))
    b = int(input("Escribe el segundo término de la expresión (si es negativo colocar signo) (bx): "))
    c = int(input("Escribe el tercer término de la expresión (si es negativo colocar signo) (c): "))

    val_b = b * -1 #-b+-
    b2 = b**2 #potencia de b
    ri = -4*a*c #multiplicacion de a y c
    val_a = 2*a #multiplicacion del denominador

    rest = b2 + ri #resta
    rc = math.sqrt(rest)#raiz cuadrada

    res1 = (val_b + rc)/val_a #resultado de x con suma
    res2 = (val_b - rc)/val_a #resultado de x con resta

    print("Resultado x positivo. x =", round(res1,2))
    print("Resultado x negativo. x =", round(res2,2))
else:
    print("Hasta Luego")




