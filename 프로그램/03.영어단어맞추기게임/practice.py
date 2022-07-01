import random

wordsDict = {
  "호랑이" : "tiger",
  "사자" : "lion",
  "사과" : "apple",
  "바나나" : "banana"
}

words = []

for i in wordsDict:
  words.append(i)
  
random.shuffle(words)

chance = 3

for i in range(0, len(wordsDict)):
  question = words[i]
  
  for j in range(0, chance):
    userInput = str(input(f"{question}의 영어단어를 입력해주세요. -> "))
    answer = wordsDict[question]
    
    if userInput.strip().lower() == answer.lower():
      print('정답입니다')
      break
    else:
      print("틀렸습니다")
  if userInput.strip().lower() != answer.lower():
    print(f"기회를 모두 소진했습니다 정답은{answer}입니다.")
  
print("모든 문제를 다 제출했습니다.")