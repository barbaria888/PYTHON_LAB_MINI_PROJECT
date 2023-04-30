from random import random,randint
def num(n):
    com =random()
    out=str(com)
    print(out[2:n])

def alphanum(n):
    ot=''
    st=0
    for _ in range(n):
        st = randint(48,122)
        ot+=chr(st)
    print(ot)

#main code
us=input('TYPE OF OTP\nALPHABNUMERIC [A] OR NUMERIC [N]').upper()
n =  int(input('ENTER THE LENGTH OF OTP'))
if us=='A':
    alphanum(n)
if us=='N':
    num(n)