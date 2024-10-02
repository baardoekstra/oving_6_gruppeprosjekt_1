import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1, delimiter=";")
    temperatur1_verdier = list()
    lufttrykk1_verdier = list()
    tidspunkt1_verdier = list()

    header = next(reader1)
    tidspunkt1 = (header[2])

    for row in reader1:
        tidspunkt1_verdier.append(row[2])
        temperatur1_verdier.append(float(row[3].replace(',', '.')))
        lufttrykk1_verdier.append(float(row[4].replace(',', '.')))
    for element in tidspunkt1_verdier:
        datetime.strptime(element, '%d.%m.%Y %H:%M')
        


with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2, delimiter=";")
    temperatur2_verdier = list()
    tidspunkt2_verdier = list()
    trykk_bar_verdier = list()
    trykk_abs_verdier = list()

    header2 = next(reader2)
    tidspunkt2 = (header2[0])

    for row2 in reader2:
        try:
            tidspunkt2_verdier.append(row2[0])
            temperatur2_verdier.append(float(row2[-1].replace(',', '.')))
            trykk_abs_verdier.append(float(row2[3].replace(',', '.')))
            trykk_bar_verdier.append(float(row2[2].replace(',', '.')))
        except ValueError:
            trykk_bar_verdier.append(None)

    konverterte_tidspunkt2_liste = list()
    for element in tidspunkt2_verdier:
        try:
            konverterte_tidspunkt2 = datetime.strptime(element, '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
            konverterte_tidspunkt2_liste.append(konverterte_tidspunkt2)
        except ValueError:
            konverterte_tidspunkt2 = datetime.strptime(element, '%m/%d/%Y %H:%M:%S %p').strftime('%d.%m.%Y %H:%M')
            konverterte_tidspunkt2_liste.append(konverterte_tidspunkt2)
    konverterte_tidspunkt2_liste.sort()
#print(len(tidspunkt1_verdier), len(temperatur1_verdier))
#print(len(konverterte_tidspunkt2_liste), len(temperatur2_verdier))
#print(len(konverterte_tidspunkt2_liste), len(trykk_abs_verdier))
#print(len(konverterte_tidspunkt2_liste), len(trykk_bar_verdier))
#print(len(tidspunkt1_verdier), len(lufttrykk1_verdier))
print(trykk_bar_verdier)

tick_antall = 3
tick_hopp = np.linspace(0, len(konverterte_tidspunkt2_liste) -1, tick_antall, dtype=int)
tick_verdier = [konverterte_tidspunkt2_liste[i] for i in tick_hopp]

plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.plot(tidspunkt1_verdier, temperatur1_verdier, label="Lufttemperatur MET", color="red", linewidth=2)
plt.plot(konverterte_tidspunkt2_liste, temperatur2_verdier, label="Temperatur i celsius", color= "blue", linewidth=2)
plt.xlabel("Tidspunkter")
plt.ylabel("Temperaturer")
plt.xticks(tick_verdier)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(konverterte_tidspunkt2_liste, trykk_abs_verdier, label="Trykk Absolutt", color= "yellow", linewidth=2)
plt.scatter(konverterte_tidspunkt2_liste, trykk_bar_verdier, label="Trykk Barometer", color= "green")
plt.xlabel("Tidspunkter")
plt.ylabel("Trykk")
plt.xticks(tick_verdier)

plt.subplot(2, 2, 3)
plt.plot(tidspunkt1_verdier, lufttrykk1_verdier, label="Lufttrykk1", color= "blue", linewidth=2)
plt.xlabel("Tidspunkter")
plt.ylabel("Trykk")
plt.xticks(tick_verdier)

plt.show()
