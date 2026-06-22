
num = input("please enter a number : ")
num = int(num)
if num % 15 == 0:
    print("fizzbuzz")
elif num % 3 == 0 :
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(f"the number is : {num}")
print('``'*30) 
favoritebook = {}
run = True
while run:
    name = input('enter your name : ')
    book = input('whats your favorite book ? : ')
    favoritebook[name] = book
    exit = input("anyone else ? (yes/no) : ")
    if exit == "yes":
        continue
    else:
        run = False
        print(favoritebook)
print('``'*30) 

shopping_list  = ['milk','apple','bread','eggs']
purchaseds = []
while shopping_list:
    enteghal = shopping_list.pop()
    print('purchasing:', enteghal)
    purchaseds.append(enteghal)
print('``'*30) 
users = ['jhon','sara','mike','admin']
info = {}
while True:
    user = input('enter your username:')
    if user in users:
        city = input('which city do you live in? :')
        age = input('how old are you? :')
        info[user] = 'city:', city ,' age:' , age
    else:
        print('user not found')
    exit = input('if you want to end enter exit :')
    if exit == 'exit':
        print(info)
        break

