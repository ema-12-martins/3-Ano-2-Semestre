import sys

def count_lines(inp):
    with open(inp, 'rt') as file:
        num_lines = len(file.readlines())
    return num_lines-1

def count_character(inp):
    count = 0
    with open(inp, 'rt') as file:
        i=1
        while i==1:
            char = file.read(1)
            if not char:
                i=0
            else:
                count += 1
    return count

def count_words(inp):
    with open(inp, 'rt') as file:
        content = file.read().replace('\n', ' ')
        num_words = len(content.split())
    return num_words

def main(inp):
    print("Argumentos da linha de comando: ", inp[1])
    print(f"{count_lines(inp[1])} {count_words(inp[1])} {count_character(inp[1])}")

if __name__ == "__main__":
    main(sys.argv)