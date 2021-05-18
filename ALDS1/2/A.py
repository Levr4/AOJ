def main():
    N = int(input())
    A = list(map(int,input().split()))
    bubblesort(A, N)

def bubblesort(A, N):
    sorted = 0
    count = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(N-1, sorted, -1):
            if A[i]<A[i-1]:
                A[i],A[i-1] = A[i-1],A[i]
                count += 1
                flag = 1
        sorted += 1
    print(*A)
    print(count)

if __name__=='__main__':
    main()