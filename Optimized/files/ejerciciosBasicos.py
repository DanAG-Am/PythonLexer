# Sección de Variables Globales
type_s = ""
type_c = ""
quant = 0

# Código comienza aquí
## Función ask() pide valores de usuario
def ask():
    # Variables locales
    pos_type_s = "bBeElL"
    pos_type_c = "nNfF"

    # Código comienza aquí
    global type_s 
    type_s = input("Tipo de silla? ")
    if type_s not in pos_type_s:
        print("Input inválido")
        type_s = input("Tipo de silla? ")   
    global type_c
    type_c = input("Tipo de cliente? ")
    if type_c not in pos_type_c:
        print("Input inválido")
        type_c = input("Tipo de cliente? ")
    global quant
    quant = int(input("Cantidad a comprar? "))
    # Fin de función

## Función calc() recibe entradas valores de ask() y procesa descuentos
def calc(type_s, type_c, quant):
    # Variables locales
    price_or = 0
    disc = 0
    price_disc = 0
    tot = 0
    
    # Código comienza aquí
    if type_s == "b" or type_s == "B":
        price_or = 700 * quant
        print(price_or)
    elif type_s == "e" or type_s == "E":
        price_or = 900 * quant
    elif type_s == "l" or type_s == "L":
        price_or = 1500 * quant
    if type_c == "n" or type_c == "N":
        if (price_or >= 10000) and (price_or < 20000):
            disc = 0.10
        elif (price_or >= 20000):
            disc = 0.15
    elif type_c == "f" or type_c == "F":
        disc = 0.2
    # Calcula outputs
    price_disc = disc * price_or
    tot = price_or - price_disc
    print(price_or, price_disc, tot)
    # Fin de función

## Función main() llama todo
def main():
  ask()
  calc(type_s, type_c, quant)
  # Fin de función

main()