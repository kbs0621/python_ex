

with open('text1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 현재 words 리스트 ['파이썬', '프로그래밍','언어', '배우기', '쉬운', '강력한', '파이썬', '프로그래밍', '언어', '파이썬']
words = content.split()

# 단어 딕셔너리에 단어와 횟수 저장
word_counts = {}

# words 리스트에 word를 확인해서 word_counts 딕셔너리에 word가 들어가고, 횟수를 1개 늘린다 
# word_counts = {"word1" : 1, "word2" "3", ...}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("단어 빈도 분석 결과 : ")
for word, count in word_counts.items():
    print(f"{word} : {count}번")
