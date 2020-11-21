def bubbleSortAlpha(vetor):
  for i in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if vetor[i][0]> vetor[i+1][0]:
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]


def bubbleSortHours(vetor):
  for i in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if float(vetor[i][2])< float(vetor[i+1][2]):
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

def bubbleSortPays(vetor):
  for i in range(len(vetor)-1):
    for i in range(len(vetor)-1):
      if (vetor[i][1]*vetor[i][2])< (vetor[i][1]*vetor[i+1][2]):
        vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
