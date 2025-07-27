import math
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
squared_even = []

for num in numbers:
    if num % 2 ==0:
        even_numbers.append(num)
        squared_even.append(math.pow(num, 2))

print(f"원본 리스트 : {numbers}")
print(f"짝수의 리스트 : {even_numbers}")
print(f"짝수의 제곱 리스트 : {squared_even}")

