from datetime import datetime
import random

fruit_list = ['사과', '바나나','체리','포도','딸기']

now = datetime.now()

random_int = random.randint(1,100)
random_float = random.uniform(1.0,4.0)
random_value = random.choice(fruit_list)
random.shuffle(fruit_list)

print(f"현재 날짜와 시간 : {now}")
print(f"포맷된 날짜 : {now.strftime("%Y년 %m월 %d일")}")
print(f"임의의 숫자 : {random_int}")
print(f"임의의 실수 : {random_float}")
print(f"임의의 리스트 요소 : {random_value}")
print(f"섞인 리스트 : {fruit_list}")
