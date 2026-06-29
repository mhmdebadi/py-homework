# تمرین ماشین
"""
def car(name , model , year ):
    if year != int or str:
        print(name , model , year)
    else:
        print(name , model) 

a = car("bmw" , "x4" , 2020)
print(car)    
"""
#-------------------------------------------------
#  تمرین اطلاعات کتاب 
"""
def book(noeh_book ,name_nevisandeh):
    return(noeh_book , name_nevisandeh)

a = book("python" , "erik motthes")
print("book _info:" , a)
"""
#--------------------------------------------------
# تمرین برنامه خوش امد گویی به کاربر
"""
while True:
    print("ba wared kardan q kharej shavid")
    a = input("whats your name ")
    b = input("whats your last name")
    c = input("khrej mishavid?")
    if c == "q":
     print("khosh omadi:" + a , b)
    break
"""
#------------------------------------------------
# تمرین معرفی حیوان
"""
def animal(name_animal , noeh_animal):
    return(name_animal , noeh_animal)

a = animal("name_animal: cat" , "noeh animal: gorbe sanan")
print(a)
"""
#-------------------------------------------------
#  تمرین انتقال سفاررش 
"""
orders = ["pizza" , "burger" , "pasta"]
completed_orders = []
def food():  
    while orders:
        x = orders.pop(0)
        print("preparing:  " + x)
        completed_orders.append(x)  
        print(completed_orders)

food()
"""
#----------------------------------------------
# تمرین ساخت پروفایل
"""
def build_student(first_name , last_name , **x):
    return(first_name , last_name , x)

z = build_student("alireza" , "cheraghi" , age = 20 , city = "tehran")
print(z)
"""
while True:
        student = {
        "name" : a,
        "last_name" : b,
        "reshteh" : c,
        "age" :d
    }
        print("enter yes and exited:")
        a = input("whats your name:")
        b = input("whats your last name:")
        c = input("reshteh tahsil:")
        d = input("tell me your age")
        i = input("kharej mishavid? yes or no:")

        if i == "yes":
          print(student)
        break
 
