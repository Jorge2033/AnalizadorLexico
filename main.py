import ply.lex as lex
import datetime
import os

# ------Inicio: Jorge Gaibor (Palabras Reservadas) ------
reserved = {
    'let': 'LET',
    'const': 'CONST',
    'var': 'VAR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'class': 'CLASS',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'try': 'TRY',
    'catch': 'CATCH',
    'finally': 'FINALLY',
    'throw': 'THROW',
    'new': 'NEW',
    'this': 'THIS',
    'super': 'SUPER',
    'typeof': 'TYPEOF',
    'instanceof': 'INSTANCEOF',
    'in': 'IN',
    'void': 'VOID',
    'delete': 'DELETE',
    'export': 'EXPORT',
    'import': 'IMPORT',
    'as': 'AS',
    'from': 'FROM',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
}
# ------Fin: Jorge Gaibor (Palabras Reservadas) ------

tokens = (
    'VARIABLE',
    'NUMBER',
    # ------Inicio: José Ramos (Operadores Aritméticos) ------
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO',
    'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTIPLY_ASSIGN', 'DIVIDE_ASSIGN', 'MODULO_ASSIGN',
    # ------Fin: José Ramos (Operadores Aritméticos) ------
    # ------Inicio: José Ramos (Operadores Booleanos) ------
    'EQUAL', 'STRICT_EQUAL', 'NOT_EQUAL',
    'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL',
    'AND', 'OR', 'NOT',
    # ------Fin: José Ramos (Operadores Booleanos) ------
    # ------Inicio: Jorge Gaibor (Delimitadores) ------
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'DOT', 'COLON', 'QUESTION_MARK',
    # ------Fin: Jorge Gaibor (Delimitadores) ------
    # ------Inicio: Julio Vivas (Tipos de Variables) ------
    'ASSIGN'
    # ------Fin: Julio Vivas (Tipos de Variables) ------
) + tuple(reserved.values())

# ------Inicio: José Ramos (Expresiones Regulares Operadores Aritméticos) ------
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULO_ASSIGN = r'%='
# ------Fin: José Ramos (Expresiones Regulares Operadores Aritméticos) ------

# ------Inicio: Jorge Gaibor (Delimitadores) ------
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_QUESTION_MARK = r'\?'
# ------Fin: Jorge Gaibor (Delimitadores) ------

# ------Inicio: José Ramos (Expresiones Regulares Operadores Booleanos) ------
t_EQUAL = r'=='
t_STRICT_EQUAL = r'==='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
# ------Fin: José Ramos (Expresiones Regulares Operadores Booleanos) ------

# ------Inicio: Julio Vivas (Expresiones Regulares Tipos de Variables) ------
t_ASSIGN = r'='
# ------Fin: Julio Vivas (Expresiones Regulares Tipos de Variables) ------

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Identifica palabras reservadas primero
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Token no admitido '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# ------Sección de Pruebas ------
prueba_jose = """
variable1 == 10 && variable2 <= 30 || variable3 != variable4;
x += 5;
y === 12;
"""

prueba_jorge = """
var total = 20 + 5 * (10 - 3);
let resultado = total >= 30 ? "Aprobado" : "Reprobado";
const mensaje = "Resultado final:";
function calcular(x, y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
"""

prueba_julio = """
let resultado = 10 + 20;
const MAX_VALOR = 100;
var variableGlobal = 50;

class Calculadora {
    static PI = 3.1415;
    calcularArea(radio) {
        let area = Calculadora.PI * radio * radio;
        return area >= 50 ? "Grande" : "Pequeña";
    }
}

if (resultado > MAX_VALOR) {
    console.log("Excedió el límite");
} else {
    console.log("Dentro del rango");
}
"""

# Generar el nombre del archivo log
usuario_git = input("Por favor, ingresa tu nombre de usuario: ")
timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)  # Crea la carpeta 'logs' si no existe
log_filename = os.path.join(log_directory, f"lexico-{usuario_git}-{timestamp}.txt")

with open(log_filename, 'w') as log_file:
    log_file.write("Tokens reconocidos:\n")
    lexer.input(prueba_julio)

    while True:
        tok = lexer.token()
        if not tok:
            break
        log_file.write(f"{repr(tok)}\n")

print(f"El análisis léxico se ha guardado en el archivo {log_filename}")
