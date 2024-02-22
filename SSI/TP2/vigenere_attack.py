import sys
import vigenere

def main(*args):
    for i in range(int(args[0])):
        resultado=vigenere.main("des",args[1],args[2+i])

        if(args[1]==resultado):
            print(args[2+i])
            print(resultado)

if __name__ == "__main__":
    main(*sys.argv[1:])