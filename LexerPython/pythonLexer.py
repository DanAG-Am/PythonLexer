'''
Autores: Mauricio Emilio Monroy González, Amilka Daniela Lopez Aguilar, Maria Rivera Gutierres
## Fecha de entrega: 10-4-2025

## Descripción: Lexer Aritmético que reconoce enteros, reales, suma, resta, multiplicación, división, asignación, potencia y variables.
'''
#--------------------------

#Tabla de Transición
#d: digitos, 1: suma, 2: resta, 3: *=^, 4: /, 5: Ee, 6: ., 7:() , 8: A-Z, 9: a-z, 10: _, 11:\n , 12: setX
tabla = [
    [1, 9, 12, 6, 14, 6, 14, 9, 7, 5, 2, 2, 14, 14],
    [1, 8, 8, 8, 3, 4, 8, 8, 8, 8, 8, 8, 8, 14],
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 14],
    [3, 8, 8, 8, 14, 4, 8, 8, 8, 8, 8, 8, 8, 14],
    [3, 14, 14, 14, 14, 14, 14, 14, 14, 3, 3, 14, 14, 14],
    [5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 14],
    [6, 14, 11, 6, 14, 6, 11, 11, 14, 14, 14, 14, 11, 14],
    [7, 7, 7, 7, 7, 7, 14, 7, 13, 7, 7, 7, 7, 14]
]

##Subconjuntos de alfabeto 
blanco = '\b \t \n $'
nums = '0123456789'
operadores = [
    '/', '**', '%', '==', '+=', '-=', '*=', '//', '<','>', '!=',
    '<=', '>=', '&', '|', '^', 'and', 'not', 'or', '+', '-', '*', '='
]

sciNot = 'Ee'
puntadores = '(){}[],:'
var = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
palabras = [
  'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

especiales = ['float', 'int', 'len', 'str', 'input', 'True', 'False', 'None']
comillas = ['"',"'", ':']
# --------------------
# Definción de funcíon
def pythonLexer (archivo):
    # Lectura de archivo
    file = open(archivo, 'r')
    s = file.read()
    file.close()
    s += '$' 
    #print("File Read:\n", s)
    print("|---------------------------------------------|")
    print("|         Token        |         Tip3o         |") 
    print("|---------------------------------------------|")
    state = 0
    pos = 0
    lex = ''

#Escaneo de todos los caracteres en string de archivo
    while (s[pos] != '$' or (s[pos] == '$' and state != 0)) and state != 14:
        c = s[pos]
        # Selección de columna correspondiente a caso leído
        if c in nums: 
            col = 0
        elif c in operadores:
            col = 1
        elif c in puntadores:
            col = 2
        elif c in var:
            col = 3
        elif c == '.': 
            col = 4
        elif c in sciNot:
            col = 5
        elif c =='\n': 
            col = 6
        elif c == '=': 
            col = 7
        elif c in comillas:
            col = 8
        elif c == '#':
            col = 9
        elif c == '+':
            col = 10
        elif c == '-': 
            col = 11
        elif c in blanco:
            col = 12
        else:
            col = 13
        #print("charac", c, "row:", state, ", col: ", col)
        state = tabla[state][col]
        #print("state:", state, ", col: ", col, ", c: ", c, ", lex:", lex)
        if state == 8:  # Caso de enteros
            print ("|", lex, "       |        NUMEROS  |")
            lex = ''
            state = 0
            pos -=1
        elif state == 9: # Caso de reales
            print ("|", c, "       |        OPERADORES  |")
            lex = ''
            state = 0
            #pos -=1
        elif state == 10:
            print ("|", lex, "       |        COMENTARIOS  |")
            lex = ''
            state = 0
            pos -=1
        elif state == 11:
            print ("|", lex, "       |        TOKEN |")
            lex = ''
            state = 0
            pos -=1
        elif state == 12:
            print ("|", c, "       |       PUNTADORES  |")
            lex = ''
            state = 0
            #pos -=1
        elif state == 13:
            if c in comillas:
                lex += c  # agrega la comilla final
                print("|", lex.ljust(20), "|", "STRING".ljust(20), "|")
                lex = ''
                state = 0
            else:
                lex += c

        elif state == 14:
            lex = ''
            state = 0
            #pos -=1
        
        pos += 1  # Avanzar a siguiente índice de string
        if(pos >= len(s)):
            break  
        if state != 0: # Concatenar caracter a lexema si es estado intermedio 
            lex += c
print("|---------------------------------------------|")

# -----------------------

pythonLexer("prueba.py")
