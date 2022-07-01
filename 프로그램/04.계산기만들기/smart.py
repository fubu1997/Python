# 5 + 5 * 10
import os

operator = ["+", "-", "*", "/", "="]

def stringCalculator(userInput, showHistory = False):
  stringList = []
  lop = 0

  if userInput[-1] not in operator:
    userInput += "="

  for i,s in enumerate(userInput):
    if s in operator:
      if userInput[lop:i].strip() != "":
        stringList.append(userInput[lop:i])
        stringList.append(s)
        lop = i + 1
        
  stringList = stringList[:-1]

  pos = 0

  while True:
    if pos + 1 > len(stringList):
      break
    if len(stringList) > pos + 1 and stringList[pos] in operator:
      temp = stringList[pos-1] + stringList[pos] + stringList[pos+1]
      del stringList[0:3]
      stringList.insert(0, str(eval(temp)))
      pos = 0
      
      if showHistory:
        print(stringList)
    pos += 1

  if len(stringList) > 0:
    result = float(stringList[0])
  
  return round(result, 4)

while True:
  os.system('cls')
  userInput = input("계산식을 입력하세요>")
  if userInput == '/exit':
    break
  result = stringCalculator(userInput, showHistory=True)
  print(f"결과: {result}")
  os.system('pause')