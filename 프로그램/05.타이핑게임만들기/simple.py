#타이핑 게임만들기
import time
import random
import os

wordList = [
  "남박사의 파이썬 100% 실전 프로그래밍 강좌",
  "파이썬에서 ord() 함수는 문자의 유니코드 값을 알아오는 함수로 10진수 값을 리턴합니다.",
  "chr(x)는 x에 유니코드 10진수 값을 입력하면 해당하는 문자를 리턴합니다.",
  "UTF-8은 유니코드를 8비트 기반으로 저장하는 인코딩 방식입니다.",
  "CP949는 윈도우에서 사용하기 위해 EUC-KR을 확장해서 만든 문자셋 입니다.",
  "파이썬은 코드가 짧고 유연하여 가독성과 생산성이 좋은 프로그래밍 언어 입니다", 
  "코딩하세요 코딩~",
  "독도는 우리땅"
]

random.shuffle(wordList)

for q in wordList:
  os.system('cls')
  startTime = time.time()
  userInput = str(input(q + "\n")).strip()
  endTime = time.time() - startTime
  
  if userInput == "/exit":
    break

  correct = 0
  for i, c in enumerate(userInput):
    if i >= len(q):
      break
    if c == q[i]:
      correct += 1
  totalLen = len(q)
  c = correct / totalLen * 100
  e = (totalLen - correct) /  totalLen *100
  speed = (correct / endTime) * 60
  
  print(f"속도 : {speed:0.2f} 정확도 : {c:0.2f} 오타율 : {e:0.2f}")
  os.system('pause')