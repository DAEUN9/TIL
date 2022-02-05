x, y, w, h = map(int,input().split())

a = x if x <= abs(x-w) else abs(x-w)
b = y if y <= abs(y-h) else abs(y-h)

c = a if a<=b else b
print(c)