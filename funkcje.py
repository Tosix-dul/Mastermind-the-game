import random
from tkinter import messagebox, font
import pygame
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import os
import sys

#-------------------------Ustawienia----------------------------
class Difficulty_Settings:
    def __init__(self, code_length: int,  how_many_tries: int, number_of_colors_in_sequence: int, number_of_colors_on_keypad: int):
        self.code_length = code_length
        self.how_many_tries = how_many_tries
        self.number_of_colors_in_sequence = number_of_colors_in_sequence
        self.number_of_colors_on_keypad = number_of_colors_on_keypad
        

    #POZIOM ŁATWY
    # kod długości 4
    # 6 prób
    # sekwencja złożona z 4 kolorów
    # 4 kolory do wyboru, 
    def easy_mode(self):
        self.code_length = 4
        self.how_many_tries = 6
        self.number_of_colors_in_sequence = 4
        self.number_of_colors_on_keypad = 4
    
    #POZIOM ŚREDNI
    # kod długości 6
    # 6 prób
    # sekwencja złożona z 5 kolorów
    # 6 kolorów do wyboru,
    def advanced_mode(self):
        self.code_length = 6
        self.how_many_tries = 6
        self.number_of_colors_in_sequence = 5
        self.number_of_colors_on_keypad = 6

    #POZIOM TRUDNY
    # kod długości 8
    # 6 prób
    # sekwencja złożona z 6 kolorów
    # 8 kolorów do wyboru,
    def hard_mode(self):    
        self.code_length = 8
        self.how_many_tries = 6
        self.number_of_colors_in_sequence = 6
        self.number_of_colors_on_keypad = 8

        
    def custom_mode(self, code_length: int=4,  how_many_tries: int=4, number_of_colors_in_sequence: int=4, number_of_colors_on_keypad: int=4):
        self.code_length = code_length
        self.how_many_tries = how_many_tries
        self.number_of_colors_in_sequence = number_of_colors_in_sequence
        self.number_of_colors_on_keypad = number_of_colors_on_keypad


#-----------------------------Ekran Startowy------------------------------

# Funkcja okna dialogowego; Poziom 1, Poziom 2, Poziom 3, Wyjdź, “Stwórz swój własny poziom”, Customizacja, Zasady gry

# Definicje do przycisków ekranu startowego
def run_level(lvl_nr, difficulty: Difficulty_Settings, window):
    print(f"Uruchamiam poziom {lvl_nr}")
    match lvl_nr:
        case 1:
            difficulty.easy_mode()
        case 2:
            difficulty.advanced_mode()
        case 3:
            difficulty.hard_mode()
    
    window.destroy()

# Okno do tworzenia poziomu o customowej trudności
def stworz_poziom(difficulty_settings: Difficulty_Settings, window):
    window.destroy()
    custom_diff_window = tk.Tk()
    custom_diff_window.title("Customise your game!")
    custom_diff_window.geometry("300x300")

    options = list(range(1,8))
    str_options = list(map(str, options))

    custom_settings = {"code_length": 4, "how_many_tries": 4, "number_of_colors_in_sequence": 4, "number_of_colors_on_keypad": 4}
    
    
    # Funkcje pobiarające wybór z opcji wyborów i dodająca go do listy ustawień

    def valueCL(selection): 
        custom_settings["code_length"] = int(selection)

        # Możliwość wyboru ilości kolorów w sekwencji dostępna dopiero po wybraniu długości sekwencji    
        L3 = tk.Label(custom_diff_window, text="The number of colors in hidden code")
        L3.pack()
        Number_Of_Colors_In_Sequence = tk.StringVar(custom_diff_window)
        Number_Of_Colors_In_Sequence.set("Number of colors in sequence")

        options_colors_in_sequ = list(range(1,int(selection)+1)) # nie można wybrać więcej kolorów w sekwencji niż jej długość
        str_options_colors_in_sequ = list(map(str, options_colors_in_sequ))

        Number_Of_Colors_In_Sequence = tk.OptionMenu(custom_diff_window, Number_Of_Colors_In_Sequence, *str_options_colors_in_sequ, command=valueNCS)
        Number_Of_Colors_In_Sequence.pack()

    def valueHMT(selection): 
        custom_settings["how_many_tries"] = int(selection)

    def valueNCS(selection): 
        custom_settings["number_of_colors_in_sequence"] = int(selection)

        # Możliwość wyboru ilości kolorów na klawiaturze dostępna dopiero po wybraniu ilości kolorów w sekwencji
        L4 = tk.Label(custom_diff_window, text="The number of colors on keypad")
        L4.pack()
        Number_Of_Colors_On_Keypad = tk.StringVar(custom_diff_window)
        Number_Of_Colors_On_Keypad.set("Number of colors on keypad")

        options_colors_on_keyp = list(range(int(selection), 9)) # nie można wybrać mniej kolorów na klawiaturze niż jest w sekwencji
        str_options_colors_on_keyp = list(map(str, options_colors_on_keyp))

        Number_Of_Colors_On_Keypad = tk.OptionMenu(custom_diff_window, Number_Of_Colors_On_Keypad, *str_options_colors_on_keyp, command=valueNCK)
        Number_Of_Colors_On_Keypad.pack()
    
    def valueNCK(selection): 
        custom_settings["number_of_colors_on_keypad"] = int(selection)


    L1 = tk.Label(custom_diff_window, text="The length of the hidden code")
    L1.pack()
    Code_Length = tk.StringVar(custom_diff_window)
    Code_Length.set("Code length")
    Code_Length = tk.OptionMenu(custom_diff_window, Code_Length, *str_options, command=valueCL)
    Code_Length.pack()

    L2 = tk.Label(custom_diff_window, text="The number of tries")
    L2.pack()
    How_Many_Tries = tk.StringVar(custom_diff_window)
    How_Many_Tries.set("How many tries")
    How_Many_Tries = tk.OptionMenu(custom_diff_window, How_Many_Tries, *str_options, command=valueHMT)
    How_Many_Tries.pack()


    tk.Button(custom_diff_window, text="Zatwierdź", command=lambda: difficulty_settings.custom_mode(code_length=custom_settings["code_length"], how_many_tries=custom_settings["how_many_tries"], 
                                                                                                    number_of_colors_in_sequence=custom_settings["number_of_colors_in_sequence"], 
                                                                                                    number_of_colors_on_keypad=custom_settings["number_of_colors_on_keypad"]), 
                                                                                                                                                        width=25).pack(pady=8)
    tk.Button(custom_diff_window, text="Graj", command=lambda: custom_diff_window.destroy(), width=25).pack(pady=8)

    custom_diff_window.mainloop()


def custom_deisgn():
    messagebox.showinfo("Customizacja", "Opcje personalizacji gracza.")


def game_rules():
    messagebox.showinfo("Zasady gry", "Tutaj znajdują się zasady gry...")
    pygame.init()
    window = pygame.display.set_mode((480, 640))
    info_button(window)

def leave(window):
    window.destroy()
    sys.exit()


#-----------------------Okno Poziomu------------------------

#definicja słowników do pobierania inputu
dict_color_to_number = {"Purple":1,"Blue":2,"Green":3,"Orange":4,"Rainbow":5,"Bubblegum":6,"Yellow":7,"Pink":8}
dict_number_to_color = {1:"Purple", 2:"Blue",3:"Green",4:"Orange",5:"Rainbow",6:"Bubblegum",7:"Yellow",8:"Pink"}


#funkcja losuje kod dla komputera w postaci listy 4 intów
def random_code(number_of_colors_in_sequence, code_length=4):
    code = list(range(1,number_of_colors_in_sequence+1))
    how_many_missing = code_length - number_of_colors_in_sequence
    for i in range(how_many_missing, 0, -1):
        code.append(random.randint(1,number_of_colors_in_sequence)) #dolosowujemy powtarzające się już kolory do sekwencji żeby długość się zgadzała
    random.shuffle(code)
    return code



# rysowanie kółek do wyświetlania obecnych i przyszłych prób użytkownika
def draw_circles (size_of_guess, n0_of_guesses, window):
    for i in range(n0_of_guesses):
        for j in range(size_of_guess):
            pygame.draw.circle(window, (33, 33, 33), (100 + 50 * j, 25 + 50 * i), 24, 1)

def info_button (screen):
    info_popup = pygame.image.load("grafiki/info.png").convert_alpha()
    info_popup = pygame.transform.scale(info_popup,(480,640))
    info_rect = info_popup.get_rect()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.MOUSEBUTTONDOWN and info_rect.collidepoint(event.pos)):
                running = False
                pygame.quit()
                break


        screen.blit(info_popup, (0,0))

        pygame.display.flip()
  

#-----------------Input użytkownika------------------

#klasa przycisków w klawiaturze kolorów
class Circ_Pushbutton:
    def __init__ (self, name,radius,center,image_path):
        self.name = name
        self.radius = radius
        self.center = center
        self.image_path = (pygame.image.load(image_path).convert_alpha())
    def draw (self, surface):
        size_adj = pygame.transform.scale(self.image_path, (self.radius*2, self.radius*2))
        surface.blit(size_adj, (self.center[0]-self.radius, self.center[1]-self.radius))
    def draw_as_answer(self,surface,center,radius_adj):
        draw_radius = 25 / radius_adj
        size_adj = pygame.transform.scale(self.image_path, (2*draw_radius,2*draw_radius))
        surface.blit(size_adj, (center[0]-draw_radius, center[1]-draw_radius))
    def is_clicked (self,event):
        mouse_pos = pygame.mouse.get_pos()
        in_circ = pow(self.center[0] - mouse_pos[0],2)+pow(self.center[1] - mouse_pos[1],2)
        return (in_circ <= pow(self.radius,2) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)
        #ew. dodać zmianę koloru przy najechaniu
    def get_name (self):
        return self.name

#rysowanie prostokątnych przycisków
def draw_button(window,image_path,size,place):
    drawing = pygame.transform.scale((pygame.image.load(image_path).convert_alpha()),size)
    window.blit(drawing,place)
    rect = drawing.get_rect(left=place[0], top=place[1])
    return rect

#rysowanie pojedynczej odpowiedzi
def draw_answer (button , user_response , row_counter, window, code_length):
    button.draw_as_answer(window,(100+50*(len(user_response)-1)/((code_length)/4),25+50*row_counter),(code_length)/4)

#usuwanie pojedynczej odpowiedzi
def cancel_answer(window, user_response , row_counter, code_length):
    center = (100 + 50 * (len(user_response)-1)/((code_length)/4), 25 + 50 * row_counter)
    radius = 26/((code_length)/4)
    background = Image.open("grafiki/stone_background.jpg").convert("RGBA")
    circle = Image.new("L", background.size, 0)
    draw = ImageDraw.Draw(circle)
    left_up = (center[0] - radius, center[1] - radius)
    right_down = (center[0] + radius, center[1] + radius)
    draw.ellipse([left_up, right_down], fill=255)
    overlay = Image.new("RGBA", background.size)
    overlay.paste(background, (0, 0), mask=circle)
    result = overlay.crop((left_up[0], left_up[1], right_down[0], right_down[1]))
    surface = pygame.image.fromstring(result.tobytes(), result.size, result.mode)
    window.blit(surface,(left_up[0], left_up[1]))


#-------------------Szukana sekwencja a input użytkownika--------------------------

#konwersja kolorów na string cyfr
"""DO ZMIANY W SPRINCIE 2"""
def Input_Conv (user_response): 
    user_response = [dict_color_to_number[user_response[i]] for i in range(len(user_response))]
    return user_response

#konwersja cyfr na nazwy kolorów
def rev_input_conv(hidden_code,buttons):
    hidden_code = [dict_number_to_color[hidden_code[i]] for i in range(len(hidden_code))]
    hidden_code = [button for i in range(len(hidden_code)) for button in buttons  if button.get_name()==hidden_code[i]]
    return hidden_code


#sprawdzenie poprawnosci inputu uzytkownika
"""!!! Wazne wstawic input uzytkownika skonwertowany funkcja Input_Conv !!!"""
def Is_Correct(user_response, hidden_code): 
    proper_code = ['r' for i in range(len(user_response))]
    mem = [i for i in range(len(user_response))]
    hidden_code_copy = hidden_code.copy()
    
    # sprawdzenie dobrych kolorow w dobrym miejscu
    for i in range(len(user_response)):
        if hidden_code[i] == user_response[i]:
            proper_code[i] = 'w'
            mem.remove(i)
            hidden_code_copy.remove(hidden_code[i])
    
    # sprawdzenie dobrych kolorow w zlym miejscu
    for i in mem:
        if user_response[i] in hidden_code_copy:
            proper_code[i] = 'b'
            hidden_code_copy.remove(user_response[i])

    return proper_code


#rysowanie odpowiedzi zwrotnej dla użytkownika - poprawność jego próby
def draw_feedback(window, feedback, pos, images, spacing=4):
    x, y = pos
    current_x = x
    random.shuffle(feedback) #kulki z feedbackiem nie są powiązane z konkretnym kolorem

    for symbol in feedback:
        if symbol == 'r':
            continue
        img = images.get(symbol)
        if img:
            window.blit(img, (current_x, y))
            current_x += img.get_width() + spacing


#------------------Koniec gry--------------------

#wyświetla ekran końcowy gry z komunikatem o wygranej lub przegranej i przycisk "Spróbuj ponownie"
def show_end_screen(result: str,hidden_code):
    if result not in ['win', 'lose']:
        raise ValueError("Użyj: 'win' lub 'lose' jako parametr.")

    # Inicjalizacja Pygame
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Koniec gry")

    # Kolory
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (76, 175, 80)
    RED = (244, 67, 54)
    GRAY = (220, 220, 220)
    DARK_GRAY = (180, 180, 180)

    # Czcionki
    font_big = pygame.font.SysFont("arial", 40, bold=True)
    font_small = pygame.font.SysFont("arial", 28)

    # Tekst i tło
    if result == "win":
        title = "Wygrałeś, Gratulacje!"
        bg = GREEN
    else:
        title = "Przegrałeś"
        bg = RED
        # Tekst główny
        title_surface = font_big.render(title, True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(title_surface, title_rect)

        # Przycisk
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, DARK_GRAY if button_rect.collidepoint(mouse_pos) else GRAY, button_rect, border_radius=10)
        button_text = font_small.render("Spróbuj ponownie", True, BLACK)
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

        #Szukany kod
        text = font_small.render("Prawidłowy kod: ", True, WHITE)
        for i in range(len(hidden_code)):
            hidden_code[i].draw_as_answer(screen,(WIDTH // 2 + 50*i , HEIGHT // 2 + 40))
        screen.blit(text, text.get_rect(center=(WIDTH // 2 - 120, HEIGHT // 2 + 40)))



        pygame.display.flip()
        pygame.time.Clock().tick(60)

    #pygame.quit()
