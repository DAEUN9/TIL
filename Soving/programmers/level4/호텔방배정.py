def solution(k, room_number):
    answer = []
    d = dict()
    for room in room_number:
        num = d.get(room, 0)
        if num == 0:
            d[room] = room + 1
            answer.append(room)
            continue

        while num:
            temp = d.get(num, 0)
            if temp:
                d[num] = max(temp, num + 1)
                num = temp
            else:
                d[num] = max(temp, num + 1)
                break
        d[room] = num + 1
        answer.append(num)

    return answer