# 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

# 파이썬에서 함수는 일급객체
# 클로저 사용
# 함수내 함수를 정의할 수 있음

# def outer_function(msg):
#   def inner_function():
#     return "난 내부함수인데 {} 메세지를 받았어".format(msg)
#   return inner_function

# c = outer_function("헬로")
# print(dir(c))
# print(type(c.__closure__))

import time

def time_checker(func):
  def inner_function(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print("함수 {} 동작시간 {}".format(func.__name__, end_time-start_time))
    return result
  return inner_function

@time_checker
def test1():
  for i in range(5):
    time.sleep(0.1)

@time_checker
def test2():
  for i in range(3):
    time.sleep(0.1)
    

from functools import wraps

def login_required(func):
  @wraps
  def inner_function(*args, **kwargs):
    if not kwargs.get("is_login"):
      print("로그인 안됨 수행안됨")
      return "로그인이 필요함"
    return func(*args, **kwargs)
  return inner_function

@login_required
def login():
  '''
  로그인 테스트 함수 입니다
  '''
  print("안녕")
  
# def add_tag(new_args):
#   def decorator(fun):
#     def wrapper(name):
#       retrun "<{}>{}</{}>".format(new_args, fun(name), new_args)
#     return wrapper
#   return decorator
  
# @add_tag('html')
# def test(msg):
#   return "반가워" + msg

# print(test("홍길동"))