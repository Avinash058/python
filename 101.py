class Blocks():
    def __init__(self,n):
        self.stack = [0]*n
        for i in range(n):
            self.stack[i] = [i]
    def move(self,work,a,b):
        for i in range(len(self.stack)):
                if (a in self.stack[i]) and (b in self.stack[i]):
                    return
        if a==b:
            return
        flag = None
        flag2 = None
        if work == 'onto':
            for i in range(len(self.stack)):
                if a in self.stack[i]:
                    while self.stack[i][-1]!=a:
                        num = self.stack[i].pop()
                        self.stack[num].append(num)
                    flag = i
                    break
            for j in range(len(self.stack)):
                if b in self.stack[j]:
                    while self.stack[j][-1]!=b:
                        num = self.stack[j].pop()
                        self.stack[num].append(num)
                    flag2 = j
                    break
            num = self.stack[flag].pop()
            self.stack[flag2].append(num)
        elif work == "over":
            for i in range(len(self.stack)):
                if a in self.stack[i]:
                    while self.stack[i][-1]!=a:
                        num = self.stack[i].pop()
                        self.stack[num].append(num)
                    flag = i
                    break
            num = self.stack[flag].pop()
            for j in range(len(self.stack)):
                if b in self.stack[j]:
                    self.stack[j].append(num)
                    break
    def pile(self,work,a,b):
        for i in range(len(self.stack)):
                if (a in self.stack[i]) and (b in self.stack[i]):
                    return
        if a==b:
            return
        flag = None
        flag2 = None
        if work == 'onto':
            for i in range(len(self.stack)):
                if a in self.stack[i]:
                    flag = i
                    break
            for j in range(len(self.stack)):
                    if b in self.stack[j]:
                        while self.stack[j][-1]!=b:
                            num = self.stack[j].pop()
                            self.stack[num].append(num)
                        flag2 = j
                        break
            self.stack[flag2]+=self.stack[flag][self.stack[flag].index(a):]
            self.stack[flag]  =self.stack[flag][:self.stack[flag].index(a)]
        elif work == "over":
            for i in range(len(self.stack)):
                if a in self.stack[i]:
                    flag = i
                    break
            for j in range(len(self.stack)):
                if b in self.stack[j]:
                    flag2 = j
                    break
            self.stack[flag2]+=self.stack[flag][self.stack[flag].index(a):]
            self.stack[flag]  =self.stack[flag][:self.stack[flag].index(a)]        
n = int(input())
stack = Blocks(n)
while True:
    try:
        command = input()
        if command=="quit":
            break
        else:
            command = command.split()
            if command[0] == "move":
                stack.move(command[2],int(command[1]),int(command[3]))
            elif command[0] == "pile":
                stack.pile(command[2],int(command[1]),int(command[3]))
    except:
        break
for i in range(n):
    print(str(i)+":",end ="")
    if len(stack.stack[i])>=1:
        print(" ",end="")
        print(*stack.stack[i])
    else:
        print()
