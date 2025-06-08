import pygame
import tkinter.messagebox
import funkcje
import tkinter as tk
import sys

#-----------------Definicje-------------------

#przygotowanie do wielokrotnego inputu użytkownika
user_response = []
row_counter = 0 #ilość dotychczasowych prób prób/rzędów
codeLength = 4
numberOfColorsInSequence = 4
howManyTries = 8
numberOfColorsOnKeypad = 8

# ustawienia trudności
diff_settings = funkcje.Difficulty_Settings(codeLength, howManyTries, numberOfColorsInSequence, numberOfColorsOnKeypad)

# Okno startowe
start_window = tk.Tk()
start_window.title("Mastermind")
start_window.geometry("300x400")

# Przyciski ekranu startowego
tk.Button(start_window, text="Poziom Łatwy", command=lambda: funkcje.run_level(1, diff_settings, start_window), width=25).pack(pady=5)
tk.Button(start_window, text="Poziom Średni", command=lambda: funkcje.run_level(2, diff_settings, start_window), width=25).pack(pady=5)
tk.Button(start_window, text="Poziom Trudny", command=lambda: funkcje.run_level(3, diff_settings, start_window), width=25).pack(pady=5)

tk.Button(start_window, text="Stwórz swój własny poziom", command=lambda: funkcje.custom_level(diff_settings, start_window), width=25).pack(pady=5)
tk.Button(start_window, text="Customizacja", command=lambda: funkcje.custom_design(), width=25).pack(pady=5)
tk.Button(start_window, text="Zasady gry", command=lambda: funkcje.game_rules(), width=25).pack(pady=5)
tk.Button(start_window, text="Wyjdź", command=lambda: funkcje.leave(start_window), width=25).pack(pady=10)


# Start GUI
start_window.mainloop()

#okno poziomu
WIDTH = 600
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")


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
pos_x = WIDTH/((diff_settings.number_of_colors_on_keypad-1)%4+2)
rad = 30
buttons =[
    funkcje.Circ_Pushbutton("Purple",rad,(120,550),"grafiki/purple.png"),
    funkcje.Circ_Pushbutton("Blue",rad,(2*120,550),"grafiki/blue.png"),
    funkcje.Circ_Pushbutton("Green",rad,(3*120,550),"grafiki/green.png"),
    funkcje.Circ_Pushbutton("Orange",rad,(4*120,550),"grafiki/orange.png"),
    funkcje.Circ_Pushbutton("Rainbow",rad,(pos_x,650),"grafiki/rainbow.png"),
    funkcje.Circ_Pushbutton("Bubblegum",rad,(2*pos_x,650),"grafiki/bubblegum.png"),
    funkcje.Circ_Pushbutton("Yellow",rad,(3*pos_x,650),"grafiki/yellow.png"),
    funkcje.Circ_Pushbutton("Pink",rad,(4*pos_x,650),"grafiki/pink.png")]


#szukana sekwencja
hidden_code_numbers = funkcje.random_code(diff_settings.number_of_colors_in_sequence, diff_settings.code_length)
hidden_code_colors = funkcje.rev_input_conv(hidden_code_numbers,buttons)

#-----------------------------Główna pętla programu-------------------------------


#Inicjalizacja okna gry
pygame.init()
running = True
window.blit(background_img, (0, 0))

while running:

    #wyswietlenie przyciskow zatwierdzania i cofania odpowiedzi
    for i in range (0,diff_settings.number_of_colors_on_keypad):
        buttons[i].draw(window)
    confirm_rect = funkcje.draw_button(window, "grafiki/confirm_button.png", (70, 35), (500, 425))
    delete_rect = funkcje.draw_button(window, "grafiki/delete_button.png", (70, 35), (500, 475))


    for event in pygame.event.get():
        #wyjście z gry
        if event.type == pygame.QUIT:
            running = False
        
        #klikniecie przycisku na klawiaturze wyboru kolorów
        for b in buttons:
            if b.is_clicked(event) and len(user_response) < diff_settings.code_length:
                user_response.append (b.get_name())
                funkcje.draw_answer(b,user_response,row_counter,window,diff_settings.code_length)


        #klikniecie jednego z przyciskow zatwierdzenia lub usunięcia
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            #przycisk usuniecia
            if delete_rect.collidepoint(event.pos):
                if (len(user_response) > 0):
                    funkcje.cancel_answer(window,user_response,row_counter,diff_settings.code_length)
                    user_response.pop(-1)
            
            #przycisk zatwierdzenia
            if confirm_rect.collidepoint(event.pos) and len(user_response) == diff_settings.code_length:
                user_response = funkcje.Input_Conv(user_response)
                print(funkcje.Is_Correct(user_response,hidden_code_numbers))
                
                #wyświetlanie feedbacku o poprawności próby zgadnięcia
                feedback = funkcje.Is_Correct(user_response,hidden_code_numbers)
                feedback_position = (325 , 15 + row_counter * 49)
                funkcje.draw_feedback(window, feedback, feedback_position, feedback_images)

                #Użytkownik zgadł kod - wygrana
                if funkcje.Is_Correct(user_response,hidden_code_numbers) == ['w'] * diff_settings.code_length:
                    funkcje.show_end_screen("win",hidden_code_colors)
                    running = False


                #przejście do następnej próby
                user_response.clear()
                row_counter += 1
        
        #Koniec prób - przegrana
        elif diff_settings.how_many_tries == row_counter:
            funkcje.show_end_screen("lose",hidden_code_colors)
            running = False

    pygame.display.update()
