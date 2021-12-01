#class1.py

# 1) 클래스 형식을 정의

class Person:
    #생성자 (초기화) 메서드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
    def print(self):
        print("My name is {0}". format(self.name))


# 2) 인스턴스 생성
p1 = Person()
p1.print()
