# Mastermind-the-game
GRA – PROJEKT

Potrzebne struktury:
- 6 różnych kolorów kulek
- 3 małe kulki sygnału ( czarny – gracz nie trafił danej kulki, biały – wskazana przez gracza kulka ma właściwy kolor i pozycję, czerwony – gracz trafił tylko kolor, ale brak pozycji (!!! Jeżeli dany kolor został już trafiony na danej pozycji i nie występuje więcej razy,  to nie zwraca czerwonego lecz czarny) 
- plansza z polem 4 – miejscowym dla osoby układającej kod, oraz w zależności od wersji 8, 10 lub 12 wierszy dla osoby zgadującej ( w każdym wierszu muszą znajdować się 4 miejsca dla 4 kulek.

Zasada działania:

FAZA POCZĄTKOWA

Po włączeniu gry, gracz ma do wyboru dwie opcje: 
 - (1) czy chce zagrać w wersje singleplayer, 
 - (2) czy w wersję multiplayer (2 graczy). 

następnie:
 - Oraz w ilu próbach chce zagrać ( 8, 10, 12 lub inna wartość )

 - (1) Po wybraniu opcji, komputer losuje 4 elementową kombinacje zmiennych, stworzoną z 6 możliwych, przy czym zmienne mogą się powtarzać. WAŻNA jest kolejność.
 - (2) Po wybraniu opcji, gra prosi jednego z graczy o podanie kodu. Gracz wybierający kod nie bierze już udziału w grze. 

DALEJ TAKI SAM PRZEBIEG DLA (1) i (2)

kod powinien wyglądać następująco:

np. [ Czerwony, czerwony, niebieski, zielony ]

Dla zmiennych powinno wyglądać to następująco
[ t[0] = 1, t[1] = 1, t[2] = 3, t[3] = 5 ]
gdzie 1 – wartość dla czerwonego, itp.

Po wybraniu kodu, gracz przystępuje do fazy właściwej gry. Zadaniem gracza jest w wybranej liczbie tur zgadnąć kod. 

FAZA ZGADYWANIA

Każda z n tur składa się z następującej czynności:
- gracz podaje kombinacje 4 kulek
- gra weryfikuje poprawność kodu
- gra zwraca wynik w podanej postaci – kombinacja 4 sygnałów

Np. 
	- Jeżeli gracz podał kod 1132, a kod szukany to 0512 to gra powinna zwrócić podaną kolejność sygnałów – czarny, czarny, czerwony, biały. 
	Inny przykład: kod podany 4452, kod 4242, sygnał – biały, czarny, czerwony, biały. 

ZAKOŃCZENIE

Gracz wygrywa jeżeli, w dostępnej liczbie prób, poda całkowicie poprawny kod.

Gracz przerywa jeżeli nie poda poprawnego kodu, w limicie prób.

UWAGI

Okno gry powinno wyświetlać całość przebiegu gry, nie tylko ostatnią turę.
