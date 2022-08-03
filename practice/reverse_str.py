# import sys
# sys.path.append("/Users/kimjeongjun/BoostCamp_python/data_structure")
# import stack

class my_stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None
    
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

def reverse_str(str) -> str:
    st = my_stack()
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