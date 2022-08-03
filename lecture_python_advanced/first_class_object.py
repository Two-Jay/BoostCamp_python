# first-class object (일등함수 혹은 일급 객체)

# 변수나 데이터 구조에 할당이 가능한 '객체'
# 파라미터로 전달이 가능 + 리턴값으로 활용
# 파이썬의 함수는 일급함수이다.

def square(x): return x * x
f = square # 함수를 변수로 활용
print(f(5)) # 25
print(type(f)) # <class 'function'>
# f 를 올려주어도 square를 활용하는 것과 똑 같음

def square(x): return x * x
def cube(x): return x * x * x
def formula(method, argument_list):
    return [method(value) for value in argument_list]

f = formula
print(f(square, [1,2,3,4,5])) # 함수를 파라미터로 사용 
print(f(cube, [1, 2, 3, 4, 5])) 

# inner function
# 함수 내에 또 다른 함수를 만들 수 있음

def print_msg(msg):
    def print_it(): print(msg) # 함수 안에 함수를 정의 및 활용 가능
    return print_it

another = print_msg("Hello")
another() # Hello


# closure
# 함수를 만들 때, 함수 내에서 다른 함수를 만들고 이를 리턴 할 수 있음

def tag(tag, txt):
    def wrap(): print("<{0}>{1}</{0}>".format(tag, txt)) # 함수 내부에서 정의된 함수가...
    return wrap # ... 정의된 함수에서 리턴됨

h1_func = tag("h1", "Hello")
p_func = tag("p", "World")

h1_func()
p_func()