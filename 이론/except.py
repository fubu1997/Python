# 파이썬에서 예외처리 try / except

# try:
#   idx = []
#   idx[0] = 100
# except:
#   pass

# print("OK")

try:
  file = open("sample.txt", "r")
  n = "10"
  v = int(n)
except:
  print("오류 발생")
finally:
  file.close()
  print("파이널리 호출")