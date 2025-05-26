print("Introduce la edad del aplicante")
edad = input()
edad = int(edad)
valido1 = False
valido2 = False
while (valido1 == False):
    edad = input()
    edad = int(edad)
    if (edad < 18):
        print("La edad del aplicante no es suficiente.")
        edad = input()
        edad = int(edad)
    elif (edad > 18): 
        print ("La edad es suficiente. ¿Trae consigo una identificación oficial? Escriba 'Sí' o 'No'")
        valido1 = True
    elif (edad == 18):
        print ("La edad es suficiente. ¿Trae consigo una identificación oficial? Escriba 'Sí' o 'No'")
        valido1 = True
id = input()
while (valido2 == False):
    if (id == "Sí"):
        valido2 = True
        print("El candidato está aprobado para su licencia de conducir")
    else:
        print("El aplicante debe traer consigo una identificación para poder ser aprobado. Regrese cuando la tenga.")
        print("¿Trae consigo una identificación oficial? Escriba 'Sí' o 'No'")
        id = input()