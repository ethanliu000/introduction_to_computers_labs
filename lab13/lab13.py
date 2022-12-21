import matplotlib.pyplot as plt
import numpy as np

f = open('Temperature.txt','r')
temp_list = []
temp_list_1 = []
temp_avg = []
for line in f:
    if line != 'Tainan:\n':
        if line[-1] == '\n':
            line1 = line[:-1]
            temp_list.append(line1)
        else:
            temp_list.append(line)

for i in temp_list:
    i=list(i.split(','))
    i.pop(0)
    for j in range(12):
        a = i[j].strip()
        i[j] = float(a)
    temp_list_1.append(i)
    

#print(temp_list_1)

months = np.array(range(1,13))
years = np.array(range(2013,2022))

figure1 = plt.figure()
for i in range(9):
    plt.plot(months, temp_list_1[i], label=years[i])
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc='lower center')
plt.xticks(months)
plt.xlim(0.5,12.5)
plt.ylim(16,32)
plt.show()
#figure1.savefig('lab13_01.png')

sum = 0
sum_tot = 0
for i in range(12):
    for j in range(9):
        sum += temp_list_1[j][i]
    temp_avg.append(sum/9)
    sum_tot += sum/9
    sum = 0
sum_tot = round(sum_tot/12,2)

figure2 = plt.figure()
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
#figure2.savefig('lab13_02.png')

figure3 = plt.figure(figsize=(15,6))

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

#figure3.savefig('lab13_03.png')