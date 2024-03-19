import ply.lex as lex

states = (
    ('count','inclusive'),
)

tokens = (
    'ON',
    'OFF',
    'NUMBER',
    'EQUAL',
)

t_ANY_ignore = ' \t\n'

def t_INITIAL_ON(t):
    r'(?i)ON'
    t.lexer.begin('count')
    return t

def t_INITIAL_OFF(t):
    r'(?i)OFF'
    t.lexer.begin('INITIAL')
    return t

def t_INITIAL_EQUAL(t):
    r'='
    print(t.lexer.sum)
    return t

def t_count_NUMBER(t):
    r'[+\-]?\d+'
    t.value = int(t.value) 
    t.lexer.sum += t.value
    return t

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

data = input("Introduza a frase a analisar: ")
lexer.input(data)

lexer.sum = 0

while tok := lexer.token():
    print(tok)