def disp():
    print(f'⁰{ls[0]} ║¹{ls[1]}  ║²{ls[2]}')
    print('═══╬════╬═══')
    print(f'³{ls[3]} ║⁴{ls[4]}  ║⁵{ls[5]}')
    print('═══╬════╬═══')
    print(f'⁶{ls[6]} ║⁷{ls[7]}  ║⁸{ls[8]}')


import random as r
numwin = 0
numlos = 0
st = ['╳','0']
m=input(f'CHOOSE EITHER {st[0]}-╳ OR {st[1]}-0').upper()
k=st[0]if m=='X' else st[1]
st.remove(k)
o = r.choice(st)
pos = [0,1,2,3,4,5,6,7,8]
ls = [' ',' ',' ',' ',' ',' ',' ',' ' ,' ']

while len(pos):
    u=int(input('ENTER THE POSITION YOU WANT TO MARK '))    
    ls[u]=m
    pos.remove(u)
    c=r.choice(pos)
    ls[c]=o
    disp()
    print()
    if ls[0]==ls[1]==ls[2]==m or ls[3]==ls[4]==ls[5]==m or ls[6]==ls[7]==ls[8]==m or ls[0]==ls[4]==ls[8]==m or ls[2]==ls[4]==ls[6]==m or ls[0]==ls[3]==ls[6]==m or ls[1]==ls[4]==ls[7]==m or ls[2]==ls[5]==ls[8]==m:
     disp()
     print('CONGRATULATIONS!!!\nYOU WON!')
     numwin += 1
     f= input('DO YOU WANT TO PLAY AGAIN?\nY/N?').upper()
     if f=='N':
        break
        
    
    if ls[0]==ls[1]==ls[2]==c or ls[3]==ls[4]==ls[5]==c or ls[6]==ls[7]==ls[8]==c or ls[0]==ls[4]==ls[8]==c or ls[2]==ls[4]==ls[6]==c or ls[0]==ls[3]==ls[6]==m or ls[1]==ls[4]==ls[7]==m or ls[2]==ls[5]==ls[8]==m:
        disp()
        print('YOU LOST')        
        f= input('DO YOU WANT TO PLAY AGAIN?\nY/N?').upper()
        numlos += 1
        if f=='N':
            break
print(f'YOU WON {numwin} TIMES AND\nLOST {numlos} TIMES')
    
