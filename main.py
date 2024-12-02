import lexer 
import parser
import csv

def read_xml_file(file_path):
    """Reads an XML file and returns its content as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def main():
    file_path = "file.xml"
    xml_content = read_xml_file(file_path)
    
    print("\n=== Tokenizing XML ===")
    lexer.lexer.input(xml_content)
    for token in lexer.lexer:
        print(token)

    parse_result = parser.parser.parse(xml_content, lexer=lexer.lexer)
    print(parse_result)

    with open("movies.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Director', 'Year', 'Genre', 'Duration', 'Rating', 'Language', 'Actor'])
        writer.writerows(parse_result)

if __name__ == "__main__":
    main()
