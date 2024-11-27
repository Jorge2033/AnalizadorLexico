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

def p_error(p):
  if p:
    message = f"Error de sintaxis en '{p.value}' línea {p.lineno}\n"
    print(message)  
    log_file.write(message)  
  else:
    message = "Error de sintaxis: fin inesperado del archivo\n"
    print(message)
    log_file.write(message)

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