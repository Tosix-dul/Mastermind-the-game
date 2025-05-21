import pygame
import tkinter.messagebox
import funkcje

#definicje
buttons =[
    funkcje.Circ_Pushbutton("Purple",(179, 157, 219),(100,450),25),
    funkcje.Circ_Pushbutton("Blue",(176, 224, 230),(200,450),25),
    funkcje.Circ_Pushbutton("Green",(197, 219, 174),(300,450),25),
    funkcje.Circ_Pushbutton("Orange",(250, 199, 192),(400,450),25)]
odpowiedz_uzytkownika = []
wylosowany_kod = funkcje.losuj_kod(4)
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mastermind")



#Okno gry
pygame.init()
running = True

while running:

    #wyswietlenie przyciskow
    for b in buttons:
        b.draw(window)

    # sprawdzenie poprawnosci odpowiedzi
    if (len(odpowiedz_uzytkownika) == 4):
        odpowiedz_uzytkownika = funkcje.Input_Conv(odpowiedz_uzytkownika)
        print(funkcje.Is_Correct(odpowiedz_uzytkownika,wylosowany_kod))
        odpowiedz_uzytkownika.clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for b in buttons:
            if b.is_clicked(event):
                #tymczasowe
                print("Button:",b.get_name())
                odpowiedz_uzytkownika.append (b.get_name())
    pygame.display.update()
#Okno wygranej
    # if guess == answer:
    #    win = True
    #    tkinter.messagebox.showinfo("WYGRANA")