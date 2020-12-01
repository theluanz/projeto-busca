import csvFunctions
import functions
import time

def testBubbleSortAlpha():
  data= csvFunctions.readCSV()
  startTime = time.time()
  functions.bubbleSortAlpha(data)
  finalTime= time.time()- startTime 
  csvFunctions.exportCSV(data, "BubbleSortAlpha.csv")
  return finalTime

def testBubbleSortHours():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.bubbleSortHours(data)
  finalTime= time.time()- start_time
  csvFunctions.exportCSV(data, "BubbleSortHours.csv")
  return finalTime


def testBubbleSortPays():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.bubbleSortPays(data)
  finalTime= time.time()- start_time
  csvFunctions.exportCSV(data, "BubbleSortPays.csv")
  return finalTime


# quick sort tests

def testQuickSortAlpha():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortAlpha(data)
  finalTime= time.time()- start_time
  csvFunctions.exportCSV(data, "quickSortAlpha.csv")
  return finalTime

def testQuickSortHours():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortHours(data)
  finalTime= time.time()- start_time
  csvFunctions.exportCSV(data, "quickSortHours.csv")
  return finalTime

def testQuickSortPays():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortPays(data)
  finalTime= time.time()- start_time
  csvFunctions.exportCSV(data, "quickSortPays.csv")
  return finalTime
