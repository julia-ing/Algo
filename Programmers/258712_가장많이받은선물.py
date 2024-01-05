from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    info = defaultdict(list)
    score = {}
    for f in friends:
        score[f] = 0

    for gift in gifts:
        giver, taker = gift.split()
        score[giver] += 1
        score[taker] -= 1
        info[giver].append(taker)
    
    for giver in friends:
        total = 0
        for taker in friends:
            if giver == taker:
                continue
            give_cnt = info[giver].count(taker)
            take_cnt = info[taker].count(giver)
            if give_cnt == take_cnt:
                # 선물 지수 비교
                if score[giver] > score[taker]:
                    total += 1
            elif give_cnt > take_cnt:
                total += 1
        answer = max(answer, total)
    return answer
