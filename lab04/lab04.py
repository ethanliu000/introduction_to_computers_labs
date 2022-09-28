subject=['國文','英文','數學','自然','社會']
name=['A','B','C']
a_score=[]
b_score=[]
c_score=[]
a_tot=0
b_tot=0
c_tot=0
print("開始輸入A學生的成績，請依照",subject,"的順序輸入")
for i in range (0,5):
  ele=int(input())
  a_score.append(ele)
print("A學生成績:")
for i in range (0,5):
  if i==4:
    print(" ",subject[i],":",a_score[i])
  else:
    print(" ",subject[i],":",a_score[i],end='')

print("開始輸入B學生的成績，請依照",subject,"的順序輸入")
for i in range (0,5):
  ele=int(input())
  b_score.append(ele)
print("b學生成績:")
for i in range (0,5):
  if i==4:
    print(" ",subject[i],":",b_score[i])
  else:
    print(" ",subject[i],":",b_score[i],end='')

print("開始輸入C學生的成績，請依照",subject,"的順序輸入")
for i in range (0,5):
  ele=int(input())
  c_score.append(ele)
print("C學生成績:")
for i in range (0,5):
  if i==4:
    print(" ",subject[i],":",c_score[i])
  else:
    print(" ",subject[i],":",c_score[i],end='')

for i in range(5):
  a_tot=a_tot+a_score[i]
  b_tot=b_tot+b_score[i]
  c_tot=c_tot+c_score[i]

print("A學生平均成績:",a_tot/5)
print("B學生平均成績:",b_tot/5)
print("C學生平均成績:",c_tot/5)

for i in range(5):
  d=(a_score[i]+b_score[i]+c_score[i])/3
  print(" ",subject[i],"平均成績:",d)
