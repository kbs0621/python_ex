numbers1 = [2,4,6,8,10]
numbers2 = [1,3,5,7,12]


def all_even(num):
    q1 = all(n % 2 == 0 for n in num)
    return q1

def any_ten(num):
    q2 = any(n > 10 for n in num)
    return q2

print(f"모든 수가 짝수인가? {all_even(numbers1)}")
print(f"하나라도 10보다 큰 수가 있는가? {any_ten(numbers1)}")

print(f"모든 수가 짝수인가? {all_even(numbers2)}")
print(f"하나라도 10보다 큰 수가 있는가? {any_ten(numbers2)}")
