import ply.yacc as yacc

# Grammar rules
from lexer import tokens

def p_document(p):
    '''document : prologue element
                | element'''
    if len(p) == 2:
        p[0] = p[1]
        p[0] = p[1] + p[2]

def p_prologue(p):
    '''prologue : LT QMARK NAME NAME EQUALS STRING QMARK GT'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]

def p_element(p):
    '''element : LT NAME attributes GT content LT SLASH NAME GT
               | LT NAME attributes SLASH GT'''
    if len(p) == 6:  # Self-closing tag
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
    else:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

def p_attributes(p):
    '''attributes : NAME EQUALS STRING attributes
                  | NAME EQUALS STRING'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3] + p[4]
    else:
        p[0] = p[1] + p[2] + p[3]

def p_content(p):
    '''content : TEXT
               | element'''
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at {p.value if p else 'EOF'}")

# Create the parser
parser = yacc.yacc()
