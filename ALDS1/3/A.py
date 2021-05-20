def main():
    A = list(map(str,input().split()))
    mystack = Mystack()
    for e in A:
        if e=='+':
            mystack.sumStack()
        elif e=='-':
            mystack.subStack()
        elif e=='*':
            mystack.mulStack()
        else:
            mystack.push(e)
    print(*mystack.l)

class Mystack:
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(int(e))
    
    def pop(self, e):
        self.l.pop()

    def sumStack(self):
        a = self.l.pop()
        b = self.l.pop()
        self.l.append(a+b)
    def subStack(self):
        a = self.l.pop()
        b = self.l.pop()
        self.l.append(b-a)
    def mulStack(self):
        a = self.l.pop()
        b = self.l.pop()
        self.l.append(a*b)
    
    

if __name__=='__main__':
    main()