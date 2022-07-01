# 반복문 for

# result = []
# for num in range(1,6):
#   result.append(num + 5)


# result = [num+5 for num in range(1,6)]
# print(result)

# result = [num *3 for num in range(1,99) if num % 2 == 0]
# print(result)

for i in range(2, 10):
  for j in range(1, 10):
    result = i * j
    print("{} X {} = {}".format(i, j, result))
    
    
gugudan = ["{} X {} = {}".format(i, j, i*j) for i in range(2,10) for j in range(1,10)]
print(gugudan)