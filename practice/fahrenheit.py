
def print_banner():
    print("python fahrenheit.py")
    print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")

def get_input():
    fahrenheit = input("섭씨온도를 입력하세요: ")
    if fahrenheit == "exit":
        return "exit"
    return float(fahrenheit)

def convert_fahrenheit(fahrenheit):
    return (9 / 5) * fahrenheit + 32

print_banner()
while True:
    fahrenheit = get_input()
    if fahrenheit == "exit":
        break
    fahrenheit = float(fahrenheit)
    print(f"섭씨온도 : {fahrenheit:.2f}")
    print(f"화씨온도 : {convert_fahrenheit(fahrenheit):.2f}")