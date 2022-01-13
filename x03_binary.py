#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""

def toBinary(num):
  x = format(num,'b')
  x = list(reversed(x))
  for i in range(10):
    if len(x) <= 7:
      x.append('0')
  for i in range(len(x)):
    x[i] = int(x[i])
  return x


def toDecimal(myList):
  myList = list(myList)
  y = True
  if 1 not in myList:
    return 0
  while y == True:
    if myList[-1] == 0:
      myList.pop()
    if myList[-1] == 1:
      y = False
  ints = list(reversed(myList))
  string_ints = [str(int) for int in ints]
  x = ''.join(string_ints)
  final = int(x, 2)
  
  return final

def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
