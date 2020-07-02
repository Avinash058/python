d ={1:1,2:2}
def maxc(n, d):
    if n in d:
        return d[n]
    else:
        if n%2==0:
            d[n] = maxc(n//2,d)+1
        else:
            d[n] = maxc(3*n+1,d)+1
        return d[n]
while True:
    try:
        i,j = map(int,input().split())
        i1,j1 = i,j
        if i>j:
            i,j = j,i
        res = 0
        for num in range(i,j+1):
            a = maxc(num,d)
            if a>res:
                res = a
        print(i1,j1,res)
    except:
        break