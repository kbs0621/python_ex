grade = int(input("점수를 입력하세요 : "))

if grade >= 90:
    print(f"점수 {grade}점의 학점은 A입니다.")
elif grade >= 80:
    print(f"점수 {grade}점의 학점은 B입니다.")
elif grade >= 70:
    print(f"점수 {grade}점의 학점은 C입니다.")
elif grade >= 60:
    print(f"점수 {grade}점의 학점은 D입니다.")
else:
    print(f"점수 {grade}점의 학점은 F입니다.")