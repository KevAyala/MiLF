import ply.lex as lex

tokens = (
    'LT', 'GT', 'SLASH', 'EQUALS', 'QMARK',
    'STRING', 'NAME', 'TEXT'
)

t_LT = r'<'
t_GT = r'>'
t_SLASH = r'/'
t_EQUALS = r'='
t_QMARK = r'\?'

# # Quoted strings for attributes
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Tag names and attribute names
def t_NAME(t):
    r'(\w+)'
    return t

# Text content
# def t_TEXT(t):
#     r'(.+?)'
#     return t

# Ignoring spaces and newlines
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def read_xml_file(file_path):
    """Reads an XML file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read()

file_path = "file.xml"  # Update this path if necessary
xml_content = read_xml_file(file_path)

print("\n=== Tokenizing XML ===")
lexer.input(xml_content)
for token in lexer:
    print(token)
