students = {'김철수' : 85, '이영희' : 92, '박민수' : 78, '최수진' : 95}

grades = students.values()

mean_grades = sum(grades) / len(grades)

print(f"학생 성적 : {students.keys()} : {students.values()}점")
print(f"평균 점수 : {mean_grades}점")
