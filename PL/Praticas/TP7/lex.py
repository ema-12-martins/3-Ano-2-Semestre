import ply.lex as lex

literals = [';']

tokens = (
    'TEXTO',
    'INT',
    'ISBN'
)


def t_TEXTO(t):
    r'\"[^"]*\"'
    return t

def t_ISBN(t):
    r'\d{4}\-\d{3}\/\d{3}'
    return t

def t_INT(t):
    r'\d{4}'
    return t



t_ignore =' \n\t'

def t_error(t):
    print("Caracter ilegal")
    t.lexer.skip(1)

lexer = lex.lex()



