import re

#....................EXERCICIOS REGEX..............................

#1-Um binario que so contenha pelo menos um zero
def bin_pelo_menos_1_0(input):
    padrao = re.compile('[0,1]*0[0,1]*')

    if padrao.fullmatch(input):
        return True
    else:
        return False

#2-Um bianrio no max 1 zero
def bin_no_max_1_0(input):
    padrao = re.compile('1*[0,1]1*')

    if padrao.fullmatch(input):
        return True
    else:
        return False

#3-Um bianrio no min 1 zero
def bin_no_min_1_0(input):
    padrao = re.compile('1*0[1,0]*')

    if padrao.fullmatch(input):
        return True
    else:
        return False

def main():
    bin1='10111111'
    bin2='111111'
    bin3='10110101'
    print(bin_no_min_1_0(bin1))
    print(bin_no_min_1_0(bin2))
    print(bin_no_min_1_0(bin3))

if __name__ == "__main__":
    main()