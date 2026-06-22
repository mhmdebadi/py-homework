# تمرین بخش پذیری
"""
a = int (input("plaese enter a number:"))
while a != 0:
    if a % 15 == 0:
        print("fizzbuzz")
    elif a % 5 ==0:
        print("buzz")
    elif a % 3 == 0:
        print("fizz")
    else:
        print(a)
    break
"""
#-------------------------------------------
# تمرین نظر سنجی
"""
information = {}
while True:
    b = input("please tell me your name \n")
    c = input("whats your favorite book \n")
    d = input("next person?")
    information[b] = c
    if d == "no":
        print(information)
        break
        """
#---------------------------------------------
# تمرین فروشگاه
"""
shoping_cart = ['milk' , 'bread' , 'eggs' , 'apple']
purchased_items = []
while shoping_cart:
    a = shoping_cart.pop()
    purchased_items.append(a)
    print("purchased_items : \t" + a)

print(purchased_items)
"""
#---------------------------------------------
#  تمرین اخر اطلاعات کاربران
"""
users = ['admin' , 'john' , 'sara' , 'mike']
user_info = []
a = input("plese enter your name")
if a in users:
    b = input('tell me your age') 
    c = input('tell me city')
    user_info = a , b , c
else:
    print("user not found")

print(user_info)
"""

   
   
   

