import csv
import matplotlib.pyplot as plt

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
    reader2 = csv.reader(file2, delimiter=";") #Delimiter gir informasjon til programmet om at elementene skal "deles" ved hver semikolon.
    temperatur2 = list()
    tidspunkt2 = list()
    for row2 in reader2:
        temperatur2.append(row2[-1])
        tidspunkt2.append(row2[0])
        #print(
    print(tidspunkt2)
    print(temperatur2)




