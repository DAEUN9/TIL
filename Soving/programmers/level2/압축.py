def solution(msg):
    answer = []
    d = dict()
    curr = 0
    i = 0
    for i in range(97-32, 123-32):
        curr += 1
        d[chr(i)] = curr
        
    answer = [0]
    value = 26
    base = ""

    for i in range(len(msg)):
        base += msg[i]
        if not base in d:
            value += 1
            d[base] = value

            base = msg[i]
            answer.append(d[base])

        else:
            answer[-1] = d[base]
    return answer
        
