def check_colours(colour, colours):
    if colour in colours:
        print('that is in amount')
    else:
        print('that is not in amount')    



colours = ['red', 'blue', 'green']
add_colours = ['yellow', 'orange', 'purple']

print(colours[1])
print(colours[2])
print(colours)

# append
amount = colours + add_colours
print(amount)
if "blue" in amount:
    print('blue is in amount')

check_colours('black', colours)
colours.append('black')
check_colours('black', colours)


# 슬라이스
cities = ['seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan', 'gyeonggi', 'gangwon', 'chungbuk', 'chungnam', 'jeonbuk', 'jeonnam', 'gyeongbuk', 'gyeongnam', 'jeju']

print(cities[3:])
print(cities[0:3]) # when slicing, the end index is not included

print(cities[::-1]) #   reverse the list
print(cities[::3]) #   every third element


# 리스트의 변수와 뮤터빌리티
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(a)
print(b)

# 이렇게 되는 경우 동일한 메모리영역을 가리킨다
# b의 수정이 a에도 영향을 미친다

a = b
print(a)
print(b)
print(id(b))
print(id(a))
b.sort()
print(b)
print(a)



# 리스트의 수정과 깊은 복사

kor_score = [100, 92, 80, 70, 60]
eng_score = [100, 92, 58, 69, 31]
math_score = [89, 53, 67, 45, 100]
mid_scores = [kor_score, eng_score, math_score]

print(mid_scores)
mid = mid_scores
print(mid)

print(id(mid))
print(id(mid_scores))

# 동일한 메모리영역을 가리키기 때문에
# mid_scores의 수정이 mid에도 영향을 미친다
mid_scores[0][3] = 90
print(mid_scores)
print(mid)

# 따라서 이중배열에서 복사를 위해서는
# deepcopy를 사용해야 한다
# copy 모듈을 사용해야 한다

import copy

mid = copy.deepcopy(mid_scores)
print(id(mid))
print(id(mid_scores))
# 두 리스트의 주소가 다르다
mid_scores[0][3] = 83
print(mid_scores) # [[100, 92, 80, 83, 60], ...
print(mid) # [[100, 92, 80, 90, 60], ...


