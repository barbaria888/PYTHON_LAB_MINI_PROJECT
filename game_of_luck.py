import random
N = input('Please Enter Your Name').capitalize()
print(f'WELCOME {N},LETS PLAY THE GAME OF SHEER LUCK:\n YOU HAVE TO ENTER ANY NUMBER FROM 1 - TO THE NUMBER OF TIMES YOU WANT TO PLAY THE GAME ,IF YOU MANAGE TO GUESS RIGHT,YOU WIN ELSE TRY ONCE AGAIN')
print(f'SO,GOOD LUCK {N}')
n = int(input('How many times would you be able to play? '))
computer = random.randint(1,n)
score = 0
for i in range(n):
    entry = int(input('ENTER YOUR GUESS:'))
    if entry == computer:
        print('CONGRATULATIONS YOU WON!')
        score += 100 
    else:
        print('SORRY,PLEASE TRY AGAIN...')
        score -= 10
print(f'Your Score is: {score}')
if score >= 50:
    print('YOU ARE LUCKY TODAY')