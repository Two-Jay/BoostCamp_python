from collections import deque
import time

def deque_time_test(test_limit):
    start_time = time.perf_counter()
    deque_list = deque()

    # 추가
    for i in range(test_limit):
        for i in range(test_limit):
            deque_list.append(i)
            deque_list.pop()
    print(f"deque : {time.perf_counter() - start_time} seconds")

def general_list_time_test(test_limit):
    start_time = time.perf_counter()
    list_list = []

    # 추가
    for i in range(test_limit):
        for i in range(test_limit):
            list_list.append(i)
            list_list.pop()
    print(f"list : {time.perf_counter() - start_time} seconds")


while True:
    test_limit = input("deque vs general_list_____\n시험 개수 (종료 = 'exit'): ")
    if test_limit == "exit": break # 종료
    else:
        test_limit = int(test_limit)
        deque_time_test(test_limit)
        general_list_time_test(test_limit)
