import ephem
import datetime

date = datetime.date.today()

mars = ephem.Mars(date)

currentState = ephem.constellation(mars)
print("Mars is in", currentState)

print ('Next full moon on', ephem.next_full_moon(date))