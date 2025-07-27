import math

number_dict = {}
even_dict = {}

for i in range(1,6):
    number_dict[i] = i**2

for j in range(2,11,2):
    even_dict[j] = j**2

print(f"1부터 5까지의 제곱 딕셔너리 : {number_dict}")
print(f"짝수만의 제곱 딕셔너리 : {even_dict}")
