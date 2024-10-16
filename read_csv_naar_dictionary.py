import csv

# Vervang 'persooneel.csv' door het pad naar jouw CSV-bestand
bestand = 'personeeldata.csv'

# Maak een lege dictionary voor de data
data = {}

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Lees de header (kolomnamen) in
    headers = next(reader)

    # Initialiseer de dictionary met de kolomnamen als sleutels en lege lijsten als waarden
    for header in headers:
        data[header] = []

    # Voeg de rijen toe aan de juiste sleutel (kolom) in de dictionary
    for row in reader:
        for i, value in enumerate(row):
            data[headers[i]].append(value)

# Print de dictionary om de gegevens te zien
print(data)
