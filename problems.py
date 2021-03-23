def nonrecurring(L):
  if len(L) < 1:
    return None
  counts = {}
  for w in L:
    counts[w] = counts.get(w,0)+1
  for k in counts:
    if counts[k] == 1:
      return k
  return None


##facebook friends tree
f = [['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A']]
def fr(l):
  dt = {}
  for i in l:
    if len(i)>1: 
      dt[i[0]] = dt.get(i[0],0) + 1
      dt[i[1]] = dt.get(i[1],0) + 1
    elif (len(i) ==1):
        dt[i[0]] = dt.get(i[0],0)
    else:
      continue
  return dt

  ## max element in list

  ## Max element in a list
def maxElement(L):
  if len(L) < 1:
    return None
  else:
    max = L[0]
    for i in L:
      if i > max:
        max = i
    return max

### 2sum leetcode

def twoSum(a,L):
  L.sort()
  ans = []
  first = 0
  last = len(L)-1
  # twoSum = (a - (L[first] + L[last]))
  while(first < last):
    twoSum = (a - (L[first] + L[last]))
    if (twoSum > 0 ):
      first +=1
    elif (twoSum < 0):
      last -=1
    else:
      ans.append([L[first], L[last]])
      first+=1
      while(first<last):
        if(L[first] == L[first-1]):
          first+=1
  return ans