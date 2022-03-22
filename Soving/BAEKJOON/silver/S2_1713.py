# 후보 추천하기
# https://www.acmicpc.net/problem/1713

import sys

sys.stdin = open('input.txt', 'r')
# 사진틀의 개수
N = int(input())
# 전체 학생 총 추천 횟수
total = int(input())
reco_li = list(map(int, input().split()))
photo = []
cnt_d = dict()
for reco in reco_li:
    if len(photo)==N and (reco not in photo):
        min_cnt = 101
        idx = -1
        for p in photo:
            idx += 1
            if cnt_d[p] < min_cnt:
                min_cnt = cnt_d[p]
                min_idx = idx
        b = photo.pop(min_idx)
        cnt_d[b] = 0
    a = cnt_d.get(reco, 0)
    cnt_d[reco] = a + 1
    if reco not in photo:
        photo.append(reco)
photo.sort()
for p in photo:
    print(p, end=' ')