dict0 = {"index":["國文","英文","數學","自然","社會"],"StuA":[50, 60, 70, 80, 90],"StuB":[57, 86, 73, 82, 43],"StuC":[97, 96, 86, 97, 83]}

subject = list(dict0.keys())
score = list(dict0.values())
a_tot=0
b_tot=0
c_tot=0
d=0

for i in range(5):  #將每個學生的成績加總
  a_tot = a_tot + score[1][i]
  b_tot = b_tot + score[2][i]
  c_tot = c_tot + score[3][i]

print("dict0 = ",dict0,"\n")
print("A學生平均成績:", a_tot / 5)
print("B學生平均成績:", b_tot / 5)
print("C學生平均成績:", c_tot / 5,"\n")

for i in range(5):  #計算各科平均
  d = (score[1][i] + score[2][i] + score[3][i]) / 3
  print(score[0][i], "平均成績:", d)
