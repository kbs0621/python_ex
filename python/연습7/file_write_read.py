text = '안녕하세요. \n' '파이썬 파일 처리를 연습하고 있습니다. \n' '오늘은 좋은 날씨입니다'

print("파일에 저장할 내용 : ")
print(text)

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("파일 내용에서 읽어온 내용")
print(content)