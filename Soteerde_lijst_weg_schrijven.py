import csv
from tabulate import tabulate

# Vervang 'personeeldata.csv' door het pad naar jouw CSV-bestand
bestand = 'personeeldata.csv'
gesorteerd_bestand = 'gesorteerde_personeeldata.csv'  # Bestand voor gesorteerde data

# Maak een lege lijst voor de data en headers
data = []
headers = []

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    try:
        # Lees de header (kolomnamen) in
        headers = next(reader)
    except StopIteration:
        # Als het bestand leeg is, geef een melding en ga verder
        print("Het CSV-bestand is leeg. Voeg een nieuw personeelslid toe om te beginnen.")

    # Voeg de bestaande rijen toe aan de data-lijst
    for row in reader:
        data.append(row)


# Functie om de lijst te sorteren op maandloon van hoog naar laag
def sorteer_op_maandloon():
    # Neem aan dat de loon-kolom "maandloon" is en vind de index
    loon_index = headers.index("maandloon")

    # Sorteer de data op basis van de maandloon-kolom (hoog naar laag)
    gesorteerde_data = sorted(data, key=lambda x: float(x[loon_index]), reverse=True)
    return gesorteerde_data


# Functie om de gesorteerde lijst naar een nieuw CSV-bestand te schrijven
def schrijf_gesorteerde_lijst_weg():
    gesorteerde_data = sorteer_op_maandloon()

    with open(gesorteerd_bestand, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Schrijf de headers
        writer.writerow(headers)

        # Schrijf de gesorteerde data
        writer.writerows(gesorteerde_data)

    print(f"\nDe gesorteerde gegevens zijn succesvol opgeslagen in {gesorteerd_bestand}.")


# Toon de bestaande gegevens, als die er zijn
if data:
    print("Huidige personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
else:
    print("Er zijn nog geen personeelsgegevens beschikbaar.")

# Als het bestand leeg is, vraag de headers aan de gebruiker
if not headers:
    aantal_kolommen = int(input("Het bestand is leeg. Hoeveel kolommen wil je toevoegen? "))
    for i in range(aantal_kolommen):
        kolomnaam = input(f"Voer de naam van kolom {i + 1} in: ")
        headers.append(kolomnaam)


# Functie om een nieuw personeelslid toe te voegen
def nieuw_personeelslid_toevoegen():
    nieuw_personeelslid = []
    print("\nVoer de gegevens in voor een nieuw personeelslid:")
    for header in headers:
        waarde = input(f"Voer {header} in: ")
        nieuw_personeelslid.append(waarde)

    # Voeg het nieuwe personeelslid toe aan de data
    data.append(nieuw_personeelslid)

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))


# Functie om een personeelslid te verwijderen
def verwijder_personeelslid():
    print("\nHuidige personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Kies op basis van een kolom om een personeelslid te verwijderen
    zoekterm = input(f"Voer de naam die je wenst te verwijderen: ")

    # Zoek naar de juiste rij om te verwijderen
    index_te_verwijderen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_verwijderen = i
            break

    if index_te_verwijderen is not None:
        print(f"Personeelslid gevonden en verwijderd: {data[index_te_verwijderen]}")
        del data[index_te_verwijderen]  # Verwijder het personeelslid
    else:
        print("Geen personeelslid gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))


# Functie om het loon van een personeelslid aan te passen
def pas_loon_aan():
    print("\nHuidige personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Vraag de naam van het personeelslid wiens loon je wilt aanpassen
    zoekterm = input(f"Voer de naam in van het personeelslid wiens loon je wilt aanpassen: ")

    # Zoek het personeelslid
    index_te_aanpassen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_aanpassen = i
            break

    if index_te_aanpassen is not None:
        # Vraag het nieuwe loon
        nieuw_loon = input("Voer het nieuwe loon in: ")

        # Neem aan dat de loon-kolom de laatste kolom is; pas dit aan indien nodig
        loon_index = headers.index("maandloon")

        # Pas het loon aan
        data[index_te_aanpassen][loon_index] = nieuw_loon
        print(f"Loon van {data[index_te_aanpassen][0]} is aangepast naar: {nieuw_loon}")
    else:
        print("Geen personeelslid gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte personeelslijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))


# Functie om de data naar het CSV-bestand weg te schrijven
def schrijf_data_weg():
    with open(bestand, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Schrijf de headers
        writer.writerow(headers)

        # Schrijf alle personeelsgegevens
        writer.writerows(data)
    print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")


# Vraag of de gebruiker de lijst wil sorteren en tonen
def vraag_sorteer_en_toon():
    while True:
        keuze = input("Wil je de personeelslijst sorteren op maandloon en wegschrijven? (ja/nee): ").strip().lower()
        if keuze == 'ja':
            schrijf_gesorteerde_lijst_weg()
            break
        elif keuze == 'nee':
            print("Sorteren en wegschrijven is overgeslagen.")
            break
        else:
            print("Ongeldige invoer. Typ 'ja' of 'nee'.")


# Voeg een personeelslid toe (dit kun je meerdere keren aanroepen als je dat wilt)
# nieuw_personeelslid_toevoegen()

# Pas loon aan
# pas_loon_aan()

# Verwijder een personeelslid (optioneel)
# verwijder_personeelslid()

# Vraag of de gebruiker de lijst wil sorteren en tonen
vraag_sorteer_en_toon()

# Op een later moment kun je de gegevens wegschrijven
schrijf_data_weg()
