

# split and join
# split: 문자열을 리스트로 분리
# join: 리스트로 된 문자열을 합침

items = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
print(items)

splitted = items.split(',')
print(splitted)

joined = "".join(splitted)
print(joined)



# list comprehension

# [x for x in list] # list에서 x를 추출하여 리스트로 만듦
result = [x for x in range(20) if x % 2 == 0]
print(result)

# 이중 포문 comprehension
word1 = "hello"
word2 = "world"
result = [x + y for x in word1 for y in word2]
print(result)



# filter in for-loop
# filter: 함수를 이용하여 리스트에서 조건을 만족하는 값만 추출

import random as rand

def isEven(x): return x % 2 == 0
result = [i + j for i in range(rand.randint(1, 100)) for j in range(rand.randint(1, 100)) if isEven(i + j)]
print(result)

# filter에 else를 사용하면 조건이 만족하지 않는 값도 추출할 수 있음
result = [i + j if isEven(i + j) else 'BEE' for i in range(rand.randint(1, 100)) for j in range(rand.randint(1, 100))]
print(result)

# enumerate
# enumerate: 리스트의 인덱스와 값을 튜플로 반환

example_source = ["hi there", "hello", "goodbye"]
result = [(i, x) for i, x in enumerate(example_source)]
print(result)

# 값을 언패킹하고 dict로 변환할 수 있음
result = {i : x for i, x in enumerate(example_source)}
print(result)
print(result[0])


# zip
# zip: 두개의 리스트를 합침

alist = [1, 2, 3, 4, 5]
blist = [6, 7, 8, 9, 10]
result = [ [a, b] for a, b in zip(alist, blist) ]
print(result)

math_score = [100, 90, 80, 70, 60]
englist_score = [32, 65, 78, 90, 100]
korean_score = [90, 80, 70, 60, 50]
avrg = [sum(value) / 3 for value in zip(math_score, englist_score, korean_score)]
print(avrg)



# lambda
# lambda: 익명함수

def f(x, y): return x + y
print(f(1, 2)) # 3

f = lambda x, y: x + y
print(f(1, 2)) # 3


# map
# map: 함수를 이용하여 리스트에서 값을 변환

l = [1, 2, 3, 4, 5]
f = lambda x: x * 2
result = list(map(f, l))
print(result)

# map 함수는 매개변수를 2개 이상 사용할 수 있음
# zip 과 비슷!?

l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
f = lambda x, y: x * y
result = list(map(f, l, l2))
print(result)

# reduce
# reduce: 리스트의 값을 하나씩 결합하여 하나의 값을 만듦
# 동일한 함수 하나를 적용

from functools import reduce

lst = [1, 2, 3, 4, 5]
print (reduce(lambda x, y: x + y, lst))
# 인덱스 하나씩 짚으면서 앞의 요소를 x 그 뒤의 요소를 y로 여기고 통합함
# 0 -> 1+2
# 1 -> 3+3
# 2 -> 6+4
# 3 -> 10+5
# print(result) # 15


# 최근에는 map, lambda, reduce 를 쓰는 것을 PEB 상에서 권장하지 않음
# Legacy lib 이나 ML 에서는 아직도 많이 사용중



# iterable object
# 차례대로 순회할 수 있는 객체
# 내부적으로 __iter__ 와 __next__ 메소드를 가짐
# __iter__: 순회할 수 있는 인스턴스를 반환
# __next__: 순회할 수 있는 인스턴스의 다음 값을 반환

cities = [ ("서울", "Seoul"), ("부산", "Busan"), ("대구", "Daegu"), ("인천", "Incheon") ]
memory_address_cities = iter(cities)
print(memory_address_cities)
print(next(memory_address_cities))
print(next(memory_address_cities))
print(next(memory_address_cities))
print(next(memory_address_cities))

# generator
# 순회할 수 있는 객체를 생성하는 함수

def generator_cities(city_list):
    for city in city_list:
        yield city # yield는 이터레이터를 만들어줌
for i in generator_cities(cities): print(i)

# generator comprehension == generator expression
# 순회할 수 있는 list 객체를 생성하는 함수
# [] 대신 ()

gen = (n * n for n in range(20))
print(type(gen))
print(gen)

for i in gen: print(i)
lst = list(gen)
# 위의 두 동작은 실제로 메모리상에 해당 정보를 로드하기 때문에 메모리 사용량이 많이 늘어남
# generator comprehension 을 사용하면 메모리 사용량이 줄어듦 (큰 데이터를 처리할 때는 고려해 볼 것)
