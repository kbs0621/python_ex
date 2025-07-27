number = []

n = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
while True:
    if n == 0:
        break
    else:
        number.append(n)
        n = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))

print(f"입력된 숫자들 : {number}")
print(f"입력된 숫자들의 합 : {sum(number)}")