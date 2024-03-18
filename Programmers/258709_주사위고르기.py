from itertools import combinations, product
from collections import defaultdict

def solution(dice):
    answer = []
    max_win = 0
    # 주사위 2개 세트로 나누기
    for combi in list(combinations(list(range(len(dice))), len(dice)//2)):
        a_combi = [dice[i] for i in combi]
        b_combi = [dice[i] for i in range(len(dice)) if i not in combi]
        # A, B 각자 주사위 굴려서 나올 수 있는 숫자 합 저장
        A = defaultdict(int)
        for a in product(*a_combi):
            A[sum(a)] += 1
        
        B = defaultdict(int)
        for b in product(*b_combi):
            B[sum(b)] += 1
        
        a_win = 0
        for a in A:
            for b in B:
                if a > b:
                    a_win += A[a] * B[b]
        if a_win > max_win:
            max_win = a_win
            answer = combi

    return [i+1 for i in answer]