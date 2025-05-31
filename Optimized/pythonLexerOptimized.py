import os
from multiprocessing import Process
import time 

'''
Autores: Mauricio Emilio Monroy González, Amilka Daniela Lopez Aguilar, Maria Rivera Gutierres
## Fecha de entrega: idk no ha dicho el profe o sí?

## Descripción: Lexer para programa en Python que reconoce números, operadores, puntadores, variables, comentarios, palabras clave, y strings.
    Después de categorizar el token, se imprime en consola y se genera un archivo HTML con el resultado coloreado según su categoría. 
    .keyword { color: goldenrod; font-weight: bold; }
    .special { color: lightpink; }
    .variable { color: lightblue; }
    .operator { color: white; }
    .number { color: lightgreen; }
    .comment { color: green; font-style: italic; }
    .string { color: lightcoral; }
    .punctuation { color: yellow; }
    .error { text-decoration: underline wavy red; color: red; }
    pre { white-space: pre-wrap; } /* Preserva espacios y saltos de línea     
'''
#--------------------------

#Tabla de Transición
tabla = [
    [1, 9, 12, 6, 14, 6, 15, 9, 7, 5, 2, 2, 15, 14],
    [1, 8, 8, 8, 3, 4, 8, 8, 8, 8, 8, 8, 8, 14], 
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 14], 
    [3, 8, 8, 8, 14, 4, 8, 8, 8, 8, 8, 8, 8, 14],
    [3, 3, 14, 14, 14, 14, 14, 14, 14, 3, 3, 14, 14, 14],
    [5, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 5, 14],     
    [6, 14, 11, 6, 14, 6, 11, 11, 14, 14, 14, 14, 11, 14], 
    [7, 7, 7, 7, 7, 7, 14, 7, 13, 7, 7, 7, 7, 14],
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
]

##Subconjuntos de alfabeto 
blanco = '\b \t \n $'
nums = '0123456789'
operadores = [
    '/', '**', '%', '==', '+=', '-=', '*=', '//', '<','>', '!=',
    '<=', '>=', '&', '|', '^', 'and', 'not', 'or', '+', '-', '*', '='
]
sciNot = 'Ee'
puntadores = '(){}[],:.'
var = '\@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"'\
      'áéíóúüñÁÉÍÓÚÜÑàèìòùâêîôûãõäëïöüÿ¿?!¡'
palabras = [
  'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield',
 'append', 'randint',
]
especiales = ['float', 'int', 'len', 'str', 'input', 'True', 'False', 'None', 'append','randit']
comillas = ['"',"'",":"]


# --------------------
# Definción de funcíon
def pythonLexer (archivo, output_html='output.html'):
    # Lectura de archivo
    file = open(archivo, 'r',  encoding='utf-8') #abrir con unicode para solucionar problemas con las tildes que puedan aparecer en maquinas en particular https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
    s = file.read()
    file.close()
    s += '$' 
    #print("File Read:\n", s)
    print("|---------------------------------------------|")
    print("|         Token        |         Tip3o         |") 
    print("|---------------------------------------------|")

    # Estructura HTML inicial a la cual concatenar resultados formateados
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
        elif c == '+':
            col = 10
        elif c == '-':
            col = 11
        elif c in blanco:
            col = 12
        else:
            col = 13
        print("charac", c, "row:", state, ", col: ", col)
        state = tabla[state][col]
        print("state:", state, ", col: ", col, ", c: ", c, ", lex:", lex)
        if state == 8:  # Caso para números, reales o enteros
            print ("|", lex, "       |        NUMEROS  |")
            html_output += f'<span class="number">{lex}</span>'
            lex = ''
            state = 0
            pos -=1
        elif state == 9: # Manejo de operadores
            print ("|", c, "       |        OPERADORES  |")
            html_output += f'<span class="operator">{c}</span>'
            lex = ''
            state = 0
            #pos -=1
        elif state == 10: # Manejo de comentarios
            print ("|", lex, "       |        COMENTARIOS  |")
            html_output += f'<span class="comment">{lex}</span>'
            lex = ''
            state = 0
            pos -=1
        elif state == 11: # Manejo de literales: palabras clave o variables
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
        elif state == 12: # Manejo de símbolos especiales
            print ("|", c, "       |       PUNTADORES  |")
            html_output += f'<span class="punctuation">{c}</span>'
            lex = ''
            state = 0
            #pos -=1
        elif state == 13: # Manejo de cadenas de texto
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
        #print("Loop end | state:", state, ", col: ", col, ", c: ", c, ", lex:", lex)
        pos += 1  # Avanzar a siguiente índice de string
        if(pos >= len(s)):
            break  
        if state != 0: # Concatenar caracter a lexema si es estado intermedio 
            lex += c
    print("|---------------------------------------------|")
    html_output += '</pre></body></html>'
    with open(output_html, 'w', encoding="utf-8") as html_file:
        html_file.write(html_output)


# -----------------------
# Old function call for testing per file
# pythonLexer(r"C:\Users\mauri\OneDrive\Documents\Programacion\Python programs\PythonLexer\LexerPython\prueba.py")

# Función helper
def procesar_archivo(ruta_py, ruta_html):
    pythonLexer(ruta_py, ruta_html)

if __name__ == "__main__":
    # 1. Carpeta a analizar, utilizamos paths absolutos para independencia de maquina 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(script_dir, "files")

    
    # 2. Listar todos los archivos .py
    archivos_py = [f for f in os.listdir(folder) if f.endswith(".py")]
    
    procesos = []
    startTime = time.perf_counter()
    for archivo in archivos_py:
        ruta_py = os.path.join(folder, archivo)
        nombre_html = os.path.splitext(archivo)[0] + ".html"
        ruta_html = os.path.join(folder, nombre_html)
        p = Process(target=procesar_archivo, args=(ruta_py, ruta_html))
        p.start()
        procesos.append(p)
    
    for p in procesos:
        p.join()
        
    endTime = time.perf_counter()
    print(f"Tiempo total de procesamiento: {endTime - startTime:.2f} segundos")
    print("All files processed and colored. ~ 100/100 ~ ")