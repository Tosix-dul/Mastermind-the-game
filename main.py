import pygame
import tkinter.messagebox
import funkcje

#definicje
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mastermind")
#przycisk cofniecia
back_button = pygame.Rect(375,350,50,25)
buttons =[
    funkcje.Circ_Pushbutton("Blue",25,(100,450),"grafiki/blue_ball.png"),
    funkcje.Circ_Pushbutton("Green",25,(200,450),"grafiki/green_ball.png"),
    funkcje.Circ_Pushbutton("Orange",25,(300,450),"grafiki/orange_ball.png"),
    funkcje.Circ_Pushbutton("Purple",25,(400,450),"grafiki/purple_ball.png")]
odpowiedz_uzytkownika = []
wylosowany_kod = funkcje.losuj_kod(4)




#Okno gry
pygame.init()
running = True

while running:

    #wyswietlenie przyciskow
    for b in buttons:
        b.draw(window)
    pygame.draw.rect(window,(255,0,0),back_button)

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.collidepoint(event.pos):
            if (len(odpowiedz_uzytkownika) > 0):
                odpowiedz_uzytkownika.pop(-1)
    pygame.display.update()
#Okno wygranej
    # if guess == answer:
    #    win = True
    #    tkinter.messagebox.showinfo("WYGRANA")