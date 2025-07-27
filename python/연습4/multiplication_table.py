multi = int(input("몇 단을 출력할까요? "))

print(f"{multi}의 구구단 : ")
for i in range(1,10):
    print(f"{multi} x {i} =", multi * i)