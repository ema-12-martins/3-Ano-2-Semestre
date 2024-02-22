import sys

def preproc(str):
      l = []
      for c in str:
          if c.isalpha():
              l.append(c.upper())
      return "".join(l)  

def main(tipo_operacao,letra_deslocamento,frase):
    frase=preproc(frase)
    letra_deslocamento=preproc(letra_deslocamento)

    resultado=""
    if(tipo_operacao=="enc"):
        for i in range (len(frase)):
            novo_char =chr(((ord(frase[i])-65)+(ord(letra_deslocamento)-65)%26)+65)
            resultado+=novo_char
        
    elif(tipo_operacao=="dec"):
        for i in range (len(frase)):
            novo_char =chr(((ord(frase[i])-65)-(ord(letra_deslocamento)-65)%26)+65)
            resultado+=novo_char
        
    return resultado

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

     
     

