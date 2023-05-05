import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
A, B, C = map(int, input().split())
specials = dict()
basics = dict()
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
service_check = 0
basic_price = 0
special_price = 0
for _ in range(N):
    menu = input().strip()
    if basics.get(menu):
        basic_price += basics.get(menu)
    elif specials.get(menu):
        special_price += specials.get(menu)
    else:
        service_check += 1
order = "Okay"
if special_price:
    if basic_price < 20000:
        order = "No"
if service_check == 1:
    if basic_price + special_price < 50000:
        order = "No"
if service_check >= 2:
    order = "No"
print(order)
