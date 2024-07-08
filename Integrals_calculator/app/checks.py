import re
import sympy as sp

# Diccionario de funciones matemáticas permitidas
ALLOWED_FUNCTIONS = {
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'exp': sp.exp,
    'sqrt': sp.sqrt,
    'log': sp.log,
    'log10': sp.log,
    'pi': sp.pi,
    'e': sp.E
}

def check_term(token, validate_input_callback):
    is_valid = check_function(token, validate_input_callback) or check_scalar(token) or check_incognita(token)
    print(f"Check term '{token}': {is_valid}")
    return is_valid

def check_scalar(token):
    is_valid = bool(re.fullmatch(r'[+-]?(\d+(\.\d*)?|\.\d+)', token))
    print(f"Check scalar '{token}': {is_valid}")
    return is_valid

def check_incognita(token):
    is_valid = bool(re.fullmatch(r'[+-]?\d*\*?x', token))
    print(f"Check incognita '{token}': {is_valid}")
    return is_valid

def check_function(token, validate_input_callback):
    match = re.match(r'(\w+)\((.*)\)', token)
    if match:
        func_name, inner_expr = match.groups()
        if func_name in ALLOWED_FUNCTIONS:
            print(f"Check function '{token}', Inner expression: {inner_expr}")
            return validate_input_callback(inner_expr)
    return False

def check_operator(token):
    is_valid = token in '+-*/'
    print(f"Check operator '{token}': {is_valid}")
    return is_valid

