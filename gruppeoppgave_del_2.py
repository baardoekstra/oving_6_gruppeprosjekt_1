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
    temperaturfall1 = 0
    temperaturfall1_tid = 0
    temperaturfall2 = 0
    temperaturfall2_tid = 0
    temperaturfall_liste = []
    temperaturfall_tid_liste = []
    temperaturfall_liste_met = []

    for row in reader1:
        tidspunkt1_verdier.append(datetime.strptime(row[2], '%d.%m.%Y %H:%M'))
        temperatur1_verdier.append(float(row[3].replace(',', '.')))
        lufttrykk1_verdier.append(float(row[4].replace(',', '.')))

        if row[2] == "11.06.2021 17:00":
                if len(temperaturfall_liste_met) == 0:
                    temperaturfall1 = float(row[3].replace(',', '.'))
                    temperaturfall_liste_met.append(temperaturfall1)
        if row[2] == "12.06.2021 03:00":
            if len(temperaturfall_liste_met) == 1:
                temperaturfall2 = float(row[3].replace(',', '.'))
                temperaturfall_liste_met.append(temperaturfall2)

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
            if len(temperaturfall_liste) == 0:
                temperaturfall1 = float(row2[-1].replace(',', '.'))
                temperaturfall1_tid = datetime.strptime(row2[0], '%m.%d.%Y %H:%M')
                temperaturfall_liste.append(temperaturfall1)
                temperaturfall_tid_liste.append(temperaturfall1_tid)
        if row2[0] == "06.12.2021 03:05":
            if len(temperaturfall_liste) == 1:
                temperaturfall2 = float(row2[-1].replace(',', '.'))
                temperaturfall2_tid = datetime.strptime(row2[0], '%m.%d.%Y %H:%M')
                temperaturfall_liste.append(temperaturfall2)
                temperaturfall_tid_liste.append(temperaturfall2_tid)

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

differanse_trykk = []
tidspunkt_differanse = []
for i in range(len(trykk_bar_verdier)):
    if trykk_bar_verdier[i] is not None:
        differanse = trykk_bar_verdier[i] - trykk_abs_verdier[i]
        differanse_trykk.append(differanse)
        tidspunkt_differanse.append(tidspunkt2_verdier[i])

def glatt_differanse(trykk_bar_verdier, n=10):
    glatt_verdier = []
    for i in range(n, len(trykk_bar_verdier) - n):
        gjennomsnitt = np.mean(trykk_bar_verdier[i - n:i + n + 1])
        glatt_verdier.append(gjennomsnitt)
    return glatt_verdier, tidspunkt_differanse[n:len(trykk_bar_verdier) - n]
glatt_trykk_differanse, glatt_tidspunkt_differanse = glatt_differanse(differanse_trykk)

plt.figure(figsize=(16, 9))

plt.subplot(2, 1, 1)
plt.plot(tidspunkt1_verdier, temperatur1_verdier, label="Lufttemperatur MET", color="red", linewidth=1)
plt.plot(tidspunkt2_verdier, temperatur2_verdier, label="Temperatur i celsius", color="blue", linewidth=1)
plt.plot(gjennomsnitt_tider, gjennomsnitt_verdier, label="Gjennomsnittsverdier", color="orange", linewidth=1)
plt.plot(temperaturfall_tid_liste, temperaturfall_liste, label="Temperaturfall 11. - 12. Juni 2021", color="purple", linewidth=1)
plt.plot(temperaturfall_tid_liste, temperaturfall_liste_met, label="Temperaturfall 11. - 12. Juni MET", color="red", linewidth=1)
plt.xlabel("Tidspunkter")
plt.ylabel("Temperaturer / Temperaturfall")
plt.gcf().autofmt_xdate(rotation=90)
plt.grid()
plt.legend()

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


# Kombiner temperaturverdiene fra begge filer
temperatur_alle_verdier = temperatur1_verdier + temperatur2_verdier

# Definer bin-størrelsen til 1 grad
bin_size = 1
min_temp = int(min(temperatur_alle_verdier))
max_temp = int(max(temperatur_alle_verdier))
bins = np.arange(min_temp, max_temp + bin_size, bin_size)

# Lag histogrammet
plt.figure(figsize=(16, 9))     # Mangle verdier på x-akse

plt.subplot(2, 1, 1)
plt.hist(temperatur1_verdier, bins=bins, alpha=0.5, label="Temperatur MET (Fil 1)", color="red")
plt.hist(temperatur2_verdier, bins=bins, alpha=0.5, label="Temperatur Dataset 2", color="blue")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Frekvens")
plt.title("Histogram over temperaturer fra begge filer")
plt.legend()
plt.grid(axis='y', alpha=0.75)

plt.subplot(2, 1, 2)
plt.plot(glatt_tidspunkt_differanse, glatt_trykk_differanse, label ="Differanse absolutt/barometrisk trykk", color="orange", linewidth=2)
plt.xlabel("Tidspunkter")
plt.ylabel("Differanse i hPA")
plt.grid()
plt.gcf().autofmt_xdate(rotation=90)
plt.legend()

plt.show()

tid_ss = []
temp_si =[]
l_trykk_si = []
temp_sa =[]
l_trykk_sa = []

with open('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv', mode='r') as file3:
    reader3 = csv.reader(file3, delimiter=";")
    for row in reader3:
        if row[0] in ["Navn", "Data er gyldig per 01.10.2024 (CC BY 4.0), Meteorologisk institutt (MET)"]:
            continue        # WTF
        if row[0] == "Sirdal - Sinnes":
            tid_ss.append(datetime.strptime(row[2], '%d.%m.%Y %H:%M'))
            temp_si.append(float(row[-2].replace(',', '.')))
            l_trykk_si.append(float(row[-1].replace(',', '.')))
        if row[0] == 'Sauda':
            temp_sa.append(float(row[-2].replace(',', '.')))
            l_trykk_sa.append(float(row[-1].replace(',', '.')))

print(tid_ss)

plt.figure(figsize=(16, 9))

plt.plot(tid_ss, temp_si, label="Temperaturer, Sirdal", color="red", linewidth=1)
plt.plot(tid_ss, temp_sa, label="Temperaturer, Sauda", color="blue", linewidth=1)
plt.plot(gjennomsnitt_tider, gjennomsnitt_verdier, label="Gjennomsnittstemperaturer, UiS", color="orange", linewidth=1)
plt.xlabel("Tidspunkter")
plt.ylabel("Temperaturer / Temperaturfall")
plt.gcf().autofmt_xdate(rotation=90)
plt.grid()
plt.legend()

plt.show()

