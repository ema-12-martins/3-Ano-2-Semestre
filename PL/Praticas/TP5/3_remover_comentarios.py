import ply.lex as lex

states = (
    ('comentariobloco', 'exclusive'),
    ('comentariolinha', 'exclusive')
)

tokens = (
    'INICIOBLOCO',
    'FIMBLOCO',
    'INICIOLINHA',
    'FIMLINHA'
)

def t_INITIAL_INICIOBLOCO(t):
    r'/\*'
    lexer.begin('comentariobloco')
    return t

def t_comentariobloco_FIMBLOCO(t):
    r'\*/'
    lexer.begin('INITIAL')
    return t

def t_INITIAL_INICIOLINHA(t):
    r'//'
    lexer.begin('comentariolinha')
    return t

def t_comentariolinha_FIMLINHA(t):
    r'\n'
    lexer.begin('INITIAL')
    pass  

def t_INITIAL_qualquercoisa(t):
    r'(.|\n)'
    t.lexer.texto_ignora_comentario += t.value 

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
/* comment */ ola1

/* comment****comment */ ola2 /*
comment
/* comentário dentro de comentário */
****/ ola3

/*********/

ola4
 mais um pouco // remover comentário inline
FIM
'''

lexer.texto_ignora_comentario = ''  
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

print(lexer.texto_ignora_comentario)

