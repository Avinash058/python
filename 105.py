def solve(lis,maxi):
    mini = lis[0][0]
    d={}
    for i in lis:
        for j in range(i[0],i[2]):
            d[j] = max(d.get(j,0),i[1])
    temp = d[mini]
    cnt = 0
    print(mini,d[mini],end=" ")
    for i in range(mini,maxi+1):
        if i not in d:
            if i ==maxi:
                print(i,0)
                break
            elif cnt == 0:
                print(i,0,end = " ")
            cnt = 1    
        elif d[i]==temp:
            cnt = 0
        else:
            print(i,d[i],end = " ")
            temp = d[i]
            cnt = 0
    return
lis = []
maxi = 0
while True:
    try:
        a,b,c = map(int,input().split())
        if max(a,b,c)>maxi:
            maxi = max(a,b,c)
        lis.append([a,b,c])
    except:
        break
solve(lis,maxi)