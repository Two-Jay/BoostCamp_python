# 스텍
# LIFO 자료구조
# push, pop, peek


# 눈감고 스텍 한 번 만들어보기...

class my_stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None
    
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None


from itertools import count
import random as rand

def test_stack():
    print("test_stack===================")
    stack = my_stack()

    stack.push(rand.randint(1, 100))
    print(f"peek : {stack.peek()}")
    print(f"popped : {stack.pop()}")
    stack.push(rand.randint(1, 100))
    print(f"peek : {stack.peek()}")
    stack.push(rand.randint(1, 100))
    print(f"peek : {stack.peek()}")
    stack.push(rand.randint(1, 100))
    print(f"peek : {stack.peek()}")
    stack.push(rand.randint(1, 100))
    print(f"peek : {stack.peek()}")
    print(f"popped : {stack.pop()}")
    print(f"popped : {stack.pop()}")
    print(f"popped : {stack.pop()}")
    print("test_stack_end===============")

test_stack()

# queue
# FIFO 자료구조
# push, pop, peek

class my_queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def peek(self):
        return self.queue[0] if len(self.queue) > 0 else None


# 튜플
# 선언시 () 사용 
# 리스트의 연산, 인덱싱, 슬라이싱 동일하게 사용가능
# 단, 값의 수정은 불가능함

tup = (1, 2, 3)
print(tup)
# tup[0] = 3 # TypeError 오류


# 집합
# 서로 다른 요소를 포함하는 자료구조
# 중복을 허용하지 않음
# 순서가 없음

s = set([rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5), rand.randint(1,5)])
print(f"set : {s}")

s.add(6)
print(f"set : {s}")
s.remove(1) # 없을 시 KeyError
print(f"set : {s}")

s.update([1,6,7,8,9,10])
print(f"set : {s}")

s.discard(3)
print(f"set : {s}")

s.clear()
print(f"set : {s}")
print(type(s))
print("set_end======================")



# 딕셔너리 (해쉬 테이블)
# Key와 Value로 구성된 자료구조
# 중복을 허용하지 않음
# 순서가 없음

country_code = { "대한민국": "KR", "일본": "JP", "중국": "CN", "미국": "US" }

print(country_code)
print(country_code["대한민국"])

country_code["독일"] = "DE"
print(country_code)

# Key 와 Value 만 출력할 수도 있다.
print(country_code.values())
print(country_code.keys())

# in 연산자를 사용하여 키가 있는지 확인
print("대한민국" in country_code)
print("KR" in country_code.values())