
"""drones = [{"id":1,"battery":90,"status":"idle"},
          {"id":2,"battery":25,"status":"idle"}]"""
#find ready drone
"""for d in drones:
  print(len(drones))"""
#average battery of entire drones
#average=total/len
"""total=0 
for d in drones:
  total+=d["battery"]
average=total/len(drones)
print(average)

satelites ={"s_1":{"altitude":550,"targets":["tehran","paris","berlin"]},
              "s_2":{"altitude":700,"targets":["tokyo","london"]}}"""
#len of satelites purpose
"""for v in satelites.values():
 # print(len(v["targets"])) 
total=0
for v in satelites.values():
    total+=len(v["targets"])
print(total)  """
#i can't solved max purpose of satelites
#average of satelites altitudes
"""total=0
for v in satelites.values():
    total+=v["altitude"]
average=total/len(satelites)    
print(average)
"""
company = {"enginering":{"employees":[{"name":"ali","salary":3000},{"name":"sara","salary":3500}]},
           "AI":{"employees":[{"name":"reza","salary":5000}]}}
#max salary for each part of company
"""total=0
for employee in company:
    total+=employee["salary"]
print(total) """
"""total=0
for employee in company["enginering"]["employees"]:
    total+=employee["salary"]  
    for employee in company["AI"]["employees"]:
      total+=employee["salary"]    
print(total)   """ 
#highest paid employee

max =max(employee["salary"])  
for v in company.values():
    print(max)    




#store = {"am":[{"name":"lap top","price":1200},{"name":"mouse","price":50}],
        # "ap":[{"name":"phone","price":800},{"name":"headphone","price":100}]}
    !!! did'nt have enough time to solve all of the task,i have done and send you.

