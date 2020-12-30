lis = ["1"]
for i in range(1,1001):
    lis.append(str(int(lis[-1])*i))
while True:
    try:
        n = int(input())
        summ = 0
        for i in lis[n]:
            summ+=int(i)
        print(summ)
    except:
        break    
