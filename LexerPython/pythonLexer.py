'''
Autores: Mauricio Emilio Monroy González, Amilka Daniela Lopez Aguilar, Maria Rivera Gutierres
## Fecha de entrega: 10-4-2025

## Descripción: Lexer Aritmético que reconoce enteros, reales, suma, resta, multiplicación, división, asignación, potencia y variables.
'''
#--------------------------

#Tabla de Transición
#d: digitos, 1: suma, 2: resta, 3: *=^, 4: /, 5: Ee, 6: ., 7:() , 8: A-Z, 9: a-z, 10: _, 11:\n , 12: setX

tabla = [
    [1, 9, 12, 6, 14, 6, 15, 9, 7, 5, 2, 2, 15, 14],  # State 0
    [1, 8, 8, 8, 3, 4, 8, 8, 8, 8, 8, 8, 8, 14],      # State 1
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 14],      # State 2
    [3, 8, 8, 8, 14, 4, 8, 8, 8, 8, 8, 8, 8, 14],     # State 3
    [3, 14, 14, 14, 14, 14, 14, 14, 14, 3, 3, 14, 14, 14],  # State 4
    [5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 14],     # State 5
    [6, 14, 11, 6, 14, 6, 11, 11, 14, 14, 14, 14, 11, 14],  # State 6
    [7, 7, 7, 7, 7, 7, 14, 7, 13, 7, 7, 7, 7, 14],     # State 7
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]  # State 15 (Spaces/Newlines)
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
 'nonlocal', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield'
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

    # Estructura HTML inicial
    html_output = '<html><head><style>'
    html_output += '''
    body { background-color: black; color: white; }
    .keyword { color: goldenrod; font-weight: bold; }
    .special { color: lightpink; }
    .variable { color: lightblue; }
    .operator { color: white; }
    .number { color: lightgreen; }
    .comment { color: green; font-style: italic; }
    .string { color: lightcoral; }
    .punctuation { color: yellow; }
    .error { text-decoration: underline wavy red; color: red; }
    pre { white-space: pre-wrap; } /* Preserva espacios y saltos de línea */
    '''
    html_output += '</style></head><body><pre>'



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
        elif c == '.': 
            col = 4
        elif c in sciNot:
            col = 5
        elif c in var:
            col = 3
        elif c =='\n': 
            col = 6
        elif c == '=': 
            col = 7
        elif c in comillas:
            col = 8
        elif c == '#':
            col = 9
        elif c in blanco:
            col = 12
        else:
            col = 13
        print("charac", c, "row:", state, ", col: ", col)
        state = tabla[state][col]
        print("state:", state, ", col: ", col, ", c: ", c, ", lex:", lex)
        if state == 8:  # Caso de enteros
            print ("|", lex, "       |        NUMEROS  |")
            html_output += f'<span class="number">{lex}</span>'
            lex = ''
            state = 0
            pos -=1
        elif state == 9: # Caso de reales
            print ("|", c, "       |        OPERADORES  |")
            html_output += f'<span class="operator">{c}</span>'
            lex = ''
            state = 0
            #pos -=1
        elif state == 10:
            print ("|", lex, "       |        COMENTARIOS  |")
            html_output += f'<span class="comment">{lex}</span>'
            lex = ''
            state = 0
            pos -=1
        elif state == 11:
            if(lex in palabras):
                print ("|", lex, "       |    KEYWORD |")
                html_output += f'<span class="keyword">{lex}</span>'
            elif(lex in especiales):
                print("|", lex, "       |    ESPECIAL |")
                html_output += f'<span class="special">{lex}</span>'
            else: 
                print("|", lex, "       |    VARIABLE |")
                html_output += f'<span class="variable">{lex}</span>'
            lex = ''
            state = 0
            pos -=1
        elif state == 12:
            print ("|", c, "       |       PUNTADORES  |")
            html_output += f'<span class="punctuation">{c}</span>'
            lex = ''
            state = 0
            #pos -=1
        elif state == 13:
            if c in comillas:
                lex += c  # agrega la comilla final
                print("|", lex.ljust(20), "|", "STRING".ljust(20), "|")
                html_output += f'<span class="string">{lex}</span>'
                lex = ''
                state = 0
            else:
                lex += c
        elif state == 14:  # Caso de error o token inválido
            print("|", lex.ljust(20), "|", "ERROR".ljust(20), "|")  # Imprimir el error en consola
            html_output += f'<span class="error">{lex}</span>'  # Agregar el error al HTML con estilo
            lex = ''  # Reiniciar el lexema
            state = 0  # Reiniciar el estado
        elif state == 15:  # Caso de espacios y saltos de línea
            if c == '\n':  # Manejo de saltos de línea
                html_output += '<br>'  # Agregar un salto de línea en HTML
                print("|", "\\n".ljust(20), "|", "NEWLINE".ljust(20), "|")
            elif c in blanco:  # Manejo de espacios
                html_output += '&nbsp;'  # Agregar un espacio en HTML
                print("|", " ".ljust(20), "|", "SPACE".ljust(20), "|")
            lex = ''
            state = 0
        print("Loop end | state:", state, ", col: ", col, ", c: ", c, ", lex:", lex)
        pos += 1  # Avanzar a siguiente índice de string
        if(pos >= len(s)):
            break  
        if state != 0: # Concatenar caracter a lexema si es estado intermedio 
            lex += c
    print("|---------------------------------------------|")
    html_output += '</pre></body></html>'
    with open('output.html', 'w') as html_file:
        html_file.write(html_output)


# -----------------------

pythonLexer(r"C:\Users\mauri\OneDrive\Documents\Programacion\Python programs\PythonLexer\LexerPython\prueba.py")
