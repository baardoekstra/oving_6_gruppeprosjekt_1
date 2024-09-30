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
<<<<<<< HEAD
    reader2 = csv.reader(file2, delimiter=";") #Delimiter gir informasjon til programmet om at elementene skal "deles" ved hver semikolon.
    reader2 = list()
    temperatur2 = list()
    tidspunkt2 = list()
    for row in reader2:
        temperatur2.append(row[1])
        tidspunkt2.append(row[0])
        #print(
    print(temperatur2, tidspunkt2)




=======
    reader2 = csv.reader(file2)
    for row in reader2:
>>>>>>> 3cba74174f3da4630e7b232d8144e78150696811
