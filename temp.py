def my_decorator(func):
    def w(*args, **kwargs):
        print("Перед вызовом функции")
        #r = func(*args, **kwargs)
        print("После вызова функции")
        return func(*args, **kwargs)
    return w
@my_decorator
def say_hello(a, d):
    print("Привет!")
    return a + d

# Применение декоратора
#decorated_say_hello = my_decorator(say_hello)

# Вызов декорированной функции

print(say_hello(1, 2))