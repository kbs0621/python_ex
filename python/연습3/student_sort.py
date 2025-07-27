student_list = [{"이름" : "김철수", "나이" : 20, "전공" : "컴퓨터공학과"}, {"이름" : "박민수", "나이" : 21, "전공" : "경영학과"}, {"이름" : "이영희", "나이" : 22, "전공" : "영어영문학과"},{"이름" : "최수진", "나이" : 23, "전공" : "수학과"}]

sorted_student_list = sorted(student_list, key=lambda student : student['나이'])

for student in sorted_student_list:
    print(f"{student['이름']}({student['나이']}세)-{student['전공']}")
