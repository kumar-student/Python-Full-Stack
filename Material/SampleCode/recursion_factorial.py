# factorial
# 5! = 5*4!
# 5! = 5*4*3!
# 5! = 5*4*3*2!
# 5! = 5*4*3*2*1!
# 5! = 5*4*3*2*1
factorial = 1
for i in range(10, 0, -1):
    factorial = factorial*i
print("Factorial using for loop: ", factorial)

def fn(n):
    if n == 1:
        return n
    return n*fn(n-1)
print(fn(5))