import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

f = open('oddExperiment.txt','r')
data_y = []
data_x = []
y_pre = []
y_pre2 = []
for line in f:  #讀取資料
    if line[-1] == '\n':
        line1 = line[:-1]
        line1=list(line1.split(' '))
        data_y.append(line1[0])  #將y軸資料存入data_y
        data_x.append(line1[1])  #將x軸資料存入data_x
    else:
        line=list(line.split(' '))
        data_y.append(line[0])   #將y軸資料存入data_y
        data_x.append(line[1])   #將x軸資料存入data_x

print(data_y,data_x)
data_y.pop(0)
data_x.pop(0)
len1 = len(data_x)
for i in range(len1):   #將data_x內的值轉成float
    a = float(data_x[i])
    data_x[i] = a

for i in range(len1):   #將data_x內的值轉成float
    a = float(data_y[i])
    data_y[i] = a

figure1 = plt.figure()
plt.title('oddExperiment Data')
eq1 = np.polyfit(data_x,data_y,1)  #計算一階多項式 

eq2 = np.polyfit(data_x,data_y,2)  #計算二階多項式
for i in range(len1):
    y1 = np.poly1d(eq2)
    y_pre2.append(y1(data_x[i]))   #計算二階多項式所對應的y軸的點
    y_pre.append(eq1[1])

mse1 = round(mean_squared_error(data_y,y_pre),5)  #計算一階多項式的mse
mse2 = round(mean_squared_error(data_y,y_pre2),5) #計算二階多項式的mse

#print(mse1,mse2)

r2_1 = round(r2_score(data_y,y_pre),5)   #計算一階多項式的R square error
r2_2 = round(r2_score(data_y,y_pre2),5)  #計算二階多項式的R square error

#print(r2_1,r2_2)

plt.scatter(data_x, data_y,label='Data')
plt.title('oddExperiment Data')
plt.axhline(y=eq1[1],  color='orange', label= 'Fit of degree 1,LSE='+ str(mse1))
plt.plot(data_x,y_pre2,color='green', label= 'Fit of degree 2,LSE='+ str(mse2))
plt.axhline(y=eq1[1],  color='red', label= 'Fit of degree 1,R2='+ str(r2_1))
plt.plot(data_x,y_pre2,color='purple', label= 'Fit of degree 1,R2='+ str(r2_2))

plt.legend(loc='upper center')
plt.show()
figure1.savefig('lab13_plus.png')