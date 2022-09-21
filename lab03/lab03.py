num=input("1.please input a number:") #輸入一數字
if int(num)% 2== 0:        #判斷輸入的數字是否為奇數或偶數
    print("this is even")
else:
    print("this is odd")

id_1=input("2.please input your student ID first character:")  #輸入學號第一碼
id_2=input("3.please input your student ID last 8 numbers:")   #輸入學號後8碼

if int(id_2)%2 ==0:                            #判斷學號後8碼為奇數或偶數 
    print("your student ID number is even")
else:
    print("your student ID number is odd")

str(id_2)        #將id_2轉換為字串型態
print("your student ID is:"+id_1+id_2)  #輸出學號共9碼



        
