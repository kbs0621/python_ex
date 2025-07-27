import math_operations

def main():
    r = 5
    w,l = 10,5
    f=5
    x,y = 48,18

    print(f"반지름이 {r}인 원의 넓이 = {math_operations.circle_calculator(r)}")
    print(f"가로가 {w}, 세로가 {l}인 직사각형의 넓이 = {math_operations.rectangle_calculator(w,l)}")
    print(f"{f}! = {math_operations.factorial_fucntions(f)}")
    print(f"최대공약수({x},{y}) = {math_operations.gcd(x,y)}")

if __name__ == "__main__":
    main()
    