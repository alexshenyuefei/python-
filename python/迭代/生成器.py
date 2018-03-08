
def fib(n):
    prev, curr = 0, 1
    while n > 0:
        n -= 1
        yield curr
        prev, curr = curr, curr + prev
a =fib(12) # 生成器只能用一次
for i in a:
    print(i)

for i in a:
    print(i)