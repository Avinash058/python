while True:
    try:
        n = input().split()
        if n==[]:
            break
        print(" ".join([x[::-1] for x in n]))
    except:
        break
