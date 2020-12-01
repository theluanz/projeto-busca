import timeTest
from csvFunctions import latexExportVars
timeToRun=0
repeat = 10

for x in range(repeat):
  timeToRun+=(timeTest.testBubbleSortAlpha())
alfaBubble= timeToRun/repeat
timeToRun=0

for x in range(repeat):
  timeToRun+=timeTest.testBubbleSortHours()
horasBubble = timeToRun/repeat
timeToRun=0

for x in range(repeat):
  timeToRun+=timeTest.testBubbleSortPays()
pagosBubble = timeToRun/repeat
timeToRun=0

for x in range(repeat):
  timeToRun+=timeTest.testQuickSortAlpha()
alfaQuick= timeToRun/repeat
timeToRun=0

for x in range(repeat):
  timeToRun+=timeTest.testQuickSortHours()
horasQuick= timeToRun/repeat
timeToRun=0

for x in range(repeat):
  timeToRun+=timeTest.testQuickSortPays()
pagosQuick= timeToRun/repeat
timeToRun=0

latexExportVars(alfaBubble,horasBubble, pagosBubble, alfaQuick, horasQuick, pagosQuick)
