import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1, delimiter=";")
    temperatur1_verdier = list()
    lufttrykk1_verdier = list()
    tidspunkt1_verdier = list()

    header = next(reader1)
    tidspunkt1 = (header[2])

    for row in reader1:
        try:
            tidspunkt1_verdier.append(datetime.strptime(row[2], '%d.%m.%Y %H:%M'))
            temperatur1_verdier.append(float(row[3].replace(',', '.')))
            lufttrykk1_verdier.append(float(row[4].replace(',', '.')))
        except ValueError:
            continue

with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2, delimiter=";") #Delimiter gir informasjon til programmet om at elementene skal "deles" ved hver semikolon.
    temperatur2_verdier = list()
    tidspunkt2_verdier = list()
    trykk_bar_verdier = list()
    trykk_abs_verdier = list()

    header2 = next(reader2)
    tidspunkt2 = (header2[0])

    for row2 in reader2:
        try:
            tidspunkt2_verdier.append(datetime.strptime(row2[0], '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M'))
        except ValueError:
            tidspunkt2_verdier.append(datetime.strptime(row2[0], '%m/%d/%Y %H:%M:%S %p').strftime('%d.%m.%Y %H:%M'))
        temperatur2_verdier.append(float(row2[-1].replace(',', '.')))
        trykk_abs_verdier.append(float(row2[3].replace(',', '.')))
        trykk_bar_verdier.append(float(row2[2].replace(',', '.')))



#for i in range(len(tidspunkt1_verdier)):
#    try:
#        tidspunkt1_verdier[i] = datetime.strptime(tidspunkt1_verdier[i], '%d.%m.%Y %H:%M')
#    except ValueError:
#        continue
#for i in range(len(tidspunkt2_verdier)):
#    try:
#        tidspunkt2_verdier[i] = datetime.strptime(tidspunkt2_verdier[i], '%m.%d.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
#    except:
#        continue

plt.figure(figsize=(12, 8))
plt.plot(tidspunkt1_verdier, temperatur1_verdier, label="Temperatur1", color="red", linewidth=4)
plt.plot(tidspunkt1_verdier, lufttrykk1_verdier, label="Lufttrykk1", color= "blue", linewidth=4)
plt.plot(tidspunkt2_verdier, temperatur2_verdier, label="Temperatur2", color= "orange", linewidth=4)
plt.plot(tidspunkt2_verdier, trykk_abs_verdier, label="Trykk Absolutt", color= "yellow", linewidth=4)
plt.plot(tidspunkt2_verdier, trykk_bar_verdier, label="Trykk Barometer", color= "green", linewidth=4)
plt.xlabel("Tidspunkter")
plt.ylabel("Verdier")

plt.show()



