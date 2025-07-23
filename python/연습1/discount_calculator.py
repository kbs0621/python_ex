item = int(input("상품 가격을 입력하세요 : "))
sale = int(input("할인율을 입력하세요(%) : "))

d = item * sale /100

print(f"상품의 원래 가격 :  {item}원")
print(f"할인율 : {sale}%")
print(f"할인 금액 : {d:.0f}원")
print(f"최종 가격 : {item - d:.0f}원")
