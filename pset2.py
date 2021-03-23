## spell corrector

def setUp(word, input_list):
  word = word.strip()
  temp_list = []
  Ismatch = False

  if word in input_list:
    Ismatch = True
  elif word is None or len(word) == 0:
    Ismatch = False
  else:
    for w in input_list:
      if len(w) == len(word):
        temp_list.append(w)
  for j in range(len(temp_list)):
    count=0
    for i in range(len(word)):
      if word[i] == temp_list[j][i] or word[i] == '.':
        count += 1
      else:
        break
    if count == len(word):
      Ismatch = True
  return (Ismatch)

def isMatch(word, input_list):
  return setUp(word, input_list)

## CALCULATE TIME FROM TUPLES
def clac_time(l):
    l.sort(key=lambda x:x[0])
    min=0
    max=0
    total=0
    for i in l :
        if i[0] > max :
            total+=i[1]-i[0]
        if i[0] >=min and i[0] == max:
            total+=i[1]-max
        if i[0] > max:
            max = i[1]
    return 'the total is : '+str(total)

clac_time([(0,10),(15,25),(5,17)])