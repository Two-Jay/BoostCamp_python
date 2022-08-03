
# function 에 parameter 를 전달하는 방법

# 1. keyword arguments
# 2. default arguments
# 3. variable-length arguments


# 1. keyword arguments

def print_hello(name : str, age : int) -> None:
    print(f"Hello, {name}! You are {age} years old.")

print_hello(age = 20, name = "John")
# 지정한 키워드에 값을 집어넣을 수 있음, 순서 상관없이 넣을 수 있다.


# 2. default arguments
def print_hello_default(name : str = "John", age : int = 20) -> None:
    print(f"Hello, {name}! You are {age} years old.")

print_hello_default()
print_hello_default(name="Jane")
print_hello_default(age=30)

#지정한 값을 따로 넣지 않아도, 함수가 실행이 되며, 기본값이 적용된다.

# 3. variable-length arguments (asterisk : *)
# 입력된 값은 튜플로 사용가능


def asterisk_test(a, b, *args):
    print(list(args))
    print(type(args))
    print(args[0])
asterisk_test(1,2,3,4,5)

# 4. keyword valiable-length arguments
# 입력된 값은 딕셔너리로 사용가능

def kwarg_test(a, b, **kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["name"])
    return a + b + kwargs["age"]
print(kwarg_test(1,2,name="John", age=20))

# 3과 4는 *로 언패킹하는 것이 가능하다.

def asterisk_test(a, b, *args):
    print(a, args) # 1 (3,4,5)
    print(a, *args) # 1 3 4 5
    print(args[0]) # 3
asterisk_test(1,2,3,4,5)    

# asterisk 를 이용해 zip을 활용할 때에도 언패킹 가능하다

ex = ([1,2,3],[4,5,6])
a,b = ex
for value in zip(a,b): print(value)
# 위의 코드는 아래의 코드와 기능이 같다.
ex = ([1,2,3],[4,5,6])
for value in zip(*ex): print(value)\