
# 기본적인 반복문
# for looper in [1,2,3,4,5]:
#     print(looper)
#
# 반복문이 한 스텝 수행될 때마다 리스트의 값이 looper에 할당된다.

for looper in [1,2,3,4,5]:
     print(f"Hello {looper}")

# 만약의 큰 수를 반복문 시전시 필요한 경우 range() 함수를 사용할 수 있다.

print("hello one to hundred")
for looper in range(1,100):
    print(f"Hello {looper}")


# break 문을 사용하여 반복문을 중단할 수 있다.
for i in range(100):
    if i == 50:
        break
    print(i)
print("reached 50")

# continue 문을 사용하여 반복문을 건너뛴다.
for i in range(100):
    if i % 2 is 1:
        continue
    print(i)

# while 문을 사용하여 조건이 참일 때에 반복문을 사용할 수 있다.
# while 조건:
#     수행할 문장

a = 0
while a < 10:
    print(a)
    a += 1
