students = ['김철수', '이영희', '박민수', '최수진']
scores = [85,92,78,95]

for a,b in zip(students, scores):
    print(f"{a}: {b}점")