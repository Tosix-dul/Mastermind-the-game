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

#ograniczona_liczba_prob
# Po jej przekroczeniu bez zgadnięcia - komunikat o przegranej i wypisanie szukanego kodu
#to nie musi być w funkcji, można w samych ifach

def ograniczona_liczba_prob(limit_prob, szukany_kod, odpowiedz_uzytkownika, liczba_prob=0):
    if liczba_prob == limit_prob:
        if odpowiedz_uzytkownika != szukany_kod:
            text_surface = font.render(f"Kod: {szukany_kod}", True, WHITE)
            messagebox.showinfo("Przegrana")
    return
