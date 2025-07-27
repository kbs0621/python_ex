num = int(input("숫자를 입력하세요 : "))

if num < 2:
    print(f"{num}은 소수가 아닙니다.")

else:
    is_prime = True
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            is_prime = False
            break

        i += 1
    
    if is_prime:
        print(f"{num}는 소수입니다.")
    else:
        print(f"{num}는 소수가 아닙니다.")