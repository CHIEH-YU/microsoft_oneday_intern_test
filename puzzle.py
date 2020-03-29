graph = [[6,8,2],[3,7,5],[0,6,8],[7,5,1],[4,4,4],[1,3,7],[8,2,0],[5,1,3],[2,0,6]]
puzzle=[[0]*3 for i in range(6)]
record_1 = []
record_2 = []

for i in range(6):
   if i==3:
       blank = input()
   puzzle[i] = list(input())
for idx,k in enumerate(puzzle):
   for idx1,j in enumerate(k):
       if j == '*':
           record_1.append(idx*3+idx1)
       else:
           record_2.append(idx*3+idx1)
record_3 = []
for i in record_2:
    if i>8:
        i = i-9
        record_3.append(i)
sum1 = str(puzzle).count('*')
flag=0
if len(record_3)==8 or len(record_1)==8:
    flag=1   
if sum1 == 9:
    for j in range(3):
        new = []
        for i in record_1:
            if i<9:  
                new.append(graph[i][j])
        new1 = []
        new2 = []
        new3 = []
        new4 = []
        new5 = []
        new6 = []
        for y in new:
            new1.append(y+3)
            new3.append(y+1)
            new5.append(y+2)
            new2.append(y-3)
            new4.append(y-1)
            new6.append(y-2)
        if set(new1) == set(record_3) or set(new2) == set(record_3) or set(new) == set(record_3):
            flag=1
            break
        if set(new4) == set(record_3) or set(new3) == set(record_3):
            flag=1
            break
        if set(new5) == set(record_3) or set(new6) == set(record_3):
            flag=1
            break
    if flag==1: 
        print('YES')
    else:
        print('NO')
else:
    print('NO')


