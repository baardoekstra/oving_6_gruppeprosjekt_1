import csv

with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1, delimiter=";")
    temperatur = list()
    lufttrykk = list()
    tidspunkt1 = list()
    for row in reader1:
        tidspunkt1.append(row[2])
        temperatur.append(row[3])
        lufttrykk.append(row[4])

print(temperatur)

with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2: