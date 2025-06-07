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

        
    def custom_mode(self, code_length: int,  how_many_tries: int, number_of_colors_in_sequence: int, number_of_colors_on_keypad: int):
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

def stworz_poziom():
    messagebox.showinfo("Stwórz poziom", "Tutaj możesz stworzyć swój własny poziom.")

def customizacja():
    messagebox.showinfo("Customizacja", "Opcje personalizacji gracza.")

def zasady_gry():
    messagebox.showinfo("Zasady gry", "Tutaj znajdują się zasady gry...")

def wyjdz(window):
    window.destroy()
    sys.exit()


#-----------------------Okno Poziomu------------------------

#definicja słłowników do pobierania inputu
dict_color_to_number = {"Blue":1,"Green":2,"Orange":3,"Rainbow":4,"Bubblegum":5,"Yellow":6,"Pink":7,"Purple":8}
dict_number_to_color = {1:"Blue",2:"Green",3:"Orange",4:"Rainbow",5:"Bubblegum",6:"Yellow",7:"Pink",8:"Purple",}


#funkcja losuje kod dla komputera w postaci listy 4 intów
def losuj_kod(liczba_kolorow, dlugosc=4):
    kod = list(range(1,liczba_kolorow+1))
    ile_brakuje = dlugosc - liczba_kolorow
    if ile_brakuje != 0:
        kod.extend(random.sample(range(1,liczba_kolorow), ile_brakuje)) #dolosowujemy powtarzające się już kolory do sekwencji żeby długość się zgadzała
    random.shuffle(kod)
    return kod

# rysowanie kółek do wyświetlania obecnych i przyszłych prób użytkownika
def draw_circles (size_of_guess, n0_of_guesses, window):
    for i in range(n0_of_guesses):
        for j in range(size_of_guess):
            pygame.draw.circle(window, (33, 33, 33), (100 + 50 * j, 25 + 50 * i), 24, 1)

def info_button (screen,bckg):
    info_popup = pygame.image.load("grafiki/info.png").convert_alpha()
    info_popup = pygame.transform.scale(info_popup,(450,650))
    info_rect = info_popup.get_rect()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.MOUSEBUTTONDOWN and not info_rect.collidepoint(event.pos)):
                running = False


        screen.blit(info_popup, (75, 25))

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
    def draw_as_answer(self,surface,center):
        size_adj = pygame.transform.scale(self.image_path, (50,50))
        surface.blit(size_adj, (center[0]-self.radius, center[1]-self.radius))
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
def draw_answer (button , odpowiedz_uzytkownika , row_counter, window):
    button.draw_as_answer(window,(100+50*(len(odpowiedz_uzytkownika)-1),25+50*row_counter))

#usuwanie pojedynczej odpowiedzi
def cancel_answer(window, odpowiedz_uzytkownika , row_counter):
    center = (100 + 50 * (len(odpowiedz_uzytkownika)-1), 25 + 50 * row_counter)
    radius = 26
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
    window.blit(surface,left_up)


#-------------------Szukana sekwencja a input użytkownika--------------------------

#konwersja kolorów na string cyfr
"""DO ZMIANY W SPRINCIE 2"""
def Input_Conv (odpowiedz_uzytkownika): 
    odpowiedz_uzytkownika = [dict_color_to_number[odpowiedz_uzytkownika[i]] for i in range(len(odpowiedz_uzytkownika))]
    return odpowiedz_uzytkownika

#konwersja cyfr na nazwy kolorów
def rev_input_conv(szukany_kod,buttons):
    szukany_kod = [dict_number_to_color[szukany_kod[i]] for i in range(len(szukany_kod))]
    szukany_kod = [button for i in range(len(szukany_kod)) for button in buttons  if button.get_name()==szukany_kod[i]]
    return szukany_kod


#sprawdzenie poprawnosci inputu uzytkownika
"""!!! Wazne wstawic input uzytkownika skonwertowany funkcja Input_Conv !!!"""
def Is_Correct(odpowiedz_uzytkownika, szukany_kod): 
    popr_kod = ['r' for i in range(len(odpowiedz_uzytkownika))]
    mem = [i for i in range(len(odpowiedz_uzytkownika))]
    kod_cpy = szukany_kod.copy()
    
    # sprawdzenie dobrych kolorow w dobrym miejscu
    for i in range(len(odpowiedz_uzytkownika)):
        if szukany_kod[i] == odpowiedz_uzytkownika[i]:
            popr_kod[i] = 'w'
            mem.remove(i)
            kod_cpy.remove(szukany_kod[i])
    
    # sprawdzenie dobrych kolorow w zlym miejscu
    for i in mem:
        if odpowiedz_uzytkownika[i] in kod_cpy:
            popr_kod[i] = 'b'
            kod_cpy.remove(odpowiedz_uzytkownika[i])

    return popr_kod


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
def show_end_screen(result: str,wylosowany_kod):
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
        for i in range(len(wylosowany_kod)):
            wylosowany_kod[i].draw_as_answer(screen,(WIDTH // 2 + 50*i , HEIGHT // 2 + 40))
        screen.blit(text, text.get_rect(center=(WIDTH // 2 - 120, HEIGHT // 2 + 40)))



        pygame.display.flip()
        pygame.time.Clock().tick(60)

    #pygame.quit()
