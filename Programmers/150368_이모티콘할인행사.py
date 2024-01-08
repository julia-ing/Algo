from itertools import product

def solution(users, emoticons):
    discount = [10,20,30,40]
    answer = [0,0]
    # 이모티콘 수만큼 할인율 조합 만들기
    for dis in product(discount, repeat=len(emoticons)):
        plus = 0
        total_pay = 0
        for ratio, limit in users:
            pay = 0
            for i, price in enumerate(emoticons):
                if ratio <= dis[i]:
                    pay += price * (100-dis[i]) // 100
            if pay >= limit:
                plus += 1
            else:
                total_pay += pay
        # 이모티콘 플러스 가입자가 더 크면 갱신
        if answer[0] < plus:
            answer = [plus, total_pay]
        # 판매액이 더 크면 갱신
        elif plus == answer[0] and answer[1] < total_pay:
            answer[1] = total_pay
    return answer
