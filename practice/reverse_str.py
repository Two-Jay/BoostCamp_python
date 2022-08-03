import sys
sys.path.append("/Users/kimjeongjun/BoostCamp_python/data_structure")
import stack

def reverse_str(str) -> str:
    st = stack.my_stack()
    for c in str: st.push(c)
    reversed_str = ""
    while st.peek(): reversed_str += st.pop()
    return reversed_str

def get_input() -> str:
    str = input("뒤집을 문자열을 입력하세요 (종료 : 'exit'): ")
    return str

def run_reverser():
    while True:
        str = get_input()
        if str == "exit": break
        print(f"뒤집은 문자열: {reverse_str(str)}")

run_reverser()