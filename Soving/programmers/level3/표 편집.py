def solution(n, k, cmd):
    answer = ''
    array = [[-1, 1, False]]
    for i in range(1, n - 1):
        array.append([i - 1, i + 1, False])
    array.append([n - 2, -1, False])
    curr = k
    deleted = []
    for cm in cmd:
        if len(cm) == 1:
            if cm == "C":
                deleted.append(curr)
                array[curr][2] = True
                prev = array[curr][0]
                next = array[curr][1]
                if array[curr][1] == -1:
                    curr = prev
                    array[prev][1] = -1
                else:
                    array[prev][1] = next
                    array[next][0] = prev
                    curr = next
            else:
                re = deleted.pop()
                prev = array[re][0]
                next = array[re][1]
                array[re][2] = False
                if prev != -1:
                    array[prev][1] = re
                if next != -1:
                    array[next][0] = re


        else:
            dr, cnt = cm.split()
            d = 1
            if dr == "U":
                d = 0
            for i in range(int(cnt)):
                curr = array[curr][d]

    for a, b, bo in array:
        if bo:
            answer += 'X'
        else:
            answer += 'O'
    return answer