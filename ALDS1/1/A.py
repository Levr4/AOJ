def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(*A)
    insertsort(A, N)

def insertsort(A, N):
    for i in range(1,N):
        for j in range(i):
            if A[i-j]<A[i-j-1]:
                A[i-j],A[i-j-1] = A[i-j-1], A[i-j]
        print(*A)

if __name__=='__main__':
    main()