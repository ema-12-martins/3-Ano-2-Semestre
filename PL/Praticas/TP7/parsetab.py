
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "INT ISBN TEXTOBiblioteca : LivrosLivros : LivroLivros : Livro ';' LivrosLivro : Titulo Autor Ano ISBNTitulo : TEXTOAutor : TEXTOAno : INT"
    
_lr_action_items = {'TEXTO':([0,4,5,6,],[5,8,-5,5,]),'$end':([1,2,3,9,12,],[0,-1,-2,-3,-4,]),';':([3,12,],[6,-4,]),'INT':([7,8,],[11,-6,]),'ISBN':([10,11,],[12,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Biblioteca':([0,],[1,]),'Livros':([0,6,],[2,9,]),'Livro':([0,6,],[3,3,]),'Titulo':([0,6,],[4,4,]),'Autor':([4,],[7,]),'Ano':([7,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Biblioteca","S'",1,None,None,None),
  ('Biblioteca -> Livros','Biblioteca',1,'p_biblio','sin.py',6),
  ('Livros -> Livro','Livros',1,'p_livros1','sin.py',10),
  ('Livros -> Livro ; Livros','Livros',3,'p_livros2','sin.py',14),
  ('Livro -> Titulo Autor Ano ISBN','Livro',4,'p_livro','sin.py',18),
  ('Titulo -> TEXTO','Titulo',1,'p_titulo','sin.py',24),
  ('Autor -> TEXTO','Autor',1,'p_auto','sin.py',30),
  ('Ano -> INT','Ano',1,'p_ano','sin.py',35),
]
