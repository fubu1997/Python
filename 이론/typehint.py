# 파이썬 타이핑, 타입 힌트

# 자료형에 대한 주석 설명을 대신하여
# 파이썬 코딩시 자료형에 대한 메타정보를 제공

# a = 10
# print(type(a))
# a = "abcd"
# print(type(a))
# a = 1.1
# print(type(a))

from typing import TypeVar
student = TypeVar("Student")

a:int = 10
b:str = "abcd"
c:dict[str, int] = {"name":"홍길동", "age":20}

def test(a:int,b:int) -> int:
  retrun a+b