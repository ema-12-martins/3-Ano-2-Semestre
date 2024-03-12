import ply.lex as lex

tokens=(
    "NUMBER",
    "BOOLEAN",
    "WORD",
    'LPAREN',
    'RPAREN',
    'COMMA',
    'RCURLY',
    'LCURLY',
    'COLON',
)

t_NUMBER = r"\d+(\.\d+)?"
t_WORD=r"\w+"
t_BOOLEAN=r"(true|false)"
t_LPAREN=r"\["
t_RPAREN = r"\]"
t_COMMA = r","
t_RCURLY=r"{"
t_LCURLY=r"}"
t_COLON=r":"

t_ignore =' \t\n\"'

def t_error(t):
    print(f"Caracter ilegal{t.value}")
    t.lexer.skip(1) 

lexer=lex.lex()

with open("ficheiro.json","r") as file:
    text_json=file.read()
lexer.input(text_json)

while tok := lexer.token():
    print(tok.type+"-----"+tok.value)