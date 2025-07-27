def greet(name, greeting = "안녕하세요", text = '님!'):
    print(f"{greeting}, {name}{text}")



greet("김철수")
greet(greeting='Hello', name='John')
greet(name = "이영희", text = "님! 좋은 하루 되세요!")
