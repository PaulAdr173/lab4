i = 10
while i > 0:
  i -= 1
  print(i)
  if i == 3:
    break
print("----------------")
b = 10
while b > 0:
  b -= 1
  if b % 2 == 0:
    continue
  print(b)
else:
  print("done3")