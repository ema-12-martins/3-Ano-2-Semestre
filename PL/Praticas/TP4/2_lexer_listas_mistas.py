import ply.lex as lex

tokens=(
    "NUMBER",
    "BOOLEAN",
    "WORD",
    'LPAREN',
    'RPAREN',
    'COMMA',
)

t_NUMBER = r"\d+(\.\d+)?"
t_WORD = r"\w+"
t_BOOLEAN = r"(True|False)"
t_LPAREN = r"\["
t_RPAREN = r"\]"
t_COMMA = r","

t_ignore = ' \t\n'  

def t_error(t):
    print(f"Caracter ilegal {t.value}")
    t.lexer.skip(1) 

lexer = lex.lex()

test_list = "[1,5,palavra,False,3.14,0,fim]"
lexer.input(test_list)

while tok := lexer.token():
    print(tok.type + "-----" + tok.value)
