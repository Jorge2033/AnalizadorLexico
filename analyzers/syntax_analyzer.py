import datetime
import os
import sys
import ply.yacc as yacc
from analyzers.lexical_analyzer import tokens, reserved
import re

# ------Inicio: Reglas Sintácticas por Jorge Gaibor ------
def p_program(p):
    '''program : statements'''
    print("Programa válido.")

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    pass

def p_statement(p):
    '''statement : print
                | structure_declaration
                | input 
                | error
                | condition'''
    pass
# ------Fin: Reglas Sintácticas por Jorge Gaibor ------    


# ------Inicio: Reglas Sintácticas por José Ramos ------
def p_print(p):
    '''print : CONSOLE DOT LOG LPAREN arguments RPAREN SEMICOLON'''
    p[0] = f"Console.log statement: {p[5]}"

# Solicitud de datos por teclado 
def p_input(p):
  '''input : VARIABLE ASSIGN INPUT LPAREN RPAREN'''
  pass

#expresiones aritméticas con uno o más operadores
def p_expression(p):
    '''expression : STRING
                  | VARIABLE
                  | NUMBER
                  | expression PLUS expression'''
    if len(p) == 2:  # Casos de STRING, VARIABLE o NUMBER
        p[0] = p[1]
    elif len(p) == 4:  # Caso de concatenación con '+'
        p[0] = f"{p[1]} + {p[3]}"

def p_term(p):
  '''term : term MULTIPLY factor
          | term DIVIDE factor
          | factor'''
  pass

def p_factor(p):
  '''factor : NUMBER
            | VARIABLE'''
  pass
# ------Fin: Reglas Sintácticas por José Ramos ------


# ------Inicio: Reglas Sintácticas por Julio Vivas ------
def p_condition(p):
    '''condition : IF LPAREN expression condition_operator expression RPAREN LBRACE statements RBRACE'''
    pass

def p_condition_operator(p):
    '''condition_operator : EQUAL
                        | GREATER
                        | LESS'''
    pass

    def p_variable_declaration(p):
        '''variable_declaration : LET VARIABLE ASSIGN expression SEMICOLON
                            | CONST VARIABLE ASSIGN expression SEMICOLON
                            | VAR VARIABLE ASSIGN expression SEMICOLON'''
        pass
# ------Fin: Reglas Sintácticas por Julio Vivas ------


# ------Inicio: Reglas Sintácticas por Jorge Gaibor ------
def p_arguments(p):
    '''arguments : argument
                 | argument COMMA arguments'''
    if len(p) == 2:  # Solo un argumento
        p[0] = [p[1]]
    elif len(p) == 4:  # Argumento seguido de más argumentos
        p[0] = [p[1]] + p[3]


def p_argument(p):
    '''argument : STRING
                | VARIABLE
                | NUMBER'''
    p[0] = p[1]

def p_structure_declaration(p):
    '''structure_declaration : CLASS VARIABLE LBRACE statements RBRACE'''
    pass
# ------Fin: Reglas Sintácticas por Jorge Gaibor ------


def p_error(p):
  if p:
    print(f"Error de sintaxis en '{p.value}' línea {p.lineno}\n")   
  else:
    print("Error de sintaxis: fin inesperado del archivo\n")

parser = yacc.yacc()

def capture_semantic_errors(input_code):
    log_directory = "logs/semantic/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_filename = f"semantic-(modificarNombre)-{datetime.datetime.now().strftime('%Y%m%d-%Hh%M')}.txt"
    log_filepath = os.path.join(log_directory, log_filename)

    with open(log_filepath, "w") as f:
        sys.stdout = f
        lines = input_code.strip().split('\n')
        for line_num, line in enumerate(lines, start=1):
            try:
                parser.parse(line)
            except Exception as e:
                print(f"Error en línea {line_num}: {e}")
        sys.stdout = sys.__stdout__
    
    print("Análisis completado. Los errores semánticos se han guardado en el archivo de registro:", log_filename)