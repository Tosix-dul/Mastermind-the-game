import pygame
import tkinter.messagebox


#konwersja inputu na string cyfr
def Input_Conv (odpowiedz_uzytkownika = []): #gotowe, do zmiany dopiero w sprincie 2.
    len = 4
    dict_color = {"kolor1":"1","kolor2":"2","kolor3":"3","kolor4":"4"}
    odpowiedz_uzytkownika = [str(input(f"Wpisz {i + 1}. kolor: ")) for i in range(len)] #tymczasowe, potem bedzie podawane jako parametr funkcji
    odpowiedz_uzytkownika = [dict_color[odpowiedz_uzytkownika[i]] for i in range(len(odpowiedz_uzytkownika))]
    return odpowiedz_uzytkownika


#sprawdzenie poprawnosci inputu uzytkownika
def Is_Correct(odpowiedz_uzytkownika, szukany_kod): #gotowe, wazne wstawic input uzytkownika skonwertowany funkcja Input_Conv !!!
    # w sprint 2. zmienic sposob wyswietlania wyniku
    popr_kod = ['r' for i in range(len(odpowiedz_uzytkownika))]
    mem = [i for i in range(len(odpowiedz_uzytkownika))]
    kod_cpy = szukany_kod.copy()
    # sprawdzenie dobrych kolorow w dobrym miejscu
    for i in range(len(odpowiedz_uzytkownika)):
        if szukany_kod[i] == odpowiedz_uzytkownika[i]:
            popr_kod[i] = 'g'
            mem.remove(i)
            kod_cpy.remove(szukany_kod[i])
    # sprawdzenie dobrych kolorow w zlym miejscu
    for i in mem:
        if odpowiedz_uzytkownika[i] in kod_cpy:
            popr_kod[i] = 'y'
            kod_cpy.remove(odpowiedz_uzytkownika[i])

    return popr_kod



#Okno gry
pygame.init()
running = True

while running:
    pass
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Mastermind")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Okno wygranej
    # if guess == answer:
        win = True
        tkinter.messagebox.showinfo("WYGRANA")