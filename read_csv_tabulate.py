import csv
from tabulate import tabulate

# Vervang 'personeeldata.csv' door het pad naar jouw CSV-bestand
bestand = 'personeeldata.csv'

# Maak een lege lijst voor de data
data = []

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Lees de header (kolomnamen) in
    headers = next(reader)

    # Voeg de rijen toe aan de data lijst
    for row in reader:
        data.append(row)

# Toon de gegevens in een nette tabel met tabulate
print(tabulate(data, headers=headers, tablefmt='grid'))
