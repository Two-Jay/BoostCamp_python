

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







