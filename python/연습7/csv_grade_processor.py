import csv

file_name = 'grades.csv'

grades = [('김철수',85),('이영희',92),('박민수',78),('최수진',95)]

with open(file_name, 'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['이름','점수'])
    writer.writerows(grades)

print(f"학생 성적이 {file_name}에 저장되었습니다. \n")

with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    scores = []
    print("성적 분석 결과 : ")
    for row in reader:
        name = row['이름']
        score = int(row['점수'])
        scores.append(score)

        print(f"{name} : {score}점")


score_mean = sum(scores) / len(scores)

print(f"전체 평균 : {score_mean:.1f}점")