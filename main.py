import ply.lex as lex

tokens = (

  #------Inicio: José Ramos (Operadores Arítmeticos) ------
  'PLUS',
  'MINUS',
  'MULTIPLY',
  'DIVIDE',
  'MODULO',  
  'PLUS_ASSIGN',
  'MINUS_ASSIGN',
  'MULTIPLY_ASSIGN',
  'DIVIDE_ASSIGN',
  'MODULO_ASSIGN',
  #------Fin: José Ramos (Operadores Arítmeticos) ------
  #------Inicio: José Ramos (Operadores Booleanos) ------

  #------Fin: José Ramos (Operadores Booleanos) ------
)

#--Inicio: José Ramos (Expresiones regulares Op. Aritmeticos) --
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
# Operadores de asignación de compuestas
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULO_ASSIGN = r'%='
#--Fin: José Ramos (Expresiones regulares Op. Aritmeticos) ---

#--Inicio: José Ramos (Expresiones regulares Op. Booleanos) --

#--Fin: José Ramos (Expresiones regulares Op. Booleanos) --



t_ignore = ' \t'

def t_error(t):
  print(f"Token no admitido '{t.value[0]}' en la línea {t.lineno}")
  t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()