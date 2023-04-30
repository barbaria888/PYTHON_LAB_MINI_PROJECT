from random import randint
n=int(input('ENTER THE LENGTH OF THE PASSWORD\n8 CHARACTERS AT LEAST\n12 CHARACTERS AT MAX'))
ot=''
st=0
for i in range(n):
    st = randint(48,122)
    ot+=chr(st)
print(ot)