#ograniczona_liczba_prob
# Po jej przekroczeniu bez zgadnięcia - komunikat o przegranej i wypisanie szukanego kodu
#to nie musi być w funkcji, można w samych ifach

def ograniczona_liczba_prob(limit_prob, szukany_kod, odpowiedz_uzytkownika, liczba_prob=0):
    if liczba_prob == limit_prob:
        if odpowiedz_uzytkownika != szukany_kod:
            text_surface = font.render(f"Kod: {szukany_kod}", True, WHITE)
            messagebox.showinfo("Przegrana")
    return
#ograniczona_liczba_prob( 7, ['n', 'z', 'n','b', 'cz'])