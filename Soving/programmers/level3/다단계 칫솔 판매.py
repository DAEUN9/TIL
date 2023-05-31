def solution(enroll, referral, seller, amount):
    answer = dict()
    result = []
    tree = dict()
    for child, parent in zip(enroll, referral):
        tree[child] = parent
        answer[child] = 0
    for sell, cnt in zip(seller, amount):
        profit = cnt * 100
        while True:
            temp = int(profit * 0.1)
            if tree[sell] != "-":
                if temp:
                    answer[sell] += profit-temp
                    profit = temp
                else:
                    answer[sell] += profit
                    break
                sell = tree[sell]
            else:
                if temp:
                    answer[sell] += profit-temp
                else:
                    answer[sell] += profit
                break
    for e in enroll:
        result.append(answer[e])

    return result