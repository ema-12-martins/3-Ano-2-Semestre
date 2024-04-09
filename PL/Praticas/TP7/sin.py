import ply.yacc as yacc
from lex import tokens #Para ir buscar os tokens do lex


def p_biblio(p):
    '''Biblioteca : Livros'''
    return p

def p_livros1(p):
    '''Livros : Livro'''
    return p

def p_livros2(p):
    '''Livros : Livro ';' Livros'''
    return p

def p_livro(p):
    '''Livro : Titulo Autor Ano ISBN'''
    print("Autor:" + p[1] + " ---------------> Titulo: " + p[2])
    parser.conta+=1
    return p

def p_titulo(p):
    '''Titulo : TEXTO'''
    #print(p[1])
    p[0]=p[1]
    return p

def p_auto(p):
    '''Autor : TEXTO'''
    p[0]=p[1]
    return p

def p_ano(p):
    '''Ano : INT'''
    return p

def p_error(p):
    print("Erro sintático! Reescreva a frase.")
    parser.exito=False


data = '''
"Os Maias" "Eça de Queirós" 1860 1000-312/521;
"Amor de Perdição" "Camilo Castelo Branco" 1862 1000-515/329
'''

parser = yacc.yacc()
parser.exito = True
parser.conta = 0

parser.parse(data)

if parser.exito:
    print("Parsing terminou com sucesso")
    print("Numero de Livros:", parser.conta)

