a = [1, 2, 3]
b = [4, 5, 6]
c = 'abc'
res = tuple(map(lambda *args: args, a, b, c))
print(res)

