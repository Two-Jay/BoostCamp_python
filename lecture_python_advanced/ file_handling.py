# file_open

# open(path, mode)
f = open("test.txt", "w")
f.write("Hello World")
contents = f.read()
print(contents)
f.close()

# with 구문과 함께 활용이 가능하다.
# 인덴테이션 적용되는 구간만 적용
with open("test.txt", "w") as f:
    f.write("Hello World")
    contents = f.read()
    print(contents) # 이 이후에는 자동으로 close()를 호출함


# file 을 read할 시에 read()를 호출하면 모든 내용을 읽어옴
# readline()는 한 줄을 읽어옴
# 줄마다 데이터 양이 상당히 클 때엔 readline() 사용을 고려해 볼 것

with open("test.txt", "r") as f:
    while True:
        line = f.readline() # 메모리 상에 한 줄 씩 로드
        if not line: break
        print(line)

#mode = r, w, a
# r : read
# w : write
# a : append

f = open("count_log.txt", mode = "w", encoding="utf-8")
for i in range(1, 11)
    f.write(f"{i}번째 입니다.\n")
f.close()

with open("count_log.txt", mode = "a", encoding="utf-8") as f:
    for i in range(11, 21):
        f.write(f"{i}번째 입니다.\n")

# 어떻게 될까요 ?!



# pickle 모듈을 사용하여 파일에 저장하고 읽어오기
# pickle 을 활용하면 파이썬에서 활용하는 많은 객체들을 영속화해서 사용할 수 있다.

import pickle
f = open("test.pickle", "wb")
test = [1,2,3,4,5]
pickle.dump(test, f)
f.close()

# 영속화해서 바이너리화 한 뒤 이를 가져와서 사용한다.

f = open("test.pickle", "rb")
test = pickle.load(f)
print(test)
f.close()