def main():
    N = int(input())
    A = list(map(Card,input().split()))
    # print(" ".join([card.card for card in A]))
    bubble = bubblesort(A.copy(), N)
    print(" ".join([card.card for card in bubble]))
    isStable(A, bubble, N)
    selection = selectionsort(A.copy(), N)
    print(" ".join([card.card for card in selection]))
    isStable(A, selection, N)
    


def isStable(before, after, N):
    counter = 0
    for i in range(N-1):
        if after[i].value==after[i+1].value:
            counter += 1
            for j in range(N):
                count = 1
                if before[j].value==after[i].value:
                    if count!=counter:
                        count += 1
                        continue
                    if before[j].mark != after[i].mark:
                        # before[j].printcard()
                        # after[i].printcard()
                        print("Not stable")
                        return False
                    else: break
        else: counter=0
    print("Stable")

class Card:
    def __init__(self, card):
        self.mark = card[0]
        self.value = int(card[1])
        self.card = card
    
    def printcard(self):
        print(self.card)

def bubblesort(A, N):
    sorted = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(N-1, sorted, -1):
            if A[i].value<A[i-1].value:
                A[i],A[i-1] = A[i-1],A[i]
                flag = 1
        sorted += 1
    return A

def selectionsort(A, N):
    count = 0
    for i in range(N):
        minj = i
        flag = 0
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
                flag = 1
        if flag:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    return A

if __name__=='__main__':
    main()