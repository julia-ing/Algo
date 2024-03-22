def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    dictionary = {} # 시간초과 방지용 딕셔너리
    for i in range(len(enroll)):
        dictionary[enroll[i]] = i
    for i in range(len(seller)):
        money = amount[i] * 100
        while seller[i] != "-" and money > 0:
            idx = dictionary[seller[i]]
            answer[idx] += money - money//10
            money //= 10
            seller[i] = referral[idx]
    return answer