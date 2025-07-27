number = [10,20,30,40,50]

def static(list):
    list_mean = sum(list) / len(list)
    list_max = max(list)
    list_min = min(list)
    variance = sum((x - list_mean) ** 2 for x in list) / (len(list) - 1)
    list_std = variance ** 0.5

    print(f"평균 : {list_mean}")
    print(f"최댓값 : {list_max}")
    print(f"최솟값 : {list_min}")
    print(f"표준편차 : {list_std:.02f}")

static(number)