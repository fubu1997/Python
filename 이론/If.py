time = 12
seek = True

if 12 <= time < 1 and not seek: print("일하는 중")
elif 3 <= time <= 4 or seek: print("휴식시간")
else: print("점심 먹으러감")

a = 10
if a>10:
  ret = 100
elif a == 10:
  ret = 200
else:
  ret = 500
  
ret = {a > 10: 100, a < 10 : 500}.get(True, 200)
ret = {True:100, False:500}.get(True, 200)

name = ["홍길동", "가가멜", "가제트"]
if "가제트" not in name:
  print("없음")
else:
  print("있음")