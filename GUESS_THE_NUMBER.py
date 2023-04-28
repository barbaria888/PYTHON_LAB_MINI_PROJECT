def check(e):
    s=0
    if entry == computer:
        print('CONGRATULATIONS YOU WON!')
        s += 100 
        
    if entry < computer:
        print('TOO SMALL,GUESS AGAIN ')
        s -= 10
    if entry > computer:
        print('TOO LARGE,TRY AGAIN')
        s -= 10
    if entry==(computer+1)or entry==(computer-1):
        print('~~CLOSE ENOUGH, BUT TRY AGAIN :)')
        s -= 10
    return s
    
#driver code

import random
import time
N = input('Please Enter Your Name').upper()
time.sleep(1)
print(f'WELCOME {N},LETS PLAY THE GAME OF SHEER LUCK:\n YOU HAVE TO ENTER ANY NUMBER FROM 1 - TO THE NUMBER OF TIMES YOU WANT TO PLAY THE GAME ,IF YOU MANAGE TO GUESS RIGHT,YOU WIN ELSE TRY ONCE AGAIN')
time.sleep(1)
print(f'SO,GOOD LUCK {N}')

score = 0
while True:
    entry = int(input('ENTER YOUR GUESS:'))
    global computer
    computer= random.randint(1,len(N))
    score = check(entry)
    if score>0:
       F =  input('DO YOU WANT TO PLAY AGAIN\n Y/N?').upper()
       
       if F=='N':
           break
    else:
        f = input('DO YOU WANT TO QUIT??\nY/N?').upper()
        if f == 'Y':
            time.sleep(1)
            print(f'THE CORRECT NUMBER WAS{computer}')
            print('THANKS FOR BEING HERE')
            break
        
print(f'Your Score is: {score}')
if score >= 50:
    print('YOU ARE LUCKY TODAY')
