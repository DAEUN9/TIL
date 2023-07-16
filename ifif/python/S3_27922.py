import sys
sys.stdin =open("input.txt", "r")

N, K = map(int, input().split())
videos = [list(map(int, input().split())) for _ in range(N)]
ab, ac, bc = 0, 0, 0
videos.sort(key=lambda x : x[0] + x[1], reverse=True)
for video in videos[:K]:
    ab += video[0] + video[1]
videos.sort(key=lambda x: x[0] + x[2], reverse=True)
for video in videos[:K]:
    ac += video[0] + video[2]
videos.sort(key=lambda x: x[1] + x[2], reverse=True)
for video in videos[:K]:
    bc += video[1] + video[2]
print(max(ab, ac, bc))
