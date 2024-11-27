import ply.lex as lex
import datetime

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
    'input': 'INPUT', # Palabra Agregada por José Ramos
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