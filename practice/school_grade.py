def check_school_grade_by_age(age):
    if age <= 26 and age >= 20: print("대학생입니다.")
    elif age < 20 and age >= 17: print("고등학생입니다.")
    elif age < 17 and age >= 14: print("중학생입니다.")
    elif age < 14 and age >= 8: print("초등학생입니다.")
    else: print("학생이 아닙니다.")

birth_year = int(input("태어난 년도를 입력하시오 : "))
age = 2022 - birth_year + 1
check_school_grade_by_age(age)