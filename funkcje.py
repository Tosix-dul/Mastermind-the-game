import random

#funkcja losuje kod dla komputera w postaci listy 4 intów
def losuj_kod(dlugosc=4):
    return [random.randint(1, 6) for _ in range(dlugosc)]

#kolor1 to tylko zmienna, która ma być zamieniona na kolor  
slownik_kolorow ={
    1: "kolor1",
    2: "kolor2",
    3: "kolor3",
    4: "kolor4",
    5: "kolor5",
    6: "kolor6"
}

#funkcja zamienia liczby na kolory i wypisuje je w postaci czytelnej
def wypisz_kod(kod, slownik):
    czytelny_kod = [slownik[liczba] for liczba in kod]
    print("Kod:", " ".join(czytelny_kod))