# Exception

# try:
#     print(a)
# except NameError:
#     print("에러가 발생했습니다.")


for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError: # exception 처리시에는 어떤 에러를 처리할 것인지 명확히 해야한다.
        print("0으로 나눌 수 없습니다.")
    except Exception as e: # 이와 같이 Exception 을 특정하지 않고도 잡을 수는 있다.
        # 그러나 디버깅하기 좋은 코드가 아님을 명심할 것.
        print(e)
        print("에러가 발생했습니다.")
        break
    else: # try 이후에 exception 에 해당되지 않으면 처리하는 코드를 작성 가능
        print("정상적으로 처리되었습니다.")
        break
    finally: #  exception 여부와 상관없이 처리하는 코드를 작성 가능
        print("처리가 끝났습니다.")
        break

# if vs try-except
# if는 로직 컨트롤
# try-except는 예외 처리