#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
  list1 = []
  list1.append(a)
  list1.append(b)
  for i in range(26):
    x = list1[i] + list1[i+1]
    if x > 9:
      y = x - 9
      list1.append(y)
    elif x <= 9:
      list1.append(x)
    if list1[-2] == list1[0] and list1[-1] == list1[1]:
      newlist = []
      for n in range(len(list1)):
        newlist.append(str(list1[n]))
      x = ''.join(newlist)
      return x
      
  


def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
