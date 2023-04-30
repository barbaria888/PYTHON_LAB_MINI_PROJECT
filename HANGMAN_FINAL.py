def loss5():
    print('███████████████████'  )
    print('█                 ▍' )
    print('█                 ▍' )
    print('█                ☹ ')
    print('█               ⎝██⎠')
    print('█                ██   ')
    print('█               〖〗')
    print('█                ╯╰  ')
    print()



def loss1():
    print('███████████████████'  )
    print('█                 ▍' )
    print('█                 ▍' )
    print('█                ☹ ' )
    print('█                   ' )
    print('█                   ' )
    print('█                   ' )
    print('█                   ' )
    print()



def loss2():
    print('███████████████████'  )
    print('█                 ▍' )
    print('█                 ▍' )
    print('█                ☹ ' )
    print('█               ⎝██⎠' )
    print('█                   ' )
    print('█                   ' )
    print('█                   ' )
    print()
    
def loss3():    
    print('███████████████████'  )
    print('█                 ▍' )
    print('█                 ▍' )
    print('█                ☹ ' )
    print('█               ⎝██⎠' )
    print('█                ██   ' )
    print('█                   ' )
    print('█                   ' )
    print()

def loss4():
    print('███████████████████'  )
    print('█                 ▍' )
    print('█                 ▍' )
    print('█                ☹ ' )
    print('█               ⎝██⎠' )
    print('█                ██   ' )
    print('█               〖〗   ' )
    print('█                   ' )
    print()
def glyph(life):
    if life ==4:
        loss1()
    if life ==3:
        loss2()
    if life ==2:
        loss3()
    if life ==1:
        loss4()
    if life == 0:
        loss5()
        print('REST IN PEACE HANGMAN †')

def chek_bffr(ma):
    comp=''
    if ma == 'SWEETS':
        comp = r.choice(sweets)
    if ma == 'GYM':
        comp = r.choice(gym)
    if ma == 'ANIMALS':
        comp = r.choice(sam1)
    if ma == 'HARDWARE':
        comp = r.choice(sam2)
    if ma == 'FOOD':
        comp = r.choice(sam3)
    if ma == 'SOFTWARE':
        comp = r.choice(software_words)
    return comp

from time import sleep
import random as r
na = input('NAME OF SUSPECT❱❱❱❱❱❱\n').upper()
sleep(0.5)
print(f'\nLISTEN TO ME CAREFULLY {na},ITS A GRAVE SITUATION\n OUR SUSPECT YOU ALIAS {na} ARE OUR SUSPECT AND YOU HAVE TO GUESS THE EVIDENCE WORDS CORRECTLY IN 5 ATTEMPTS.... \nOTHERWISE YOU ARE HANGED TO DEATH  ☠ ')
sleep(0.5)
print('⫸⫸ PICK YOUR EVIDENCE SET FROM FOLLOWING ⫸⫸\n SOFTWARE\nFOOD\nSWEETS\nGYM\nHARDWARE')

ma = input().upper()
sam1 =['cow','buffalo','dog','cat','horse','mouse']
sam2 = ['monitor','graphic card','hard drive']
sam3 = ['spaghetti','pizza','macaroni','pasta','sandwich','cake']
sweets = ['cake','choclate','candy','lollipop','mousse','cottoncandy']
gym = ['bicep','curl','creatine','muscle','tricep','abs','forcep','bulk','lean']
software_words = ['algorithm',  'app', 'backend', 'browser', 'compiler', 'database', 'debugger', 'desktop', 'framework', 'frontend', 'interface',  'module', 'network', 'operating system',  'programming', 'script', 'server', 'software', 'source code', 'stack', 'user interface', 'web', ]

comp= chek_bffr(ma)
ls = list(comp)
print(len(comp)) 
print(ls)
life = 5
st=list('_'*len(ls))

ind= 0
u = ''
s=''
i=0
k=0
while life!=0:
    u = input('GUESS LETTER OR RIP †').lower()
    print(st)
    glyph(life)
    if u in ls:
        freq=st.count(u)
        print(freq)
        if freq>1:
            ind=ls.index(u,ind+1)
        else:
            ind = ls.index(u)
        st[ind]=u#drives the index fillings
        print()
        print(ind)
        out=''.join(st)
        print(out)
        if out==comp:
            print('HA, YOU GUESSED IT RIGHT\nYOU SURVIVED..')
            break    
    else:
        life-=1
        glyph(life)
