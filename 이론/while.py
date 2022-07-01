#반목문 while

num = 1
jjak = 0
hol = 0
while num <= 10:
  if num % 2 == 0:
    print("짝 {}".format(num))
    jjak += num
  else:
    print("홀 {}".format(num))
    hol += num
  num = num + 1
  
print("홀 합 {}".format(hol))
print("짝 합 {}".format(jjak))