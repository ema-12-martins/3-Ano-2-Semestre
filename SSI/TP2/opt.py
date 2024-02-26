import sys
import random
import re



def main(*args):
    if(args[1]=="setup"):
        num_bytes_a_gerar=int(args[2])
        nome_ficheiro_guarda_chave=args[3]

        with open(nome_ficheiro_guarda_chave, "w+") as ficheiro:
            for i in range(num_bytes_a_gerar):
                novo_byte=random.randint(0,1)
                ficheiro.write(str(novo_byte))
    
    elif(args[1]=="enc"):
        ficheiro_com_criptograma=args[2]
        ficheiro_com_chave=args[3]

        with open(ficheiro_com_criptograma,"r") as ficheiro_criptograma:
            with open(ficheiro_com_chave,"r") as ficheiro_chave:
                #Converter o conteudo para binario
                criptograma=ficheiro_criptograma.read()
                criptograma_aux = criptograma.encode('utf-8') 
                criptograma_bin = ''.join(format(byte, '08b') for byte in criptograma_aux)
            

                #Fazer o XOR
                posicao_chave=0
                chave=ficheiro_chave.read()
                tamanho_chave=len(chave)
                texto_cifrado_bin=""
                for i in range(len(criptograma_bin)):
                    if(criptograma_bin[i]!=chave[posicao_chave]):
                        texto_cifrado_bin+="1"
                    else:
                        texto_cifrado_bin+="0"
                    posicao_chave+=1
                    if(posicao_chave==tamanho_chave):
                        posicao_chave=0
                
                #Converter de novo para texto
                bytes_binario = [texto_cifrado_bin[i:i+8] for i in range(0, len(texto_cifrado_bin), 8)]
                texto = ''.join(chr(int(byte, 2)) for byte in bytes_binario)

                #Guardar a menssagem
                with open(".enc","w+") as ficheiro_cifrado:
                    ficheiro_cifrado.write(texto)





if __name__ == "__main__":
    main(*sys.argv)
