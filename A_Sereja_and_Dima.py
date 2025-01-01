
def func(cards, turn, score, l, r):

    if l > r:
        return score

    if cards[l] >= cards[r]:
        score[turn]+=cards[l]
        l+=1
    else:
        score[turn]+=cards[r]
        r-=1
    return func(cards, 1-turn, score, l, r)


n = input()  
cards = list(map(int, input().split()))
score =  func(cards, 0, [0,0], 0, len(cards)-1)
print(*score)

