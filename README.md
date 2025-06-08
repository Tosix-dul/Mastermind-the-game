# Mastermind-the-game
GRA – PROJEKT

POTRZEBNE STRUKTURY:
- 6 różnych kolorów kulek
- 3 małe kulki sygnału ( czarny – gracz nie trafił danej kulki, biały – wskazana przez gracza kulka ma właściwy kolor i pozycję, czerwony – gracz trafił tylko kolor, ale brak pozycji (!!! Jeżeli dany kolor został już trafiony na danej pozycji i nie występuje więcej to nie zwraca czerwonego lecz czarny))
- plansza z polem 4 – miejscowym dla osoby układającej kod, oraz w zależności od wersji 8, 10 lub 12 wierszy dla osoby zgadującej ( w każdym wierszu muszą znajdować się 4 miejsca dla 4 kulek).

ZASADA DZIAŁANIA:

POCZĄTEK:

Po włączeniu gry, gracz ma do wyboru dwie opcje: 
 - (1) czy chce zagrać w wersje singleplayer, 
 - (2) czy w wersję multiplayer (2 graczy),

 - W ilu próbach chce zagrać ( 8, 10, 12 lub inna wartość ).

 - (1) Po wybraniu opcji, komputer losuje 4 elementową kombinacje zmiennych, stworzoną z 6 możliwych przy czym zmienne mogą się powtarzać, ważna jest kolejność.
 - (2) Po wybraniu opcji, gra prosi jednego z graczy o podanie kodu na analogicznej zasadzie co w (1). Gracz wybierający kod nie bierze już udziału w grze.
   
np. [ Czerwony, czerwony, niebieski, zielony ]

Dla zmiennych powinno wyglądać to następująco
[ t[0] = 1, t[1] = 1, t[2] = 3, t[3] = 5 ]
gdzie 1 – wartość dla czerwonego, itp.

DALEJ TAKI SAM PRZEBIEG DLA (1) i (2)

Po wybraniu kodu, gracz przystępuje do fazy właściwej gry. Zadaniem gracza jest w wybranej liczbie tur zgadnąć kod. 

FAZA ZGADYWANIA

Każda z n tur składa się z następującej czynności:
- gracz podaje kombinacje 4 kulek
- gra weryfikuje poprawność kodu
- gra zwraca wynik w podanej postaci – kombinacja 4 sygnałów

Np. Jeżeli gracz podał kod 1132, a kod szukany to 0512 to gra powinna zwrócić podaną kolejność sygnałów – czarny, czarny, czerwony, biały.

Inny przykład: kod podany 4452, kod 4242, sygnał – biały, czarny, czerwony, biały. 

ZAKOŃCZENIE

Gracz wygrywa jeżeli, w dostępnej liczbie prób, poda całkowicie poprawny kod.

Gracz przerywa, jeżeli nie poda poprawnego kodu w limicie prób.

UWAGA
- Okno gry powinno wyświetlać całość historii obecnej gry, nie tylko ostatnią turę. 

---------------------------------------------------------------------------------------------------------------------
LISTA ZMIENNYCH GLOBALNYCH (nie używamy polskich znaków i wielkich liter do nazw):
hidden_code - kod ustalony randomowo do zgadnięcia
trial_limit - limit ustawiony w zależności od poziomu
how_many_tries - numer obecnej próby zgadnięcia kodu, musi być <= limit_prob
user_response - kod imputowany przez gracza, który my interpretujemy
proper_code - sprawdzona poprawność kodu (brak koloru, kolor występuje i jest w dobrym miejscu, kolor występuje ale jest w złym miejscu)
custom_lvl - tworzenie nowewgo poziomu przez użytkownika
custom_design - możliwość dostosowania estetyki gry
number_of_colors_in_sequence - zmienna określająca ilość kolorów, jej wartość zmienia się w różnych pozimach
game_rules - funkcja wyświetlająca zasady gry
leave - możliwość zamknięcia gry przez UI
random_code - funkcja losowania kodu
how_many_missing - 
hidden_code_copy - kopia ukrytego kodu, aby móc wykonywać na niej operacje nie wpływając na właściwy kod

