import csv

with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        print(row)

with open('trykk_og_temperaturlogg_rune_time.csv', mode='r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        print(row)


stasjon = list()

x = 45
