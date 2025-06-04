import pygame
import tkinter.messagebox
import funkcje
import tkinter as tk
import sys
#-----------------Definicje-------------------

#okno gry
WIDTH = 600
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")

#przygotowanie do wielokrotnego inputu użytkownika
odpowiedz_uzytkownika = []
row_counter = 0 #ilość dotychczasowych prób prób/rzędów
codeLength = 4
numberOfColorsInSequence = 4
howManyTries = 8
numberOfColorsOnKeypad = 8

# ustawienia trudności
diff_settings = funkcje.Difficulty_Settings(codeLength, howManyTries, numberOfColorsInSequence, numberOfColorsOnKeypad)

#Tło
background_img = pygame.image.load("grafiki/stone_background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

#obrazki do kulek z odpowiedziami
black_ball = pygame.image.load('grafiki/black.png')
white_ball = pygame.image.load('grafiki/white.png')
black_ball = pygame.transform.scale(black_ball, (30, 30))
white_ball = pygame.transform.scale(white_ball, (30, 30))

feedback_images = {
    'b': black_ball,
    'w': white_ball,
}


#Klawiatura kolorów
#Zakladam min. 4 kolory, jeśli możliwe mniej, zmienic
pos_x = WIDTH/((numberOfColorsOnKeypad-1)%4+2)
rad = 30
buttons =[
    funkcje.Circ_Pushbutton("Blue",rad,(120,550),"grafiki/blue.png"),
    funkcje.Circ_Pushbutton("Green",rad,(2*120,550),"grafiki/green.png"),
    funkcje.Circ_Pushbutton("Orange",rad,(3*120,550),"grafiki/orange.png"),
    funkcje.Circ_Pushbutton("Rainbow",rad,(4*120,550),"grafiki/rainbow.png"),
    funkcje.Circ_Pushbutton("Bubblegum",rad,(pos_x,650),"grafiki/bubblegum.png"),
    funkcje.Circ_Pushbutton("Yellow",rad,(2*pos_x,650),"grafiki/yellow.png"),
    funkcje.Circ_Pushbutton("Pink",rad,(3*pos_x,650),"grafiki/pink.png"),
    funkcje.Circ_Pushbutton("Purple",rad,(4*pos_x,650),"grafiki/purple.png")]
#info button


#szukana sekwencja
wylosowany_kod_numbers = funkcje.losuj_kod(diff_settings.number_of_colors_in_sequence, diff_settings.code_length)
wylosowany_kod_colors = funkcje.rev_input_conv(wylosowany_kod_numbers,buttons)

#-----------------------------Główna pętla programu-------------------------------

# Główne okno tkinter
start_window = tk.Tk()
start_window.title("Mastermind")
start_window.geometry("300x400")

# Przyciski
tk.Button(start_window, text="Poziom Łatwy", command=funkcje.start_poziom(1, start_window), width=25).pack(pady=5)
tk.Button(start_window, text="Poziom Średni", command=funkcje.start_poziom(2, start_window), width=25).pack(pady=5)
tk.Button(start_window, text="Poziom Trudny", command=funkcje.start_poziom(3, start_window), width=25).pack(pady=5)

tk.Button(start_window, text="Stwórz swój własny poziom", command=funkcje.stworz_poziom, width=25).pack(pady=5)
tk.Button(start_window, text="Customizacja", command=funkcje.customizacja, width=25).pack(pady=5)
tk.Button(start_window, text="Zasady gry", command=funkcje.zasady_gry, width=25).pack(pady=5)
tk.Button(start_window, text="Wyjdź", command=funkcje.wyjdz(start_window), width=25).pack(pady=10)


# Start GUI
start_window.mainloop()

#Inicjalizacja okna gry
pygame.init()
running = True
window.blit(background_img, (0, 0))

while running:

    #wyswietlenie przyciskow zatwierdzania i cofania odpowiedzi
    for i in range (0,numberOfColorsOnKeypad):
        buttons[i].draw(window)
    confirm_rect = funkcje.draw_button(window, "grafiki/confirm_button.png", (70, 35), (500, 425))
    delete_rect = funkcje.draw_button(window, "grafiki/delete_button.png", (70, 35), (500, 475))
    
    # przycisk do wyświetlania zasad - ostatecznie dodana do menu poczatkowego, dlatego na razie wyjscie z niej powoduje bledy
    info_circle = pygame.draw.circle(window,(65, 105, 225),(550,50),10)
    info_text = pygame.font.SysFont("arial",18).render('i',True,(255,255,255))
    window.blit(info_text,info_text.get_rect(center=(550,50)))

    for event in pygame.event.get():
        #wyjście z gry
        if event.type == pygame.QUIT:
            running = False
        
        #klikniecie przycisku na klawiaturze wyboru kolorów
        for b in buttons:
            if b.is_clicked(event) and len(odpowiedz_uzytkownika) < 4:
                odpowiedz_uzytkownika.append (b.get_name())
                funkcje.draw_answer(b,odpowiedz_uzytkownika,row_counter,window)


        #klikniecie jednego z przyciskow zatwierdzenia lub usunięcia
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # przycisk info
            if info_circle.collidepoint(event.pos):
                funkcje.info_button(window, background_img)
                window.blit(background_img, (0, 0))
            
            #przycisk usuniecia
            if delete_rect.collidepoint(event.pos):
                if (len(odpowiedz_uzytkownika) > 0):
                    funkcje.cancel_answer(window,odpowiedz_uzytkownika,row_counter)
                    odpowiedz_uzytkownika.pop(-1)
            
            #przycisk zatwierdzenia
            if confirm_rect.collidepoint(event.pos) and len(odpowiedz_uzytkownika) == 4:
                odpowiedz_uzytkownika = funkcje.Input_Conv(odpowiedz_uzytkownika)
                print(funkcje.Is_Correct(odpowiedz_uzytkownika,wylosowany_kod_numbers))
                
                #wyświetlanie feedbacku o poprawności próby zgadnięcia
                feedback = funkcje.Is_Correct(odpowiedz_uzytkownika,wylosowany_kod_numbers)
                feedback_position = (325, 15 + row_counter * 49)
                funkcje.draw_feedback(window, feedback, feedback_position, feedback_images)

                #Użytkownik zgadł kod - wygrana
                if funkcje.Is_Correct(odpowiedz_uzytkownika,wylosowany_kod_numbers) == ['w'] * diff_settings.code_length:
                    funkcje.show_end_screen("win",wylosowany_kod_colors)
                    running = False


                #przejście do następnej próby
                odpowiedz_uzytkownika.clear()
                row_counter += 1
        
        #Koniec prób - przegrana
        elif diff_settings.how_many_tries == row_counter:
            funkcje.show_end_screen("lose",wylosowany_kod_colors)
            running = False

    pygame.display.update()
