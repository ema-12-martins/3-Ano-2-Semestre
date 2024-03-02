import sys
import cesar

def main(criptograma,palavra_1,palavra_2):
    for i in range(65, 91):
        segredo= cesar.main("dec",chr(i),criptograma)
        if (palavra_1 in segredo) or (palavra_2 in segredo):
            return (chr(i),segredo)
    return ("","")
    

if __name__ == "__main__":
    letra,segredo = main(sys.argv[1],sys.argv[2],sys.argv[3])
    print(letra)
    print(segredo)

     
     

