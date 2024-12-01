import lexer  # Import lexer implementation
import parser  # Import parser implementation

def read_xml_file(file_path):
    """Reads an XML file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Example: Read XML content from a file
    file_path = "file.xml"  # Update this path if necessary
    xml_content = read_xml_file(file_path)
    
    # Step 1: Lexical Analysis (Tokenization)
    print("\n=== Tokenizing XML ===")
    lexer.lexer.input(xml_content)
    for token in lexer.lexer:
        print(token)
    
    # Step 2: Parsing XML
    print("\n=== Parsing XML ===")
    parse_result = parser.parser.parse(xml_content, lexer=lexer.lexer)
    
    # Step 3: Display Parse Tree
    print("\n=== Parse Tree ===")
    print(parse_result)

if __name__ == "__main__":
    main()
