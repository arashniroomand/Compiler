import keyword
import regex as re

def lexer(contents):
    lines = contents.split('\n')

    nLines = []
    for line in lines:
        chars = list(line)
        temp_str = ""
        tokens = []
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1
            if quote_count % 2 == 0:
                in_quotes = False
            else:
                in_quotes = True
            if char == " " and in_quotes == False:
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
        tokens.append(temp_str)
        items = []
        for token in tokens:
            iden = False
            if token[0] == "'" or token[0] == '"':
                if token[-1] == '"' or token[-1] == "'":
                    items.append(("string", token))
                else:
                    break
            
            elif re.match(r"[.0-9]+", token):
                items.append(("number", token))
            
            elif token in keyword.kwlist:
                items.append(("Identifier", token))
                iden = True

            elif re.match(r"[.a-zA-Z]+", token) and iden != True:
                items.append(("symbol", token))

            elif token in "+-*/":
                items.append(("expression", token))
            elif token in "=<>=!":
                items.append(("Comparison", token))
        nLines.append(items)
    return nLines

def read_file(source_code):
    contents = open(source_code, 'r').read()
    lines = lexer(contents)
    return(lines)

print(read_file(r'source_code.txt'))
