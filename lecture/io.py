
name = input("Enter your name : ")
print("Hello, ", name)
print(type(name))


age = int(input("Enter your age : "))
# 기본적으로 입력된 문자열은 문자열 형태로 입력된다
# 문자열을 숫자로 변환하려면 int() 함수를 사용한다
print("Hello, ", name, "! You are ", age, "years old.")
print("after 10 years, you will be ", age + 10, "years old.")
print(type(age))


# print formatting
# 1. %s String
# 2. format()
# 3. fstring

print(1,2,3)
print("1" + " " + "2" + " " + "3")
print("%d %d %d" % (1,2,3))
print("{} {} {}".format(1,2,3))
print(f"value is {1} {2} {3}")

# %Datatype %(value) 의 형식에서는 정밀도를 설정할 수 있다
print("%d %.1f %.1f" % (1, 2.345, 3.456))

# fstring - python 3.6 이상
# f"{value}"

name = "jekim"
age = 30

print(f"hello, {name}! you are {age} years old.")
print(f"{name:*>20}")
print(f"{name:*<20}")
print(f"{name:*^20}")

pi = 3.141592
print(f"pi is {pi:.2f}")