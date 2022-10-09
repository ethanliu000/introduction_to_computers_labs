keys=[]
values_1=[]
values_2=[]
values_3=[]
values_4=[]
dict0={}

for i in range(4):
  ele=input("Enter keys:")
  keys.append(ele)
  for j in range(5):
    wle=input("Enter values:")
    if i == 0:
      values_1.append(wle)
    elif i == 1:
      values_2.append(wle)
    elif i == 2:
      values_3.append(wle)
    else:
      values_4.append(wle)

dict0={keys[0]:values_1,keys[1]:values_2,keys[2]:values_3,keys[3]:values_4}
print("dict0=",dict0)
