from sys import getrecursionlimit, setrecursionlimit

print(getrecursionlimit())

def fn(n):
    if n == 0:
        return
    fn(n-1)

setrecursionlimit(2000)
fn(1998)
print(getrecursionlimit())
