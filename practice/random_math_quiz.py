import random as rand

def set_answer(fr, to): return rand.randint(fr, to)

def ask_answer(answer):
    while True:
        guess = input("숫자를 입력하세요: ")
        if guess == "exit": break
        guess = int(guess)
        if guess == answer: return print("정답입니다.")
        elif guess < answer: print("입력한 숫자가 너무 작습니다.")
        else: print("입력한 숫자가 너무 큽니다.")

def run_quiz():
    answer = set_answer(1, 100)
    ask_answer(answer)

run_quiz()