# 해시
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    total={}
    gen_dic={}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else:
            total[genres[i]]=plays[i]
            gen_dic[genre]=[(play,i)]

        
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    
    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i==2:
                break
            answer.append(playlist[i][1])
    return answer