def main():
    N = int(input())
    A = list(map(int,input().split()))
    selectionsort(A, N)

def selectionsort(A, N):
    count = 0
    for i in range(N):
        minj = i
        flag = 0
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
                flag = 1
        if flag:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    print(*A)
    print(count)

if __name__=='__main__':
    main()