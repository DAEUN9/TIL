def solution(n, k, cmd):
    answer = ''
    array = [[-1, 1, False]]
    for i in range(1, n-1):
        array.append([i-1, i+1, False])
    array.append([n-2, -1, False])
    curr = k
    deleted = []
    for cm in cmd:
        if len(cm) == 1:
            if cm =="C":
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
                while array[re][0] != -1:
                    if not array[prev][2]:
                        next = array[prev][1]
                        array[prev][1] = re
                        array[next][0] = re
                        array[re][0] = prev
                        array[re][1] = next
                        break
                    if array[prev][0] == -1:
                        array[re][0] = -1
                        while array[re][1] != -1:
                            if not array[next][2]:
                                prev = array[next][0]
                                array[prev][1] = re
                                array[next][0] = re
                                array[re][0] = prev
                                array[re][1] = next
                                break

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
solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])