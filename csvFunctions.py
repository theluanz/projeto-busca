import csv

def readCSV(file='MOCK_DATA.csv'):
  data=[]
  arq = open(file, 'r')
  reader = csv.reader(arq)
  for x in reader:
    data.append(x)
  arq.close()
  data.pop(0)
  return data

def exportCSV(data, fileName="default.csv"):
  with open(fileName, mode='w') as writer:
    writer = csv.writer(writer, delimiter=',')
    for x in data:
      writer.writerow(x)

  