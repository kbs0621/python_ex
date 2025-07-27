list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

list3 = sorted(set(list1+list2))
list4 = sorted(set(list1) & set(list2))

print(f"리스트 1 : {list1}")
print(f"리스트 2 : {list2}")
print(f"병합된 리스트 : {list3}")
print(f"공통 요소 : {list4}")

