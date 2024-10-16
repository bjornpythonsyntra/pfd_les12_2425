import csv

muzikanten = {
    1: {"naam": "Emma", "woonplaats": "Antwerpen", "genre": "Pop", "instrument": "Zang"},
    2: {"naam": "Liam", "woonplaats": "Brugge", "genre": "Rock", "instrument": "Gitaar"},
    3: {"naam": "Sophie", "woonplaats": "Gent", "genre": "Jazz", "instrument": "Piano"},
    4: {"naam": "Noah", "woonplaats": "Leuven", "genre": "Hip-Hop", "instrument": "Drums"},
    5: {"naam": "Mila", "woonplaats": "Luik", "genre": "Klassiek", "instrument": "Viool"},
    6: {"naam": "Lucas", "woonplaats": "Charleroi", "genre": "Reggae", "instrument": "Basgitaar"},
    7: {"naam": "Julia", "woonplaats": "Namen", "genre": "Indie", "instrument": "Zang"},
    8: {"naam": "Daan", "woonplaats": "Brussel", "genre": "Blues", "instrument": "Harmonica"},
    9: {"naam": "Lara", "woonplaats": "Oostende", "genre": "Electronic", "instrument": "Synthesizer"},
    10: {"naam": "Finn", "woonplaats": "Hasselt", "genre": "Folk", "instrument": "Gitaar"},
    11: {"naam": "Tess", "woonplaats": "Tournai", "genre": "Metal", "instrument": "Drums"},
    12: {"naam": "Max", "woonplaats": "La Louvière", "genre": "Pop", "instrument": "Zang"},
    13: {"naam": "Zoe", "woonplaats": "Sint-Truiden", "genre": "Rock", "instrument": "Gitaar"},
    14: {"naam": "Mason", "woonplaats": "Verviers", "genre": "Hip-Hop", "instrument": "Zang"},
    15: {"naam": "Nina", "woonplaats": "Mouscron", "genre": "Jazz", "instrument": "Saxofoon"},
    16: {"naam": "Julian", "woonplaats": "Binche", "genre": "Klassiek", "instrument": "Cello"},
    17: {"naam": "Yara", "woonplaats": "Sint-Niklaas", "genre": "Pop", "instrument": "Keyboard"},
    18: {"naam": "Ravi", "woonplaats": "Kortrijk", "genre": "Reggae", "instrument": "Basgitaar"},
    19: {"naam": "Sara", "woonplaats": "Genk", "genre": "Indie", "instrument": "Zang"},
    20: {"naam": "Luca", "woonplaats": "Ukkel", "genre": "Electronic", "instrument": "Drums"}
}

# Schrijf naar een CSV-bestand
with open('muzikanten.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'naam', 'woonplaats', 'genre', 'instrument']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Schrijf de header
    writer.writeheader()

    # Schrijf de records
    for id, gegevens in muzikanten.items():
        writer.writerow({'id': id, **gegevens})

print("De gegevens zijn succesvol weggeschreven naar 'muzikanten.csv'.")
