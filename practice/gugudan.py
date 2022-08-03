
def print_gugudan(a):
    for i in range(1,10): print(f"{a} * {i} = {a*i}")

def get_input():
    a = input("숫자를 입력하세요: ")
    if a == "exit":
        return "exit"
    return int(a)

def run_calculator():
    while True:
        a = get_input()
        if a == "exit":
            break
        print_gugudan(a)

run_calculator()