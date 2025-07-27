score = 85
result = "합격" if score >= 80 else "탈락"

age = 17
result1 = "성인" if age >= 19 else "미성년자"

list_n = [42,10,3,23,17]
result2 = max(list_n) 


list_n1 = [5,12,8,23,-17,0,-75]
result3 = [n for n in list_n1 if n >0]



print(f"점수 : {score}, 결과 : {result}")
print(f"나이 : {age}, 상태 : {result1}")
print(f"숫자들의 최대값 : {result2}")
print(f"양수들 : {result3}")

