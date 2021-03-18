
import datetime
def timeAndDate():

  dateToday = datetime.datetime.now()
  print("Today is %d-%d-%d" % (dateToday.year, dateToday.month, dateToday.day))
timeAndDate()