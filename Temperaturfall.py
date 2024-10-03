import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Funksjon for å lese og konvertere data fra den første filen
def les_fil1(filnavn):
    temperatur1 = []
    lufttrykk1 = []
    tidspunkt1 = []

    with open(filnavn, mode='r') as file1:
        reader1 = csv.reader(file1, delimiter=";")
        next(reader1)  # Hopper over headeren
        for row in reader1:
            try:
                tidspunkt1.append(datetime.strptime(row[2], '%d.%m.%Y %H:%M'))
                temperatur1.append(float(row[3].replace(',', '.')))
                lufttrykk1.append(float(row[4].replace(',', '.')))
            except ValueError:
                continue  # Hopp over rader med feil

    return tidspunkt1, temperatur1, lufttrykk1

# Funksjon for å lese og konvertere data fra den andre filen
def les_fil2(filnavn):
    temperatur2 = []
    trykk_abs = []
    trykk_bar = []
    tidspunkt2 = []

    with open(filnavn, mode='r') as file2:
        reader2 = csv.reader(file2, delimiter=";")
        next(reader2)  # Hopper over headeren
        for row in reader2:
            try:
                # Prøv med to formater for å håndtere ulike datofeil
                try:
                    tidspunkt = datetime.strptime(row[0], '%m.%d.%Y %H:%M')
                except ValueError:
                    tidspunkt = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S %p')
                
                tidspunkt2.append(tidspunkt)
                temperatur2.append(float(row[-1].replace(',', '.')))
                trykk_abs.append(float(row[3].replace(',', '.')))
                trykk_bar.append(float(row[2].replace(',', '.')))
            except ValueError:
                continue  # Hopp over rader med feil

    return tidspunkt2, temperatur2, trykk_abs, trykk_bar


# Funksjon for å hente data for bestemt tidsintervall
def hent_temperatur_interval(tidspunkt_liste, temperatur_liste, start_tid, slutt_tid):
    start_index = None
    slutt_index = None
    for i, tid in enumerate(tidspunkt_liste):
        if tid >= start_tid and start_index is None:
            start_index = i
        if tid > slutt_tid:
            slutt_index = i
            break

    if start_index is not None and slutt_index is not None:
        return tidspunkt_liste[start_index:slutt_index], temperatur_liste[start_index:slutt_index]
    else:
        return [], []

# Lese begge filene
tidspunkt1_verdier, temperatur1_verdier, lufttrykk1_verdier = les_fil1('temperatur_trykk_met_samme_rune_time_datasett.csv')
tidspunkt2_verdier, temperatur2_verdier, trykk_abs_verdier, trykk_bar_verdier = les_fil2('trykk_og_temperaturlogg_rune_time.csv')

# Punkt h: Plotting av temperaturfall fra 11. juni til 12. juni
start_tid = datetime(2021, 6, 11, 17, 31)
slutt_tid = datetime(2021, 6, 12, 3, 5)
tidspunkt_interval, temperatur_interval = hent_temperatur_interval(tidspunkt1_verdier, temperatur1_verdier, start_tid, slutt_tid)

plt.figure(figsize=(12, 8))
plt.plot(tidspunkt_interval, temperatur_interval, label="Temperaturfall (11. juni - 12. juni)", color="purple", linewidth=2)
plt.xlabel("Tidspunkt")
plt.ylabel("Temperatur")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


