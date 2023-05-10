import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B, C = map(int, input().split())
basics = dict()
specials = dict()
services = dict()
for _ in range(A):
    name, price = input().split()
    basics[name] = int(price)
for _ in range(B):
    name, price = input().split()
    specials[name] = int(price)
for _ in range(C):
    name = input().strip()
    services[name] = 1

N = int(input())
basic_price = 0
special_price = 0
service_check = 0
for _ in range(N):
    menu = input().strip()
    if basics.get(menu):
        basic_price += basics[menu]
    elif specials.get(menu):
        special_price += specials[menu]
    else:
        service_check += 1
answer = "Okay"
if special_price:
    if basic_price < 20000:
        answer = "No"
if service_check:
    if service_check > 1:
        answer = "No"
    if basic_price+special_price < 50000:
        answer = "No"
print(answer)