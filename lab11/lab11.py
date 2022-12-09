import json

def BF(input):
    a = ''
    N = len(input)
    for i in range(0,N):
        a = a + str(i)
    a1 = list(a)
    data = permutation(a1)
    data_len = len(data)
    cost = 9999
    sum = 0
    for i in range(0,data_len):
        for j in range(0,N):
            b = int(data[i][j])
            sum = sum + input[j][b]  #計算成本
        if sum < cost :  #當此次的成本比原先的低時，更改原本成本所儲存的值
            cost = sum
            assignment = data[i]
        sum = 0
    
    return assignment, cost

def permutation(lst):  #產生排列的函式
    if len(lst) == 1:
        return [lst]
    l = [] # 儲存排列的組合
 
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]  #拔除 m 後所剩的 list
       for p in permutation(remLst):  ##產生所有排列的方式
           l.append([m] + p)
    return l

# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # show input data and number of the Tasks
        #print(input)

        # Brute Force Algorithm
        assignment, cost = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
