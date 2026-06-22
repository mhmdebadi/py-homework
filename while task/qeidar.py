

#addmisions depatment numbers to15,3,5:
"""number =int(input("enter your number:"))
active=True
while active:
    if number%3==0 and number%5==0:
        print("fizz buzz")
    elif number%3==0:
        print("fizz")  
    elif number%5==0:
        print("buzz")  
    else:
        print(number)
    active=False    """
#book survay
"""active=True
respons={}
while active:
    name=input("enter your name please:")
    favorite_book=input("enter your favorite book please:")
    respons[name]=favorite_book
    repeat=input("for end enter yes/no:")
    if repeat=="yes":
        active=False
        print(respons)
for k,v in respons.items():
    print(f"{name}:{favorite_book}")  """      
#manage shopping list
"""shopping_cart = ['milk','bread','egg','apple']
purchased_items=[]
while shopping_cart:
    shopping=shopping_cart.pop()
    print(f"my purchase items are:{shopping}")
    purchased_items.append(shopping)
print(f"my purchase items:{purchased_items}")"""
#a list to store usernames
user = ['admin','john','sara','mike']
user_name={}
active=True
while active:
    name=input("enter your name:")
    if name=="exit":
        break
    if name in user:
        age=input("enter your age:")
        city=input("enter your city:")
        user_name[name]={"age":age,"city":city}
    else:
        print("user not found")    
for name in user_name:
    print(name)
    print(user_name[name]['age'])  
    print(user_name[name]['city'])  
    #which one dose'nt wok?
    #what 's my problem?
        

