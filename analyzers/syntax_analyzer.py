import datetime
import os
import sys
import ply.yacc as yacc
from analyzers.lexical_analyzer import tokens, reserved
import re

# ------Inicio: Reglas Sintácticas por Jorge Gaibor ------
def p_program(p):
    '''program : statements'''

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    pass

def p_statement(p):
    '''statement : print
                 | structure_declaration
                 | input 
                 | condition
                 | arithmetic_assignment
                 | object_creation
                 | constructor_declaration
                 | method_call
                 | error'''
    pass
# ------Fin: Reglas Sintácticas por Jorge Gaibor ------    


# ------Inicio: Reglas Sintácticas por José Ramos ------
def p_print(p):
    '''print : CONSOLE DOT LOG LPAREN arguments RPAREN SEMICOLON'''
    p[0] = f"Console.log statement: {p[5]}"

def p_input(p):
    '''input : VARIABLE ASSIGN PROMPT LPAREN RPAREN SEMICOLON
            | LET VARIABLE ASSIGN PROMPT LPAREN RPAREN SEMICOLON
            | VAR VARIABLE ASSIGN PROMPT LPAREN RPAREN SEMICOLON
            | CONST VARIABLE ASSIGN PROMPT LPAREN RPAREN SEMICOLON'''
    p[0] = f"Solicitud de datos asignada a variable '{p[1]}'"

#expresiones aritméticas con uno o más operadores
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    pass

def p_term(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | factor'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | VARIABLE'''
    pass

def p_expression_comparison(p):
    '''expression : expression GREATER expression
                  | expression LESS expression
                  | expression GREATER_EQUAL expression
                  | expression LESS_EQUAL expression
                  | expression EQUAL expression
                  | expression NOT_EQUAL expression'''
    pass

def p_arithmetic_assignment(p):
    '''arithmetic_assignment : LET VARIABLE ASSIGN expression SEMICOLON
                            | VAR VARIABLE ASSIGN expression SEMICOLON
                            | CONST LET VARIABLE ASSIGN expression SEMICOLON'''
    p[0] = f"Variable '{p[2]}' declarada y asignada con el resultado de una operación."


def p_invalid_declaration(p):
    '''typed_variable_declaration : VARIABLE error
                                   | VARIABLE VARIABLE error'''
    print(f"Error: Token inesperado '{p[2].value}' en línea {p.lineno(2)}, posición {p.lexpos(2)}.")

def p_object_creation(p):
    '''object_creation : VARIABLE ASSIGN NEW VARIABLE LPAREN arguments RPAREN SEMICOLON'''
    p[0] = f"Objeto '{p[4]}' creado y asignado a la variable '{p[1]}'."

def p_method_call(p):
    '''method_call : VARIABLE DOT VARIABLE LPAREN arguments RPAREN SEMICOLON'''
    p[0] = f"Método '{p[3]}' llamado en el objeto '{p[1]}'."

def p_constructor_declaration(p):
    '''constructor_declaration : CONSTRUCTOR LPAREN parameters RPAREN LBRACE constructor_body RBRACE'''
    p[0] = f"Constructor declarado correctamente con parámetros: {p[3]} y cuerpo: {p[6]}."

def p_parameters(p):
    '''parameters : parameter
                  | parameters COMMA parameter'''
    if len(p) == 2:  # Un único parámetro
        p[0] = [p[1]]
    elif len(p) == 4:  # Varios parámetros
        p[0] = p[1] + [p[3]]

def p_parameter(p):
    '''parameter : VARIABLE COLON VARIABLE'''
    p[0] = f"{p[1]} de tipo {p[3]}"

def p_constructor_body(p):
    '''constructor_body : constructor_statement
                        | constructor_body constructor_statement'''
    if len(p) == 2:  # Una sola declaración
        p[0] = [p[1]]
    elif len(p) == 3:  # Múltiples declaraciones
        p[0] = p[1] + [p[2]]

def p_constructor_statement(p):
    '''constructor_statement : THIS DOT VARIABLE ASSIGN VARIABLE SEMICOLON'''
    p[0] = f"Asignación dentro del constructor: {p[3]} = {p[5]}"

# ------Fin: Reglas Sintácticas por José Ramos ------


# ------Inicio: Reglas Sintácticas por Julio Vivas ------
def p_condition(p):
    '''condition : IF LPAREN expression RPAREN LBRACE statements RBRACE
                 | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if len(p) == 8:  # Solo el bloque `if`
        p[0] = f"Estructura 'if' sin 'else'."
    elif len(p) == 12:  # Bloque `if-else`
        p[0] = f"Estructura 'if-else' correctamente estructurada."

def p_condition_operator(p):
    '''condition_operator : EQUAL
                          | GREATER
                          | LESS
                          | GREATER_EQUAL
                          | LESS_EQUAL
                          | NOT_EQUAL'''
    pass

def p_typed_variable_declaration(p):
    '''typed_variable_declaration : VAR VARIABLE COLON VARIABLE SEMICOLON
                                   | LET VARIABLE COLON VARIABLE SEMICOLON
                                   | CONST VARIABLE COLON VARIABLE SEMICOLON
                                   | VAR VARIABLE error
                                   | LET VARIABLE error
                                   | CONST VARIABLE error'''
    if len(p) == 6:  # Declaración válida
        p[0] = f"Variable declarada: {p[2]} de tipo {p[4]}"
    else:  # Declaración inválida
        print(f"Error de sintaxis en línea {p.lineno(2)}, posición {p.lexpos(2)}: Falta ':' o tipo en declaración de '{p[2]}'.")


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
    '''structure_declaration : CLASS VARIABLE LBRACE typed_variable_declarations RBRACE'''
    p[0] = f"Clase '{p[2]}' con declaraciones de variables."

def p_typed_variable_declarations(p):
    '''typed_variable_declarations : typed_variable_declaration
                                   | typed_variable_declarations typed_variable_declaration'''
    pass
# ------Fin: Reglas Sintácticas por Jorge Gaibor ------


def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}'"
    else:
        error_msg = "Error de sintaxis: fin inesperado de entrada"
    print(error_msg)
    raise SyntaxError(error_msg)  # Detener el análisis si hay un error


parser = yacc.yacc()


