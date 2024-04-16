# Exemplo 
~~~
31630481Z012#Marques.da.Silva,Joana@2000/06/20
66775544X980#Rangel.Henriques,Pedro@1925-12-5
36472839X098#Antunes.Silva,Ana.Maria@1715/01/2
28462738Z234#Araujo,maria@1988/5/10
~~~

# Gramática
~~~
Frases-> Frases Frase
        |Frases

frase -> NUM_CC '#' nome_completo '@' DATA_NASC

nome_completo -> nome ',' nome

nomes -> nomes '.' PALAVRA
       | PALAVRA 
~~~

# Arvores Bottom-Up (PLY)
Antunes.Silva,Ana.Maria
~~~
                        nome_completo
                              |
          ------------------------------------------
          |                   |                    |
        nomes                 |                  nomes
          |                   |                    |
    -------------             |              -------------
    |     |     |             |              |     |     |
  Nomes   |     |             |            Nomes   |     |
    |     |     |             |              |     |     |
 PALAVRA '.' PALAVRA          |           PALAVRA '.' PALAVRA
          |                   |                    |     
    Antunes.Silva             ,                 Ana.Maria
~~~


Araujo,Maria@1998/5/10
~~~
                    
                        |
        --------------------------------
          nome_completo        |       |
                |              |       |      
        ----------------       |       |
        |       |      |       |       |
      Nomes     |    Nomes     |       |
        |       |      |       |       |
      PALAVRA   |   PALAVRA    |      DATA
        |       |      |       |       |
      Araujo    ,    Maria     @   1998/5/10
~~~


