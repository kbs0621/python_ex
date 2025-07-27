import json

file_name = 'data.json'

person = {
    "이름" : "김철수",
    "나이" : 25,
    "직업" : "개발자",
    "취미" : ['독서','영화감상','코딩'],
    "주소" : '서울시 강남구'
}

with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(person, file, ensure_ascii=False, indent=4)


print(f'데이터가 {file_name}에 저장되었습니다.')

with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

print("JSON에서 읽어온 데이터 : ")
print(data)