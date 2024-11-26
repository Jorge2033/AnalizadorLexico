import datetime
import os
import sys
import ply.yacc as yacc
from analyzers.lexical_analyzer import tokens, reserved
import re

# ------Inicio: Reglas Sintácticas por José Ramos ------

# Solicitud de datos por teclado 
def p_input(p):
  '''input : VARIABLE ASSIGN INPUT LPAREN RPAREN'''
  pass

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

# ------Fin: Reglas Sintácticas por José Ramos ------

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
                | structure_declaration
                | input 
                | error'''
  if len(p) == 2 and p[1] == 'error':
      print(f"Error en la regla 'statement' cerca de '{p.slice[1].value}' en la línea {p.lineno(1)}")

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

# ------Fin: Reglas Sintácticas por Jorge Gaibor ------

def p_error(p):
  if p:
    message = f"Error de sintaxis en '{p.value}' línea {p.lineno}\n"
    print(message)  
    log_file.write(message)  
  else:
    message = "Error de sintaxis: fin inesperado del archivo\n"
    print(message)
    log_file.write(message)


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


# ------Inicio: Prueba de Julio Vivas ------

# ------Fin: Prueba de Julio Vivas ------
prueba_julio = '''
if (x > y) {
    let resultado = x + y;
    const mensaje = "Suma completada";
}
'''

# ------Inicio: Logs de Errores ------
usuario_git = input("Por favor, ingresa tu nombre de usuario: ")
timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

log_filename = os.path.join(log_directory, f"sintactico-{usuario_git}-{timestamp}.txt")

with open(log_filename, 'w') as log_file:

    # ------Inicio: Prueba de José Ramos ------
    prueba_valida = "x = input()"
    codigo_prueba_1 = "x = input;"
    codigo_prueba_2 = "y == input();"
    codigo_prueba_3 = "z = inp();"
    prueba_codigo_aritmetica = '''
    let x = 10 + 20 * 3;
    x = x / 2;
    y = input();
    '''
    # ------Fin: Prueba de José Ramos ------

    def probar_codigo(codigo):
        log_file.write("\nProbando código:\n")
        log_file.write(codigo + "\n")
        lexer.input(codigo)
        log_file.write("\nTokens reconocidos:\n")
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"{repr(tok)}\n")
        log_file.write("\nAnálisis Sintáctico:\n")
        try:
            parser.parse(codigo)
            log_file.write("El código pasó la prueba sintáctica.\n")
        except Exception as e:
            log_file.write(f"Error durante el análisis: {str(e)}\n")

    probar_codigo(prueba_codigo_aritmetica)

print(f"El análisis léxico y sintáctico se ha guardado en el archivo {log_filename}")