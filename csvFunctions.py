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

def latexExportVars(alfaBubble,horasBubble, pagosBubble, alfaQuick, horasQuick, pagosQuick,mediaBubble=0, mediaQuick=0):
  mediaBubble=(alfaBubble+horasBubble+ pagosBubble)/3
  mediaQuick=(alfaQuick+horasQuick+ pagosQuick)/3
  
  with open("./relatorio-latex/times.sty", mode='w') as writer:
    writer.writelines("\\newcommand\\alfaBubble{"+str(alfaBubble)+"}\n")
    writer.writelines("\\newcommand\\horasBubble{"+ str(horasBubble) + "}\n")
    writer.writelines("\\newcommand\\pagosBubble{"+str(pagosBubble)+ "}\n")
    writer.writelines("\\newcommand\\mediaBubble{"+ str(mediaBubble) +"}\n")
    writer.writelines("\\newcommand\\alfaQuick{" +str(alfaQuick)+"}\n")
    writer.writelines("\\newcommand\\horasQuick{"+ str(horasQuick)+ "}\n")
    writer.writelines("\\newcommand\\pagosQuick{"+str(pagosQuick)+"}\n")
    writer.writelines("\\newcommand\\mediaQuick{"+str(mediaQuick)+"}\n")

