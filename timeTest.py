import csvFunctions
import functions
import time


def testBubbleSortAlpha():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.bubbleSortAlpha(data)
  print("--- {} seconds ---".format(time.time()- start_time)) 
  csvFunctions.exportCSV(data, "BubbleSortAlpha.csv")

def testBubbleSortHours():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.bubbleSortHours(data)
  print("--- {} seconds ---".format(time.time()- start_time)) 
  csvFunctions.exportCSV(data, "BubbleSortHours.csv")

def testBubbleSortPays():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.bubbleSortPays(data)
  print("--- {} seconds ---".format(time.time()- start_time)) 
  csvFunctions.exportCSV(data, "BubbleSortPays.csv")

# quick sort tests

def testQuickSortAlpha():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortAlpha(data)
  print("--- {} seconds ---".format(time.time() - start_time)) 
  csvFunctions.exportCSV(data, "quickSortAlpha.csv")

def testQuickSortHours():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortHours(data)
  print("--- {} seconds ---".format(time.time() - start_time)) 
  csvFunctions.exportCSV(data, "quickSortHours.csv")

def testQuickSortPays():
  data= csvFunctions.readCSV()
  start_time = time.time()
  functions.quickSortPays(data)
  print("--- {} seconds ---".format(time.time() - start_time)) 
  csvFunctions.exportCSV(data, "quickSortPays.csv")
