import matplotlib.pyplot as plt
import numpy as np

f = open('Temperature.txt','r')
temp_list = []
temp_list_1 = []
temp_avg = []
for line in f:   #將資料存入temp_list
    if line != 'Tainan:\n':
        if line[-1] == '\n':
            line1 = line[:-1]
            temp_list.append(line1)
        else:
            temp_list.append(line)

for i in temp_list:
    i=list(i.split(','))  #切開資料
    i.pop(0)
    for j in range(12):   #將資料轉成float
        a = i[j].strip()
        i[j] = float(a)
    temp_list_1.append(i)  #將轉換過的資料存入temp_list_1
    
months = np.array(range(1,13))
years = np.array(range(2013,2022))

figure1 = plt.figure()
for i in range(9):   #畫出那9張圖
    plt.plot(months, temp_list_1[i], label=years[i])
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc='lower center')
plt.xticks(months)
plt.xlim(0.5,12.5)
plt.ylim(16,32)
plt.show()
figure1.savefig('lab13_01.png')

sum = 0
sum_tot = 0
for i in range(12):
    for j in range(9):
        sum += temp_list_1[j][i]
    temp_avg.append(sum/9)  #計算各月平均值
    sum_tot += sum/9
    sum = 0
sum_tot = round(sum_tot/12,2)   #計算各月平均值的平均值

figure2 = plt.figure()
plt.plot(months, temp_avg)
plt.scatter(months, temp_avg, c ='r')
plt.axhline(y=sum_tot, label='Mean of 9 Years', color='red', linestyle="--")
plt.text(1,sum_tot+0.1,sum_tot)
for i in range(12):              #標出各點的標籤值
    plt.text(months[i],temp_avg[i],round(temp_avg[i],2),verticalalignment='bottom',horizontalalignment='left')
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(months)   #調整x軸的刻度顯示
plt.xlim(0.5,12.5)   #調整x軸的上下限
plt.ylim(16,32)      #調整y軸的上下限
plt.legend()
plt.show()
figure2.savefig('lab13_02.png')

figure3 = plt.figure(figsize=(15,6))

#以下的註解同上

plt.subplot(1,2,1)
for i in range(9):
    plt.plot(months, temp_list_1[i], label=years[i])
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc='lower center')
plt.xticks(months)
plt.xlim(0.5,12.5)
plt.ylim(16,32)

plt.subplot(1,2,2)
plt.plot(months, temp_avg)
plt.scatter(months, temp_avg, c ='r')
plt.axhline(y=sum_tot, label='Mean of 9 Years', color='red', linestyle="--")
plt.text(1,sum_tot+0.1,sum_tot)
for i in range(12):
    plt.text(months[i],temp_avg[i],round(temp_avg[i],2),verticalalignment='bottom',horizontalalignment='left')
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(months)
plt.xlim(0.5,12.5)
plt.ylim(16,32)
plt.legend()
plt.show()

figure3.savefig('lab13_03.png')