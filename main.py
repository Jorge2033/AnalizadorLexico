import ply.lex as lex
import ply.yacc as yacc
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
    'print': 'PRINT',
}
# ------Fin: Jorge Gaibor (Palabras Reservadas) ------

tokens = (
    'VARIABLE', 'NUMBER', 'STRING',
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

t_STRING = r'\".*?\"'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')  # Verifica si es una palabra reservada
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Token no admitido '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
# ------Fin: Reglas Léxicas------

# ------Inicio: Reglas Sintácticas por Jorge Gaibor ------
def p_program(p):
    '''program : statements'''
    pass

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    pass

def p_statement(p):
    '''statement : print
                 | structure_declaration'''
    pass

def p_print(p):
    '''print : PRINT LPAREN arguments RPAREN SEMICOLON'''
    pass

def p_arguments(p):
    '''arguments : argument
                 | argument COMMA arguments'''
    pass

def p_argument(p):
    '''argument : STRING
                | VARIABLE'''
    pass

def p_structure_declaration(p):
    '''structure_declaration : CLASS VARIABLE LBRACE statements RBRACE'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' línea {p.lineno}")
    else:
        print("Error de sintaxis en el final del archivo")
# ------Fin: Reglas Sintácticas por Jorge Gaibor ------

parser = yacc.yacc()

# ------Inicio: Prueba de Jorge Gaibor ------
prueba_jorge_sintactico = '''
print("Inicio del programa");
class Vehiculo {
    constructor(marca, modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    mostrarInfo() {
        print("Marca: " + this.marca + ", Modelo: " + this.modelo);
    }
}

let auto = new Vehiculo("Toyota", "Corolla");
auto.mostrarInfo();
'''
# ------Fin: Prueba de Jorge Gaibor ------

# ------Inicio: Logs de Errores ------
usuario_git = input("Por favor, ingresa tu nombre de usuario: ")
timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

log_filename = os.path.join(log_directory, f"sintactico-{usuario_git}-{timestamp}.txt")

with open(log_filename, 'w') as log_file:
    # Analiza los tokens primero
    lexer.input(prueba_jorge_sintactico)
    log_file.write("Tokens reconocidos:\n")
    while True:
        tok = lexer.token()
        if not tok:
            break
        log_file.write(f"{repr(tok)}\n")  # Escribe el token en el log

    log_file.write("\nAnálisis Sintáctico:\n")
    try:
        parser.parse(prueba_jorge_sintactico)
        log_file.write("Análisis completado sin errores\n")
    except Exception as e:
        log_file.write(f"Error durante el análisis: {str(e)}\n")

print(f"El análisis léxico y sintáctico se ha guardado en el archivo {log_filename}")
# ------Fin: Logs de Errores ------