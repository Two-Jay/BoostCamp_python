
# 프로그램 작성 시 조건문에 따른 코드의 실행을 제어하는 방법
#
# if CONDITION:
#     조건이 참이면 실행되는 코드
# else:
#     조건이 거짓이면 실행되는 코드

def play_VOD():
    print("VOD 영상을 재생합니다.")

age = int(input("나이를 입력하시오 : "))
if age >= 18:
    play_VOD()
else:
    print("청소년이므로 VOD 영상을 재생할 수 없습니다.")


# 조건문에서 조건을 여러 개 설정할 수 있다
#
# if CONDITION1:
#     조건1이 참이면 실행되는 코드
# elif CONDITION2:
#     조건2가 참이면 실행되는 코드
# elif CONDITION3:
#     조건3이 참이면 실행되는 코드
# else:
#     조건1,2,3이 모두 거짓이면 실행되는 코드


# is 키워드
#
# if VALUE is VALUE:
#     조건이 참이면 실행되는 코드

def isEquel(a, b):
    if a is b:
        return True
    else:
        return False

a = 1
if isEquel(a, 1): print("입력한 두 값이 같습니다.")
else: print("입력한 두 값이 다르거나, 입력한 값이 없습니다.")

if isEquel(a, 2): print("입력한 두 값이 같습니다.")
else: print("입력한 두 값이 다르거나, 입력한 값이 없습니다.")

