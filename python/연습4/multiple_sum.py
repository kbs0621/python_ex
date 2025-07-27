number_3 = []
for n in range(1, 101):
    print(n)
    if n % 3 == 0:
        number_3.append(n)
        n +=1

number_3_sum = sum(number_3)

count = len(number_3)

print(f"1부터 100까지 3의 배수 : {number_3}")
print(f"3의 배수의 합 : {number_3_sum}")
print(f"3의 배수의 개수 : {count}개")
