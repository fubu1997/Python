import random
import os

def inputCheck(msg, casting=int):
  while True:
    try:
      userInput = casting(input("몇 일까요?"))
      return userInput
    except:
      continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system('cls')
print("1부터 99까지의 숫자를 10번안에 맞춰보세요.")

while count < chance:
  count += 1
  userInput = inputCheck("몇일까요?")
  if number == userInput:
    break
  elif userInput < number:
    print(f"{userInput}보다 큰 숫자입니다")
  elif userInput > number:
    print(f'{userInput}보타 작은 숫자입니다')
    
if userInput == number :
  print(f'성공! {number}이 맞습니다')
else :
  print(f'실패! 정답은 {number}입니다')