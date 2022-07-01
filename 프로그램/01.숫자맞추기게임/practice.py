import random
import os

def inputCheck(msg, casting=int):
  while True:
    try:
      userInput = casting(int(input("숫자를 입력하세요 =>")))
      return userInput
    except:
      continue
  
os.system('cls')
print("1 ~ 100까지의 숫자중에 맞춰보세요, 기회는 10번")
number = random.randint(1, 100)
count = 1

while count < 10:
  count += 1
  userInput = inputCheck("숫자를 입력하세요 =>")

  if number == userInput:
    print(f"정답입니다 정답은 {number}이었습니다")
    break
  elif number < userInput:
    print(f"{userInput}보다 작습니다")
  elif number > userInput:
    print(f'{userInput}보다 큽니다')