import ply.lex as lex

tokens=(
    'PALAVRA',
    'VIRGULA',
    'PONTUACAO'
)

t_PALAVRA=r"\w+"
t_VIRGULA=r","
t_PONTUACAO=r"(!|\?|\.|\.\.\.)"

t_ignore =' \t\n'

def t_error(t):
    print(f"Caracter ilegal{t.value[0]}")
    t.lexer.skip(1) 

lexer=lex.lex()

frase="Isto é uma frase, muito bonita, que construi."
lexer.input(frase)

while tok := lexer.token():
    print(tok)