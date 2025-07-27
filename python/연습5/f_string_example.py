import datetime


name = '김철수'
age = 25
pi = 3.14159
price = 1234
percent = 0.855
today = datetime.date(2025,7,20)

print(f"이름 : {name}, 나이 : {age}")
print(f"원주율 : {pi:.02f}")
print(f"가격 : {price:,}원")
print(f"퍼센트 : {percent:.2%}")
print(f"날짜 : {today.strftime("%Y년 %m월 %d일")}")