def coins(kinds, money):
    num_list =[0]*(money+1) 
    for i in range(1,money+1):
        num_list[i] = money + 1 
        for j in kinds:
            if j<=i:
                num_list[i]=min(num_list[i],num_list[i-j]+1)
    if num_list[money]==money+1: 
        return -1
    else:
        return num_list[money]

len_data = int(input())
for i in range (len_data):
    sum_kind,money= input().split(' ')
    _kinds = input().split(' ')
    kinds = []
    for i in _kinds:
        kinds.append(int(i))
    print(coins(kinds,int(money)))

