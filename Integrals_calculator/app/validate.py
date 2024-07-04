from app.checks import check_term, check_operator

def tokenize_expression(expression):
    tokens = []
    current_token = []
    paren_count = 0

    for char in expression:
        if char == ' ' and paren_count == 0:
            if current_token:
                tokens.append(''.join(current_token))
                current_token = []
        else:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            current_token.append(char)
    
    if current_token:
        tokens.append(''.join(current_token))
    
    return tokens

def validate_input(expression):
    tokens = tokenize_expression(expression)
    print(f"Tokens: {tokens}")

    for i, token in enumerate(tokens):
        print(f"Índice: {i}, Token: {token}")
        if i % 2 == 0:
            if not check_term(token, validate_input):
                print(f"Token inválido como término: {token}")
                return False
        else:
            if not check_operator(token):
                print(f"Token inválido como operador: {token}")
                return False

    return True

