def solve(arr):
    minimum = sum(arr)
    if arr[0]+arr[2]+arr[4]+arr[7]+arr[3]+arr[8]<=minimum:
        minimum = arr[0]+arr[2]+arr[4]+arr[7]+arr[3]+arr[8]
        charset = "GCB"
    if arr[0]+arr[2]+arr[4]+arr[7]+arr[5]+arr[6]<=minimum:
        minimum = arr[0]+arr[2]+arr[4]+arr[7]+arr[5]+arr[6]
        charset = "GBC"
    if arr[0]+arr[1]+arr[5]+arr[8]+arr[3]+arr[7]<=minimum:
        minimum = arr[0]+arr[1]+arr[5]+arr[8]+arr[3]+arr[7]
        charset = "CGB"
    if arr[0]+arr[1]+arr[5]+arr[8]+arr[4]+arr[6]<=minimum:
        minimum = arr[0]+arr[1]+arr[5]+arr[8]+arr[4]+arr[6]
        charset = "CBG"
    if arr[1]+arr[2]+arr[3]+arr[6]+arr[5]+arr[7]<=minimum:
        minimum = arr[1]+arr[2]+arr[3]+arr[6]+arr[5]+arr[7]
        charset = "BGC"
    if arr[1]+arr[2]+arr[3]+arr[6]+arr[4]+arr[8]<=minimum:
        minimum = arr[1]+arr[2]+arr[3]+arr[6]+arr[4]+arr[8]
        charset = "BCG" 
    return charset+" "+str(minimum)
while True:
    try:
        arr = list(map(int,input().split()))
        if len(arr)==9:
            print(solve(arr))
        else:
            break
    except:
        break