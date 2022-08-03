# ? : 수강신청을 하는 프로그램을 작성해야한다.
# 어떻게 해야할까?
# 1. 수강신청의 플로우를 시작부터 끝까지 순서대로 작성
# 혹은
# 2. 수강신청의 주체들을 작성하고, 이들의 행동과 데이터를 중심으로
# 수강신청의 플로우를 작성하고 연결


# #############################################################################
# 축구 선수 정보를 클래스로 구현하기

# 클래스 네이밍은 카멜케이스를 사용한다
class SoccerPlayer(object): # object는 여기서 상속받는 객체명을 의미한다
    def __init__(self, name, back_number, position): # 생성자
        # 생성자 내부에서 속성을 결정해준다
        # 속성에서 내부적으로 사용하는 변수가 있다면 _ 를 붙여준다
        # 기본적으로 속성은 모두 public으로 설정된다
        # 메소드나 속성을 private으로 설정하려면 __ 를 붙여준다
        self.name = name
        self.back_number = back_number
        self._position = position
    
    def change_back_number(self, new_number): # 메소드 (멤버함수)
        print(f"{self.name}의 등번호를 {self.back_number}에서 {new_number}로 변경합니다.")
        self.back_number = new_number

    def __change_position(self, new_position):
        print(f"{self.name}의 위치를 {self.position}에서 {new_position}로 변경합니다.")
        self._position = new_position
    # 이제 __change_position 을 외부에서 접근할 경우에는 AttributeError가 발생한다


aaa = SoccerPlayer("aaa", 1, "수비수")
bbb = SoccerPlayer("bbb", 2, "유리수")
ccc = SoccerPlayer("ccc", 3, "원수")
# 이렇게 생성한 인스턴스들은 다른 메모리 영역대에 할당된다.


# #############################################################################

# 상속 구조 사용하기
# 클래스를 상속하는 것은 다른 클래스의 기능을 상속하는 것이다
# 상속을 통해서 기능을 추가할 수 있다

class Person(object):
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"{self.name}님 안녕하세요.")
    def say_bye(self):
        print(f"{self.name}님 안녕히가세요.")

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name) # 상위 클래스를 생성하여 상속함 - 속성이나 메소드를 추가할 수 있다
        self.salary = salary
    def work(self):
        print(f"{self.name}님은 회사에서 일하고 있습니다.")
    def pay(self):
        print(f"{self.name}님의 월급은 {self.salary}원입니다.")

