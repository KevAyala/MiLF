import ply.lex as lex

tokens = (
    'LT', 'GT', 'SLASH', 'EQUALS', 'QMARK',
    'STRING', 'TEXT', 'NAME'
    )

t_LT = r'<'
t_GT = r'>'
t_SLASH = r'/'
t_EQUALS = r'='
t_QMARK = r'\?'

def t_STRING(t):
    r'"([^"]+)"'
    t.value = t.value[1:-1]
    return t

# Text content
def t_TEXT(t):
    r'(?<=>)[^><]+(?=<)'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

t_ignore = ' \n'

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()