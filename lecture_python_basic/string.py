
# 문자열
# 시퀀스 자료형으로 문자형 데이터를 메모리에 저장함
# 영문은 1byte, 한글은 3byte
# 한글의 경우 유니코드 처리를 위해 추가적으로 기본 메모리 사용량이 다름

import sys
print(sys.getsizeof('a'), sys.getsizeof('abc'), sys.getsizeof('안녕')) # 50, 52, 78

test_str = "Hello World"
print(test_str)
print(test_str[0]) # h
print(test_str[-1]) # d
print(test_str[0:3]) # hel
print(test_str[0:]) # hello world
print(test_str[:3]) # hel
print(test_str[3:]) # lo world
print(test_str[-3:]) # rld


# 두 줄 이상의 문자열을 할당하는 방법

test_str_long = """
안녕하세요
반갑습니다
"""
print(test_str_long)

test_str_long1 = "안녕 \n반갑 \n감사"
print(test_str_long1)


# 문자열 함수를 사용할 수 있다.

# len() 함수를 사용하여 문자열의 길이를 확인할 수 있다.
length = len(test_str)
print(length) # 11

# upper() 함수를 사용하여 문자열의 모든 문자를 대문자로 변환할 수 있다.
print(test_str.upper()) # HELLO WORLD

# lower() 함수를 사용하여 문자열의 모든 문자를 소문자로 변환할 수 있다.
print(test_str.lower()) # hello world

# capitalize() 함수를 사용하여 문자열의 첫번째 문자를 대문자로 변환할 수 있다.
print(test_str.capitalize()) # Hello world

# swapcase() 함수를 사용하여 문자열의 모든 문자를 대소문자를 변환할 수 있다.
print(test_str.swapcase()) # hELLO wORLD

# title() 함수를 사용하여 문자열의 모든 문자를 대문자로 변환할 수 있다.
print(test_str.title()) # Hello World

# count() 함수를 사용하여 문자열에서 특정 문자가 몇 개 있는지 확인할 수 있다.
print(test_str.count('o')) # 2

# find() 함수를 사용하여 문자열에서 특정 문자가 처음 등장하는 위치를 확인할 수 있다.
# 못 찾을 시에는 -1을 반환한다.
print(test_str.find('o')) # 4
print(test_str.find('z')) # -1

# index() 함수를 사용하여 문자열에서 특정 문자가 처음 등장하는 위치를 확인할 수 있다.
# 못 찾을 시에는 ValueError를 발생시킨다.
print(test_str.index('o')) # 4
# print(test_str.index('z')) # ValueError

# startswith() 함수를 사용하여 문자열이 특정 문자열로 시작하는지 확인할 수 있다.
print(test_str.startswith('He')) # True
print(test_str.startswith('he')) # False

# endswith() 함수를 사용하여 문자열이 특정 문자열로 끝나는지 확인할 수 있다.
print(test_str.endswith('ld')) # True
print(test_str.endswith('z')) # False

