# Lexer Aritmético en Python

Autores: **Mauricio Emilio Monroy González**, **Amilka Daniela Lopez Aguilar**, **Maria Rivera Gutierres**  
Fecha de entrega: **10-04-2025**

---

## 📜 Descripción

Este proyecto implementa un **analizador léxico (lexer)** en Python, diseñado para identificar y clasificar los siguientes elementos dentro de un archivo fuente:

- Números enteros y reales
- Operadores aritméticos: suma (`+`), resta (`-`), multiplicación (`*`), división (`/`), potencia (`^`)
- Operadores lógicos y de asignación
- Variables (letras, mayúsculas, minúsculas y guiones bajos)
- Comentarios
- Strings entre comillas
- Paréntesis y otros puntadores

---

## ⚙️ Funcionamiento

El lexer utiliza una **tabla de transición de estados** para recorrer cada carácter del archivo de entrada y construir los tokens válidos.

- Lee el archivo especificado (`prueba.py`)
- Escanea carácter por carácter
- Usa la tabla de transición para cambiar de estado según el carácter léido
- Imprime cada token reconocido junto con su tipo

---

## 📋 Alfabeto Reconocido

- **Dígitos:** `0-9`
- **Operadores:** `+`, `-`, `*`, `/`, `**`, `=`, `+=`, `-=`, `==`, `<`, `>`, etc.
- **Puntadores:** `(){}[],:`
- **Variables:** Letras `A-Z`, `a-z`, y `_`
- **Notación científica:** `E`, `e`
- **Palabras clave de Python:** `if`, `else`, `while`, `def`, etc.
- **Funciones y valores especiales:** `int`, `float`, `input`, `True`, `False`, `None`
- **Comentarios:** `#`
- **Strings:** Comillas simples `'` y dobles `"`

---

## Color 
- Se subrayan las palabras o simbolos segun el tipo al que corresponden
