import time
from datetime import datetime

parking_time = ["" for i in range(6)]
parking_space = ["" for i in range(6)]

def main():

  while True:
    choice_parking = int(input("0) Programm beenden 1) Wagen abstellen 2) Wagen abholen   "))

    if choice_parking == 1:
      set_parkingspace()
    elif choice_parking == 2:
      free_parkingspace()
    elif choice_parking == 0:
      break
    else:
      print("Die Eingabe war nicht korrekt. Bitte geben Sie eine der möglichen Auswahlmöglichkeiten ein: ")

def set_parkingspace():
  while True:
    license_plate = input ("Wie lautet Ihr Kennzeichen?")
    while True:
      parking_lot_number = int(input("Wie lautet Ihre Parkplatznummer?"))
      if parking_lot_number < 1 or parking_lot_number > len(parking_space):
        print("Entschuldigung. Diese Parkplatznummer gibt es nicht auf unserem Parkplatz nicht. Es sind nur Parkplätze mit den Nummern 1 -", len(parking_space), " vorhanden.")
        print("Bitte versuche Sie es erneut.")
        continue
      break
    if len(parking_space[parking_lot_number-1]) == 0:
        parking_space[parking_lot_number-1] = license_plate
        parking_time[parking_lot_number-1] = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        break
    else:
        print("Auf diesem Parkplatz steht bereits ein Auto. \n Bitte suchen Sie sich einen anderen Parkplatz aus.")

def free_parkingspace():
  parking_ID = input("Ich hoffe Sie hatten einen schönen Aufenthalt. \n Bitte geben Sie Ihre Parkplatznummer oder ihr Kennzeichen ein.")
  while True:
    if parking_ID.isdigit():
      parking_space[int(parking_ID)-1] = ""
      time_parking(int(parking_ID)-1)
    else:

      for i, element in enumerate(parking_space):

        if element == parking_ID:
          parking_space[i] = ""
          time_parking(i)
    break

def time_parking(position):
  print("Startzeit: " + parking_time[position] )
  print("Endzeit: " + datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
  x = datetime.strptime(parking_time[position], '%m/%d/%Y %H:%M:%S')
  y = datetime.strptime(datetime.now().strftime('%m/%d/%Y %H:%M:%S'), '%m/%d/%Y %H:%M:%S')
  duration = abs((y - x).seconds)


#  duration += 36001 Stundentest

  if duration < 60:
      print("Parkzeit: ", duration, " sec")
  elif duration >= 3600:
      hours = duration // 3600
      minutes = (duration % 3600) // 60
      seconds = duration % 60
      print("Parkzeit: ", hours, "h ", minutes, "min und ", seconds, "sec")
  else:
      minutes = duration // 60
      seconds = duration % 60
      print("Parkzeit: ", minutes, "min und ", seconds, "sec")

main()