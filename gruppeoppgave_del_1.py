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
        tidspunkt1_verdier.append(row[2])
        temperatur1_verdier.append(float(row[3].replace(',', '.')))
        lufttrykk1_verdier.append(float(row[4].replace(',', '.')))
    for element in tidspunkt1_verdier:
        datetime.strptime(element, '%d.%m.%Y %H:%M')
        


with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2, delimiter=";")
    temperatur2_verdier = list()
    tidspunkt2_verdier = list()
    trykk_bar_verdier_feil = list()
    trykk_abs_verdier_feil = list()

    header2 = next(reader2)
    tidspunkt2 = (header2[0])

    for row2 in reader2:
        try:
            tidspunkt2_verdier.append(row2[0])
            temperatur2_verdier.append(float(row2[-1].replace(',', '.')))
            trykk_abs_verdier_feil.append(row2[3].replace(',', '.'))
            trykk_bar_verdier_feil.append(row2[2].replace(',', '.'))
        except ValueError:
            trykk_bar_verdier_feil.append(None)
    
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


    konverterte_tidspunkt2_liste = list()
    for element in tidspunkt2_verdier:
        try:
            konverterte_tidspunkt2 = datetime.strptime(element, '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
            konverterte_tidspunkt2_liste.append(konverterte_tidspunkt2)
        except ValueError:
            konverterte_tidspunkt2 = datetime.strptime(element, '%m/%d/%Y %H:%M:%S %p').strftime('%d.%m.%Y %H:%M')
            konverterte_tidspunkt2_liste.append(konverterte_tidspunkt2)
    konverterte_tidspunkt2_liste.sort()
print(len(tidspunkt1_verdier), len(temperatur1_verdier))
print(len(konverterte_tidspunkt2_liste), len(temperatur2_verdier))
print(len(konverterte_tidspunkt2_liste), len(trykk_abs_verdier))
print(len(konverterte_tidspunkt2_liste), len(trykk_bar_verdier))
print(len(tidspunkt1_verdier), len(lufttrykk1_verdier))
print(tidspunkt1_verdier, "SKILLE", lufttrykk1_verdier)

tick_antall = 3
tick_hopp = np.linspace(0, len(konverterte_tidspunkt2_liste) -1, tick_antall, dtype=int)
tick_verdier = [konverterte_tidspunkt2_liste[i] for i in tick_hopp]

# Funksjon for å regne gjennomsnitt av temperaturer
#def snitt_temperaturer(tidspunkt1_verdier, temperatur2_verdier, n):
#tidspunkt1_verdier_gj = list()
#temperatur1_verdier_gj = list()
snitt_temperaturer = list()
n = 30

for i in range(len(tidspunkt1_verdier)):
    #tidspunkt1_verdier.append(i[2])
    #temperatur1_verdier.append(float(i[-2]))
    snitt = np.mean(temperatur1_verdier[i]) # : i + n + 1]) #beregner snittet av de n-forrige, den nåværende og de n neste målingene.
    #tidspunkt1_verdier.append(tidspunkt1_verdier[i])
    snitt_temperaturer.append(snitt)
#return tidspunkt1_verdier, snitt_temperaturer
#snitt_temperaturer(tidspunkt1_verdier, temperatur2_verdier, n)
#print("Andreas sine drittall", (len(tidspunkt1_verdier), len(snitt_temperaturer)))


plt.figure(figsize=(12, 12))
plt.subplot(2, 1, 1)
plt.plot(tidspunkt1_verdier, temperatur1_verdier, label="Lufttemperatur MET", color="red", linewidth=2)
plt.plot(konverterte_tidspunkt2_liste, temperatur2_verdier, label="Temperatur i celsius", color= "blue", linewidth=2)
#plt.plot(tidspunkt1_verdier, snitt_temperaturer, label="Gjennomsnittsverdier", color="green", linewidth=2)
plt.scatter(konverterte_tidspunkt2_liste, temperatur2_verdier, label="Temperatur i celsius", color= "blue", linewidth=2)
plt.xlabel("Tidspunkter")
plt.ylabel("Temperaturer")
plt.xticks(tick_verdier)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(konverterte_tidspunkt2_liste, trykk_abs_verdier, label="Trykk Absolutt", color= "yellow", linewidth=2)
plt.scatter(konverterte_tidspunkt2_liste, trykk_bar_verdier, label="Trykk Barometer", color= "green")
plt.plot(tidspunkt1_verdier, lufttrykk1_verdier, label="Lufttrykk1", color= "blue", linewidth=2)
plt.xlabel("Tidspunkter")
plt.ylabel("Trykk i hPa")
plt.xticks(tick_verdier)

#plt.subplot(2, 2, 3)
#plt.plot(tidspunkt1_verdier, lufttrykk1_verdier, label="Lufttrykk1", color= "blue", linewidth=2)
#plt.xlabel("Tidspunkter")
#plt.ylabel("Trykk")
#plt.xticks(tick_verdier)

plt.show()
