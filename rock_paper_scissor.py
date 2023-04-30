from time import sleep 
from random import choice
def short(u):
    p=''
    if u == 'R':
        p = 'ROCK'
    if u == 'P':
        p = 'PAPER'
    if u == 'S':
        p= 'SCISSORS'
    print(f'USER:{p}')
    
        
    
    return p

def check_win(p):
    comp = choice(set1)
    s=0
    print(f'COMPUTER:{comp}')
    if (p!='')and((p=='SCISSORS'and comp=='PAPER') or (p  =='PAPER' and comp == 'ROCK')or( p== 'ROCK' and comp == 'SCISSORS')):
        s= 100
        print('HURRAY!YOU WON ')
        print('+100 POINTS\n')
        sleep(4)
    return s
def greet():
    print(f'---------HI {na}, its good to see you,lets play ROCK PAPER SCISSOR----------------')
    print()
    print('YOU NEED NOT TO TYPE ROCK,PAPER, SCISSOR\nEACH TIME JUST ENTER R for ROCK,S for SCISSOR,P for PAPER WHEN IT SAYS:\nYOUR MOVE:')
    print()
    sleep(2)

# main code:
set1= ['ROCK','PAPER', 'SCISSORS']
score=0
na = input('PLEASE ENTER YOUR NAME').upper()
sleep(1)

greet()

while True:
    u = input('YOUR MOVE:').upper()
    p = short(u)
    score+=check_win(p)
    f=input('DO YOU WANT TO PLAY AGAIN?\nY/N?').upper()
    print()
    if f=='N':
        sleep(1)
        print('FINE,WE WILL MEET AGAIN...')
        break

print()
print(f'YOUR TOTAL SCORE IS:{score}')
