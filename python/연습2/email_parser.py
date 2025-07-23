e_add = input("이메일 주소를 입력하세요 : ")

e_user = e_add.split('@')

print(f"사용자명 : {e_user[0]}")
print(f"도메인 : {e_user[1]}")