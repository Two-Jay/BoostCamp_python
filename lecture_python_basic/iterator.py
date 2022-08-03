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
