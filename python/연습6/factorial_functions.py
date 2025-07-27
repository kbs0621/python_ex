def factorial_self(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_self(n-1)



def factorial_iterat(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a


num = int(input("숫자를 입력하세요 : "))
result = factorial_self(num)
result1 = factorial_iterat(num)

print(f"{num}!(재귀) = {result}")
print(f"{num}!(반복) = {result1}")