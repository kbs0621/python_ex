point = (10,20)
x,y = point
print(f"좌표 : x={x}, y={y}")

values = [1,2,3]
a,b,c = values
print(f"리스트 언패킹 : a={a},b={b},c={c}")

def sum_args(*args):
    return sum(args)

total = sum_args(10,20,30)

print(f"가변 인수의 합 : {total}")

def print_kwargs(**kwargs):
    output = ','.join(f"{key}={value}" for key, value in kwargs.items())
    print(f"키워드 인수들 : {output}")

print_kwargs(name='김철수', age=25, city='서울')