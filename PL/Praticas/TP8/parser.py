data='''
31630481Z012#Marques.da.Silva,Joana@2000/06/20
66775544X980#Rangel.Henriques,Pedro@1925-12-5
36472839X098#ANtunes.Silva,Ana.MAria@1715/01/2
'''

'''
Frases-> Frases Frase
        |Frases

frase -> NUM_CC '#' nome_completo '@' DATA_NASC

nome_completo -> nome ',' nome

nomes -> nomes '.' PALAVRA
       | PALAVRA 


'''
