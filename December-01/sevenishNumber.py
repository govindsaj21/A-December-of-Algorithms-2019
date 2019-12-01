n=input()

def sevenishNumber(n):
  b=bin(int(n))
  print(int(str(b)[2:],7))

sevenishNumber(n)
