from string import ascii_lowercase
from string import ascii_uppercase
def solution(s, n):
    answer = ''
    lower_list=list(ascii_lowercase)*2
    upper_list=list(ascii_uppercase)*2
    for i in s:
        if i in lower_list:
            answer+=lower_list[lower_list.index(i)+n]
        elif i in upper_list:
            answer+=upper_list[upper_list.index(i)+n]
        else:
            answer+=" "
    return answer