
#task1(car introduction)
"""def cars(name,model,since=" "):
  if since:
    cars_info=f"{name}{model}{since}"  
  else:
    cars_info=f"{name}{model}"
  return cars_info
c=cars("bmw","x4",2020)  
print(c)
c=cars("bmw","x4") """
#task2(bookinformation)
"""def book_info(author,book):
  while True:    
    name=input("enter author name:")
    if name=="q":
      break
    book=input("enter book name:")
    if book=="q":
      break
b=book_info("eric math","python")    
print(b)"""
#task3(welcome program)
"""p="enter your name:"
p+="\nenter your last name:"
active=True
while True:
    n=input(p)
    if n=="q" :
      break
    else:
       print(n)  """
#task4(animal information)
"""def animal_type(name,animal="cat"):
    return f"{name}{animal}"
print(f"i have a{animal}")
a=animal_type("kitty")  
print(f"the name of my cat is {a}")  
i can't solve it"""
#task5(preparring pizza)
"""orders=["pizza","burger","pasta"]
completed_order=[]
while orders:
    a=orders.pop()
    print(f"your order:{a}")
    completed_order.append(a)
    for c in completed_order:
        print(f"preparing :{c}")
print("your order is ready.")    """
#task7(students informations)    
"""students={}
while True:
    name=input("enter your name:")
    if name=="q":
        break
    last_name=input("enter your last name:")
    if last_name=="q":
        break
    field=input("enter your field:")
    age=input("enter your age:")
    students[name]={"name":name,"last":last_name,"fields":field,"age":age}
    for k,v in students.items():
        print(f"{k}:{v}")"""
#task6(student profile)
def build_profile(name,last,**user_info):
    user_info['first_name']=name
    user_info['last_name']=last
    return user_info
p=build_profile('parvaneh','gheydar',age=31,field='biology',city='shahriyar')
print(p)

  