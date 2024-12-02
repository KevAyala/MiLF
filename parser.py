import ply.yacc as yacc

from lexer import tokens

def p_document(p):
    '''document : prologue element
                | element'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_prologue(p):
    '''prologue : LT QMARK NAME NAME EQUALS STRING QMARK GT'''

def p_element(p):
    '''element : LT NAME attributes GT content LT SLASH NAME GT
               | LT NAME GT content LT SLASH NAME GT
               | LT NAME attributes GT SLASH GT'''

    if(p[2] == "movie"):
        p[0] = [p[4]]
    else:
        p[0] = p[4]

def p_attributes(p):
    '''attributes : NAME EQUALS STRING attributes
                  | NAME EQUALS STRING'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3] + p[4]
    else:
        p[0] = p[1] + p[2] + p[3]

def p_content(p):
    '''content : content TEXT
               | content element
               | TEXT
               | element
               | '''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        if(type(p[1]) == str):
            p[0] = [p[1]]
        else:
            p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_error(p):
    print(f"Syntax error at {p.value if p else 'EOF'}")

parser = yacc.yacc()
