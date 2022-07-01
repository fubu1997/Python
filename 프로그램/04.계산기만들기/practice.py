import os

operator = ["+", "-", "*", "/", "="]
userInput = input("계산식을 입력하세요 => ")

stringList = [] #10+10

for i,s in enumerate(userInput):
  if s in operator:
    print("만남")
  print(s)