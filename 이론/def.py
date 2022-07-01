# 내장함수
# 사용자함수

# def 함수명():
#   print("함수 호출")
#   return True


# c = 10

# def add(a, b):
#   global c
#   c = a+b
#   return c

# b = add(1,10)
# print(b, c)

from unittest import result


def get_input_user(msg, casting=int):
  while True:
    try:
      user = casting(input(msg))
      return user
    except:
      continue

# user = get_input_user("사용자 이름을 입력하세요>", str)
# age = get_input_user("사용자 나이를 입력하세요.>")

# user = input("사용자 이름을 입력하세요.")

# age = input("사용자 나이를 입력하세요.")


def is_prime_number(num):
  '''사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 리텅합니다
  args:
    msg(str) : input 시 출력할 문구
    casting(class) : 사용자에게 입력 받은 값의 자료형
    
  Return:
    user(casting-value) :사용자에게 입력받은값
  '''
  prime_lists = [False, False] + [True] * (num - 1)
  primes = []
  for i in range(2, num+1):
    if prime_lists[i]:
      for j in range(2 * i, num + 1, i):
        prime_lists[j] = False
  primes = [i for i in range(2, num + 1) if prime_lists[i]==True]
  
  if num in primes:
    return True
  else:
    return False
  
  
def save_winner(*args):
  print(args)

def save_winner2(**kwargs):
  print(kwargs)
  if kwargs.get("name1"):
    print(kwargs["name1"])
  
# save_winner("홍길동", "가가멜", "아즈라엔")
# save_winner2(name1 = "홍길동", name2="가가멜")
  
# def test1(num):
#   num += 10
#   print(num)
  
# a = 50
# test1(a)
# print(a)

# def test2(lists):
#   lists.append("aaaa")
#   print(list)
  
# a = []
# a.append("1234")
# test2(a)
# print(a)

# num = get_input_user("2 이상의 숫자를 입력하세요>", int)
# if is_prime_number(num):
#   print("{}는 소수 입니다".format(num))
# else:
#   print("{} 는 소수가 아닙니다".format(num))

# def hi():
#   print("hello")
  
# hello = hi
# hello()
# print(type(hello))

# def add(a,b):
#   return a + b

# def cal(func, a, b):
#   print("결고{}".format(func(a,b)))
  
# cal(add, 1,5)


def outer_function(func):
  def inner_function(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
  return inner_function

def add(a,b):
  return a + b

f = outer_function(add)
f(10,20)