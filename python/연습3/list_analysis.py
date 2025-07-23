number = [15,3,27,8,19,12,31]

#for i in number:
#    if i < number:
max_value = max(number)
min_value = min(number)

number_without_max = number.copy()

number_without_max.remove(max_value)

second_max_value = max(number_without_max)

print(f"최댓값 : {max_value}")
print(f"최솟값 : {min_value}")
print(f"두번째로 큰 값 : {second_max_value}")