import pygame
import tkinter.messagebox
import funkcje

#definicje
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mastermind")


#obrazki do kulek z odpowiedziami
black_ball = pygame.image.load('grafiki/black.png')
white_ball = pygame.image.load('grafiki/white.png')
black_ball = pygame.transform.scale(black_ball, (30, 30))
white_ball = pygame.transform.scale(white_ball, (30, 30))

feedback_images = {
    'y': black_ball,
    'g': white_ball,
}

#przycisk cofniecia
back_button = pygame.Rect(375,325,50,25)
confirm_button = pygame.Rect(375,375,50,25)

buttons =[
    funkcje.Circ_Pushbutton("Blue",25,(100,450),"grafiki/blue_ball.png"),
    funkcje.Circ_Pushbutton("Green",25,(200,450),"grafiki/green_ball.png"),
    funkcje.Circ_Pushbutton("Orange",25,(300,450),"grafiki/orange_ball.png"),
    funkcje.Circ_Pushbutton("Purple",25,(400,450),"grafiki/purple_ball.png")]
odpowiedz_uzytkownika = []
row_counter = 0
wylosowany_kod = funkcje.losuj_kod(4)
funkcje.draw_circles(4,8,window)



#Okno gry
pygame.init()
running = True

while running:

    #wyswietlenie przyciskow
    for b in buttons:
        b.draw(window)
    confirm_rect = funkcje.draw_button(window, "grafiki/confirm_button.png", (50, 25), (350, 315))
    delete_rect = funkcje.draw_button(window, "grafiki/delete_button.png", (50, 25), (350, 350))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #klikniecie przycisku na klawiaturze
        for b in buttons:
            if b.is_clicked(event) and len(odpowiedz_uzytkownika) < 4:
                odpowiedz_uzytkownika.append (b.get_name())
                funkcje.draw_answer(b,odpowiedz_uzytkownika,row_counter,window)
        #klikniecie jednego z przyciskow
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #przycisk usuniecia
            if delete_rect.collidepoint(event.pos):
                if (len(odpowiedz_uzytkownika) > 0):
                    funkcje.cancel_answer(window,odpowiedz_uzytkownika,row_counter)
                    odpowiedz_uzytkownika.pop(-1)
            #przycisk zatwierdzenia
            if confirm_rect.collidepoint(event.pos) and len(odpowiedz_uzytkownika) == 4:
                odpowiedz_uzytkownika = funkcje.Input_Conv(odpowiedz_uzytkownika)
                print(funkcje.Is_Correct(odpowiedz_uzytkownika, wylosowany_kod))
                
                feedback = funkcje.Is_Correct(odpowiedz_uzytkownika, wylosowany_kod)
                feedback_position = (325, 15 + row_counter * 49)
                funkcje.draw_feedback(window, feedback, feedback_position, feedback_images)

                odpowiedz_uzytkownika.clear()
                row_counter += 1
    pygame.display.update()
#Okno wygranej
    # if guess == answer:
    #    win = True
    #    tkinter.messagebox.showinfo("WYGRANA")