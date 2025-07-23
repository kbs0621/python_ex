s = input("문자을 입력하세요 : ")

a = s.strip()
b = s.split()

print(f"공백 제거 : {a}")
print(f"단어 개수 : {len(b)}개")
