#Tem como objetivo criar 8 pastas TPC (TPC1,TPC2...)
#Criar Pasta "Projeto"
#Criar Pasta "Teste"
#Em cada pasta criar o ficheiro .gitkeep (para nao apagar as pastas vazias)

import os

#Mudar diretoria
os.chdir('/home/emamartins12/GIT/EngWeb2024')

for i in range(8):
    nomePasta=f"TPC{i+1}"

    #Criar pasta
    os.mkdir(nomePasta)

    #Criar ficheiros
    open(f"{nomePasta}/.gitkeep","w")

nomePasta="Teste"
os.mkdir(nomePasta)

nomePasta="Projeto"
os.mkdir(nomePasta)