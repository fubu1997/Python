# 유니코드와 인코딩

# 1010110000000000=가


# print(hex(0b11101010))
# print(hex(0b10110000))
# print(hex(0b10000000))


file = open("utf8.txt", mode="rb")
print(file.read().decode("utf-8")
      )
file.close()