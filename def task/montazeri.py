'''
def car (x,y,*a):
    if a == ():
        print(x,y,)
    else:
        b = a[0]
        print(x,y,b)
car('bmw','m4','a')
**************************************************
def book (*a):
    print('book info:',a)
book('hello','whats up?')
****************************************************
a = 'hi whats your name ?: '
b = 'and your last name please : '
c = 'thank you do you want to exit? if do you want enter (q) if no enter anything :'
m = []
e = True
while e:
    f = input(a)
    l = input(b)
    g = input(c)
    m.append(f)
    m.append(l)
    if g == "q":
        print('its ok')
        e = False
    else :
        print(m)
        continue
*************************************************************
def animal(a):
    if a == "cat" or a =="lion" or a =="tiger" or a =="dog" or a =="bear" or a =="donkey":
        print(a+" = mammale")

    elif a == "ghezel ala" or a =="salmon" or a =="catfish" or a =="sardine" :
        print(a + " = fish")

    elif a == "eagle" or  a =="parrot" or a =="duck" or a =="chiken" or a =="rooster":
         print(a + " = bird") 
    

    else:
        print('i dont know what is it')

def food ():
    orders = ['pizza','burger','pasta']
    completed_orders = []
    for i in orders:
        print(f'preparing {i}')
        completed_orders.append(i)
        print('complete')
    
food()

def student(**a):
    b = {}
    b['first name'] = a[0]
    b['last name'] = a[1]
student('ali','hasan')
i dont know this
'''
h = True
info = {}
while h:
     n = input('please enter your name : ')
     l = input('please enter your last name :')
     m = input('please enter your major : ')
     a = input('please enter your age : ')
     info['first name'] = n
     info['last name']=  l
     info['major'] = m
     info['age'] = a
     z = input('if do you want to exit enter q: ')
     if z == 'q':
          print(info)
          h = False
     else:
          continue
     