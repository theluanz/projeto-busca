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
  functions.bubbleSortHours(data)
  print("--- {} seconds ---".format(time.time()- start_time)) 
  csvFunctions.exportCSV(data, "BubbleSortPays.csv")
