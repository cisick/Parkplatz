# Parkplatz
Eine Übung zum Thema Listen und Funktionen im Fach PG1

0) Die Parkplätze bilden Sie in einer Liste ab.
   Wie im Bild sind sechs Parkplätze verfügbar. Zu Begin sind alle Parkplätze leer.
1) Erstellen Sie eine Funktion "set_parkingspace", welche den Benutzer nach seinen Kennzeichen und Parkplatznummer fragt. 
   Die Funktion speichert das Kennzeichen als String für die jeweilige Parkplatznummer ab.
2) Implementieren Sie die Funktion "free_parkingspace".
   Der Benutzer wird nach seiner Parkplatznummer gefragt und der Eintrag für das Kennzeichen mit einem leeren String "" überschrieben.
3) Erweitern Sie nun die Funktionen aus 1) und 2).
   Damit es zu keiner Doppelbelegung oder -löschung der Parkplätze kommen kann, wird nun geprüft, ob der Parkplatz bereits belegt oder leer ist.
4) Oft können sich die Kunden des Parkplatzes die Parkplatznummer nicht merken. Ändern Sie die Funktion aus 2) so ab, dass der Kunde entweder sein Kennzeichen oder die Parkplatznummer eingeben kann.
5) Erweitern Sie die Funktionen entsprechend, dass die Parkdauer ermittelt wird. Dafür nutzen Sie am Besten die Klasse time über import time in Python.
   Ein Beispiel finden Sie unter https://pynative.com/python-get-time-difference/. Lesen Sie sich dafür den Abschnitt "Get time difference in hours and minutes" durch.
