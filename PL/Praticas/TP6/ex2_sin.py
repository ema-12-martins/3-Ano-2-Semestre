import ply.yacc as yacc
import sys

from ex2_lex import tokens 

def p_bibliografia_grammar(p):
    """ 
    Bibliografia:Livros

    Livros:Livro
          |Livros Livro

    Livro:Titulo Autor Ano ISBN

    Titulo: TEXTO
    
    Autor: TEXTO

    Ano: INT
    """

def p_error(p):
    print("Erro sintático! Reescreva a frase.")
    parser.exito=False

parser = yacc.yacc()
parser.exito = True

fonte =""
for linha in sys.stdin:
    fonte+=linha

if parser.exito:
    print("Parsing terminou com sucesso")


