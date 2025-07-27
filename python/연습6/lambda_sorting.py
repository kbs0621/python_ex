student_list = [('김철수',85),('이영희',92),('박민수',78),('최수진',95)]

name_sorted = sorted(student_list, key=lambda x : x[0])
score_sorted = sorted(student_list, key=lambda x : x[1])
score_desc_sorted = sorted(student_list, key=lambda x : x[1], reverse=True)

print(f"학생 정보 : {student_list}")
print(f"이름순 정렬 : {name_sorted}")
print(f"점수순 정렬 : {score_sorted}")
print(f"점수 내림차순 정렬 : {score_desc_sorted}")
