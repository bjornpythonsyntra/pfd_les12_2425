import csv

# Vervang 'persooneel.csv' door het pad naar jouw CSV-bestand
bestand = 'personeeldata.csv'

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Elke rij (record) afdrukken
    for row in reader:
        for item in row:
            print(item,end="\t")
        print("")