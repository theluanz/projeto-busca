def bubbleSortAlpha(vetor):
  for x in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if vetor[i][0]> vetor[i+1][0]:
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]


def bubbleSortHours(vetor):
  for x in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if float(vetor[i][2])< float(vetor[i+1][2]):
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

def bubbleSortPays(vetor):
  for x in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if float(vetor[i][1])*float(vetor[i][2]) < float(vetor[i+1][1])*float(vetor[i+1][2]):
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

def quickSortAlpha(vetor, beginVet=0, endVet=None):
  if endVet is None:
    endVet = len(vetor)-1
  if beginVet < endVet:
    p = partition(vetor, beginVet, endVet)
    quickSortAlpha(vetor, beginVet, p-1)
    quickSortAlpha(vetor, p+1, endVet)

def partition(vetor, beginVet, endVet):
  pivot = vetor[endVet][0] # pivo = ultimo elemento
  i = beginVet
  for x in range(beginVet, endVet):
    if vetor[x][0]<= pivot:
      vetor[x], vetor[i] = vetor[i], vetor[x]
      i+=1
  vetor[i], vetor[endVet] = vetor[endVet], vetor[i]
  return i

def quickSortHours(vetor, beginVet=0, endVet=None):
  if endVet is None:
    endVet = len(vetor)-1
  if beginVet < endVet:
    p = partitionHours(vetor, beginVet, endVet)
    quickSortHours(vetor, beginVet, p-1)
    quickSortHours(vetor, p+1, endVet)

def partitionHours(vetor, beginVet, endVet):
  pivot = vetor[endVet][2] # pivo = ultimo elemento
  i = beginVet
  for x in range(beginVet, endVet):
    if float(vetor[x][2])>= float(pivot):
      vetor[x], vetor[i] = vetor[i], vetor[x]
      i+=1
  vetor[i], vetor[endVet] = vetor[endVet], vetor[i]
  return i

def quickSortPays(vetor, beginVet=0, endVet=None):
  if endVet is None:
    endVet = len(vetor)-1
  if beginVet < endVet:
    p = partitionPays(vetor, beginVet, endVet)
    quickSortPays(vetor, beginVet, p-1)
    quickSortPays(vetor, p+1, endVet)


def partitionPays(vetor, beginVet, endVet):
  pivot = vetor[endVet] # pivo = ultimo elemento
  i = beginVet
  for x in range(beginVet, endVet):
    if float(vetor[x][2])*float(vetor[x][1])>= float(pivot[2])*float(pivot[1]):
      vetor[x], vetor[i] = vetor[i], vetor[x]
      i+=1
  vetor[i], vetor[endVet] = vetor[endVet], vetor[i]
  return i