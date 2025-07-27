numbers = [1,2,3,4,5,6,7,8,9,10]

squared = map(lambda x : x**2, numbers)
big_num = filter(lambda x : x > 5, numbers)
squared_big_num = map(lambda x : x**2, filter(lambda x : x>5, numbers))

print(f"원본 숫자 : {numbers}")
print(f"모든 수의 제곱 : {list(squared)}")
print(f"5보다 큰 수들 : {list(big_num)}")
print(f"5보다 큰 수들의 제곱 : {list(squared_big_num)}")