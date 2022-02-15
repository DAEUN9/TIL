def star(x):
    if x == 1:
        return ['*']
    x = x // 3
    a = star(x)
    topbottom = [i * 3 for i in a]
    middle = [i + ' ' * x + i for i in a]
    return topbottom + middle + topbottom

n = int(input())
mystar = '\n'.join(star(n))
print(mystar)