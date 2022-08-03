
def print_gugudan(a):
    for i in range(1,10): print(f"{a} * {i} = {a*i}")

def get_input():
    a = input("숫자를 입력하세요: (종료 : 'exit')")
    if a == "exit": return "exit"
    return int(a)

def run_calculator():
    while True:
        a = get_input()
        if a == "exit": break
        if a < 1 or a > 9: print("숫자는 1에서 9 사이여야 합니다.")
        else : print_gugudan(a)

run_calculator()