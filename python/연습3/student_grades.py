students = {'김철수' : 85, '이영희' : 92, '박민수' : 78, '최수진' : 95}

grades = students.values()

mean_grades = sum(grades) / len(grades)

print("학생 성적 : ")
for name, score in students.items():
    print(f"{name} : {score}점")

print(f"평균 점수 : {mean_grades}점")
