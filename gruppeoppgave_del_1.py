import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1, delimiter=";")
    temperatur1 = list()
    lufttrykk1 = list()
    tidspunkt1 = list()

    for row in reader1:
        tidspunkt1.append(row[2])
        temperatur1.append(row[3].replace(',', '.'))
        temperatur1_verdier = float(temperatur1[1:])
        lufttrykk1.append(row[4].replace(',', '.'))
        lufttrykk1_verdier = float(lufttrykk1[1:])



with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2, delimiter=";") #Delimiter gir informasjon til programmet om at elementene skal "deles" ved hver semikolon.
    temperatur2 = list()
    tidspunkt2 = list()
    for row2 in reader2:
        temperatur2.append(row2[-1].replace(',', '.'))
        temperatur2_verdier = float(temperatur2[1:])
        tidspunkt2.append(row2[0])

for i in range(len(tidspunkt1) - 1):
    tidspunkt1[i+1] = datetime.strptime(tidspunkt1[i+1])
for i in range(len(tidspunkt2) - 1):
    tidspunkt2[i+1] = datetime.strptime(tidspunkt2[i+1], '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M')

plt.figure(figsize=(12, 8))
plt.plot(tidspunkt1[1:], temperatur1_verdier[1:], label="Temperatur1", color="red", linewidth=4)
plt.plot(tidspunkt2[1:], temperatur2_verdier[1:], label="Temperatur2", color= "blue", linewidth=4)
plt.xlabel("Tidspunkter")
plt.ylabel("Verdier")

plt.show()



