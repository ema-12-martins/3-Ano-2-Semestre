import ply.lex as lex

tokens=(
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

#Ele le sempre primeiro a expressao mais comprida
t_PLUS=r"\+"
t_MINUS=r"-"
t_TIMES=r"\*"
t_DIVIDE=r"\/"
t_LPAREN=r"\("
t_RPAREN = r"\)"

#As funcoes, ele le por ordem em que estao no ficheiro as funcoes
def t_NUMBER(t): #O t é o valor capturado com o token
    r"\d+"
    t.value=int(t.value)
    return t

#O que ele vai ignorar
t_ignore =' \t'

#Para contar as linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Funcao a ser executada caso o caracter veja invalido
def t_error(t):
    print(f"Caracter ilegal{t.value[0]}")
    t.lexer.skip(1) #Ignorar
    #exit(1) se quisermos sair do programa

#construir o lexer
lexer=lex.lex()

frase="4 * (2 + 3) \n 3*4"
lexer.lineno=0

#Passamos a fase para o lexer
lexer.input(frase)

#Devolver os tokens. Le 1 tok de cada vez, pelo que temos de chamar varias vezes
while tok := lexer.token():
    #Diz o token
    print(tok)
    #Diz a linha
    print(lexer.lineno)