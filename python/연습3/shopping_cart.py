shopping_cart = {
    '사과': {'수량': 2, '가격': 1000},
    '바나나': {'수량': 3, '가격': 800},
    '오렌지': {'수량': 1, '가격': 1500}
}

print("쇼핑 카트:")

total_price = 0

for product, info in shopping_cart.items():
    quantity = info['수량']
    price_per_item = info['가격']
    item_total = quantity * price_per_item
    total_price += item_total
    print(f"{product}: {quantity}개 (개당 {price_per_item}원) = {item_total}원")

print(f"총 가격: {total_price}원")
