menu = """
Bienvenidos al convertidor de monedas
Escribe el número de la unidad que deseas hacer la conversión:
1 - Peso colombiano
2 - Peso mexicano
3 - Colon costarricense
4 - Sol peruano
5 - Peso chileno
6 - Córdoba nicaraguense
Escribe una opción: """

selec = int(input(menu))
if selec == 1:
    uni = int(input("Ahora dime, ¿Quieres cambiar de Pesos colombianos a Dólar(1) o de Dólar a Pesos Colombianos(2)? Por favor escribe la opcíon que desees: "))
    if uni == 1:
        p_col = float(input("Dime cuantos pesos colombianos deseas cambiar: "))
        val_dol = 3875
        conv= float(p_col/val_dol)
        print("Tu conversión de pesos a dólares es de: $", round(conv, 2))
    elif uni == 2:
        dol = float(input("Dime cuantos dólares deseas cambiar: "))
        val_col = 0.00022
        conv = float(dol/val_col)
        print("Tu conversión de dólares a pesos es de: ", round(conv, 2), "COL$")
    else: 
        print("Opcíon no válida, por favor selecciona una opción válida")

