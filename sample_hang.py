'''def sec_a():
    print('/_☹_', chr(92),sep='')#section a
def sec_b():
    print(' >()<')#section b
def sec_c():
    print("  || ")#section c'''



from design_test import sec_a,sec_b,sec_c
import random as r




print('pick your sample buffer :')
ma = input().upper()
sam1 =['cow','buffalo','dog','cat','horse','mouse']
sam2 = ['monitor','graphic card','hard drive']
sam3 = ['spaghetti','pizza','macaroni',]
software_words = ['algorithm',  'app', 'backend', 'browser', 'cache', 'compiler', 'database', 'debugger', 'desktop', 'framework', 'frontend', 'interface', 'library', 'module', 'network', 'operating system', 'patch', 'programming', 'script', 'server', 'software', 'source code', 'stack', 'user interface', 'version control', 'web', 'widget']

comp=''

if ma == 'ANIMALS':
    comp = r.choice(sam1)

if ma == 'HARDWARE':
    comp = r.choice(sam2)

if ma == 'FOOD':
    comp = r.choice(sam3)
if ma == 'SOFTWARE':
    comp = r.choice(software_words)
ls = list(comp)
print(comp) 
print(ls)
life = len(ls)
ls1=['_'*len(ls)]

ind= 0
u = ''
s=''
while life!=0:
    u = input('GUESS THE LETTER: ').lower()
    print(s)
    if u in ls:
        ind = ls.index(u)
        ls1.insert(ind,u)
        sec_a()
    else:
        life-=1
    