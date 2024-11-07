import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1, delimiter=";")
    temperatur1_verdier = list()
    lufttrykk1_verdier = list()
    tidspunkt1_verdier = list()

    header = next(reader1)
    tidspunkt1 = (header[2])

    for row in reader1:
        tidspunkt1_verdier.append(datetime.strptime(row[2], '%d.%m.%Y %H:%M'))
        temperatur1_verdier.append(float(row[3].replace(',', '.')))
        lufttrykk1_verdier.append(float(row[4].replace(',', '.')))

with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2, delimiter=";")
    temperatur2_verdier = list()
    tidspunkt2_verdier = list()
    trykk_bar_verdier_feil = list()
    trykk_abs_verdier_feil = list()

    header2 = next(reader2)
    tidspunkt2 = (header2[0])
    temperaturfall1 = 0
    temperaturfall1_tid = 0
    temperaturfall2 = 0
    temperaturfall2_tid = 0
    temperaturfall_liste = []
    temperaturfall_tid_liste = []

    for row2 in reader2:
        try:
            temperatur2_verdier.append(float(row2[-1].replace(',', '.')))
            trykk_abs_verdier_feil.append(row2[3].replace(',', '.'))
            trykk_bar_verdier_feil.append(row2[2].replace(',', '.'))
        except ValueError:
            trykk_bar_verdier_feil.append(None)
    
        try:
            tidspunkt2 = datetime.strptime(row2[0], '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
            tidspunkt2_str = str(tidspunkt2)
            tidspunkt2 = datetime.strptime(tidspunkt2_str, '%d.%m.%Y %H:%M')
            tidspunkt2_verdier.append(tidspunkt2)
        except ValueError:
            if row2[0][11:13]=="00":
                row2[0]=row2[0][:11]+"12"+row2[0][13:]
            tidspunkt2 = datetime.strptime(row2[0], '%m/%d/%Y %I:%M:%S %p')
            tidspunkt2_verdier.append(tidspunkt2)
        if row2[0] == "06.11.2021 17:31":
            temperaturfall1 = row2[-1]
            temperaturfall1_tid = row2[0]
            temperaturfall1_tid = datetime.strptime(temperaturfall1_tid, '%m.%d.%Y %H:%M')
            temperaturfall_liste.append(temperaturfall1)
            temperaturfall_tid_liste.append(temperaturfall1_tid)
            
        if row2[0] == "06.12.2021 03:05":
            temperaturfall2 = row2[-1]
            temperaturfall2_tid = row2[0]
            temperaturfall2_tid = datetime.strptime(temperaturfall2_tid, '%m.%d.%Y %H:%M')
            temperaturfall_liste.append(temperaturfall2)
            temperaturfall_tid_liste.append(temperaturfall2_tid)

print(temperaturfall_liste, temperaturfall_tid_liste)
#print(temperaturfall2, temperaturfall2_tid)

"""
def gjennomsnitt_temperaturer(tider, temperaturer, n=30):
    gjennomsnitt_tider = []
    gjennomsnitt_verdier = []
    
    for i in range(n, len(temperaturer) - n):
        gj = sum(temperaturer[i - n:i + n + 1]) / (2 * n + 1)
        gjennomsnitt_verdier.append(gj)
        gjennomsnitt_tider.append(tider[i])
    
    return gjennomsnitt_tider, gjennomsnitt_verdier

gjennomsnitt_tider, gjennomsnitt_verdier = gjennomsnitt_temperaturer(tidspunkt2_verdier, temperatur2_verdier)

trykk_bar_verdier = list()
trykk_abs_verdier = list()

for element in trykk_bar_verdier_feil:
    if '.' in element:
        parts = element.split('.')
        trykk_bar_verdi_justert = parts[0] + parts[1][0] + '.' + parts[1][1:]
        trykk_bar_verdi_justert_float = float(trykk_bar_verdi_justert)
        trykk_bar_verdier.append(trykk_bar_verdi_justert_float)
    else:
        trykk_bar_verdier.append(None)
for element in trykk_abs_verdier_feil:
    if '.' in element:
        parts = element.split('.')
        trykk_abs_verdi_justert = parts[0] + parts[1][0] + '.' + parts[1][1:]
        trykk_abs_verdi_justert_float = float(trykk_abs_verdi_justert)
        trykk_abs_verdier.append(trykk_abs_verdi_justert_float)

# Calculate temperature drops for MET data (file1)
temperaturfall1 = [temperatur1_verdier[i] - temperatur1_verdier[i + 1] for i in range(len(temperatur1_verdier) - 1)]

# Calculate temperature drops for other data (file2)
temperaturfall2 = [temperatur2_verdier[i] - temperatur2_verdier[i + 1] for i in range(len(temperatur2_verdier) - 1)]

# Update the existing plot
plt.figure(figsize=(16, 9))

# First subplot: Temperature
plt.subplot(2, 1, 1)
plt.plot(tidspunkt1_verdier, temperatur1_verdier, label="Lufttemperatur MET", color="red", linewidth=2)
plt.plot(tidspunkt2_verdier, temperatur2_verdier, label="Temperatur i celsius", color="blue", linewidth=1)
plt.plot(gjennomsnitt_tider, gjennomsnitt_verdier, label="Gjennomsnittsverdier", color="orange", linewidth=1)
#plt.plot(tidspunkt1_verdier[:-1], temperaturfall1, label="Temperaturfall MET", color="purple", linewidth=1)
#plt.plot(tidspunkt2_verdier[:-1], temperaturfall2, label="Temperaturfall Dataset 2", color="teal", linewidth=1)
plt.plot(temperaturfall_liste, temperaturfall_tid_liste, label="Temperaturfall faen", color="purple", linewidth=1)
plt.xlabel("Tidspunkter")
plt.ylabel("Temperaturer / Temperaturfall")
plt.gcf().autofmt_xdate(rotation=90)
plt.grid()
plt.legend()

# Second subplot: Pressure
plt.subplot(2, 1, 2)
plt.plot(tidspunkt2_verdier, trykk_abs_verdier, label="Trykk Absolutt", color="yellow", linewidth=1)
plt.scatter(tidspunkt2_verdier, trykk_bar_verdier, label="Trykk Barometer", color="green")
plt.plot(tidspunkt1_verdier, lufttrykk1_verdier, label="Lufttrykk i havnivå", color="blue", linewidth=1)
plt.xlabel("Tidspunkter")
plt.ylabel("Trykk i hPa")
plt.grid()
plt.gcf().autofmt_xdate(rotation=90)
plt.legend()

plt.show()


"""