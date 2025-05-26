import random
from tkinter import messagebox, font
import pygame
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

#-----------------Przygotowanie do gry------------------

#funkcja losuje kod dla komputera w postaci listy 4 intów
def losuj_kod(liczba_kolorow,dlugosc=4):
    return [random.randint(1,liczba_kolorow) for _ in range(dlugosc)]

# rysowanie kółek do wyświetlania obecnych i przyszłych prób użytkownika
def draw_circles (size_of_guess, n0_of_guesses, window):
    for i in range(n0_of_guesses):
        for j in range(size_of_guess):
            pygame.draw.circle(window, (211, 211, 211), (100 + 50 * j, 25 + 50 * i), 24, 1)


#-----------------Input użytkownika------------------

#klasa przycisków w klawiaturze kolorów
class Circ_Pushbutton:
    def __init__ (self, name,radius,center,image_path):
        self.name = name
        self.radius = radius
        self.center = center
        self.image_path = pygame.transform.scale((pygame.image.load(image_path).convert_alpha()),(self.radius*2,self.radius*2))
    def draw (self, surface):
        surface.blit(self.image_path, (self.center[0]-self.radius, self.center[1]-self.radius))
    def draw_as_answer(self,surface,center):
        surface.blit(self.image_path, (center[0]-self.radius, center[1]-self.radius))
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
    pygame.draw.circle(window,(0,0,0),(100 + 50 * (len(odpowiedz_uzytkownika)-1), 25 + 50 * row_counter),26)
    pygame.draw.circle(window, (211, 211, 211), (100 + 50 * (len(odpowiedz_uzytkownika)-1), 25 + 50 * row_counter), 24, 1)


#-------------------Szukana sekwencja a input użytkownika--------------------------

#konwersja inputu na string cyfr
"""DO ZMIANY W SPRINCIE 2"""
def Input_Conv (odpowiedz_uzytkownika): 
    dict_color = {"Purple":1,"Blue":2,"Green":3,"Orange":4}
    odpowiedz_uzytkownika = [dict_color[odpowiedz_uzytkownika[i]] for i in range(len(odpowiedz_uzytkownika))]
    return odpowiedz_uzytkownika


#sprawdzenie poprawnosci inputu uzytkownika
"""!!! Wazne wstawic input uzytkownika skonwertowany funkcja Input_Conv !!!"""
def Is_Correct(odpowiedz_uzytkownika, szukany_kod): 
    """w sprint 2. zmienic sposob wyswietlania wyniku"""
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

    for symbol in feedback:
        if symbol == 'r':
            continue  # nie rysujemy i nie przesuwamy pozycji
        img = images.get(symbol)
        if img:
            window.blit(img, (current_x, y))
            current_x += img.get_width() + spacing


#------------------Koniec gry--------------------

#funkcja resetująca grę w razie porażki
UTTON_IMAGE_PATH = "red-7262301_1280.webp"

def show_result_screen(won=True):
    def restart_program():
        print("🔁 Restart programu...")
        root.destroy()
        show_result_screen(won=False)  # Możesz tu dać won=True jeśli chcesz

    root = tk.Tk()
    root.title("Wynik gry")
    root.geometry("600x400")
    root.configure(bg="white")

    # Komunikat
    message = "🎉 Gratulacje, wygrałeś!" if won else "❌ Przegrałeś! Spróbuj jeszcze raz."
    label = tk.Label(root, text=message, font=("Helvetica", 20), bg="white")
    label.pack(pady=40)

    # Załaduj obraz jako przycisk
    try:
        img = Image.open(BUTTON_IMAGE_PATH)
        img = img.resize((300, 100), Image.ANTIALIAS)
        button_image = ImageTk.PhotoImage(img)

        # Przycisk z obrazkiem
        button = tk.Button(root, image=button_image, command=restart_program, borderwidth=0, highlightthickness=0)
        button.image = button_image  # trzymamy referencję
        button.place(relx=0.5, rely=0.6, anchor="center")

        # Nakładany tekst (uwaga: nieklikalny — to tylko dekoracja!)
        btn_text = tk.Label(root, text="Spróbuj ponownie", font=("Helvetica", 14, "bold"), fg="white", bg="#e84118")
        btn_text.place(relx=0.5, rely=0.6, anchor="center")

    except Exception as e:
        print("❌ Błąd ładowania obrazu:", e)
        # Awaryjny przycisk tekstowy
        fallback_button = tk.Button(root, text="Spróbuj ponownie", font=("Helvetica", 14, "bold"),
                                    bg="#e84118", fg="white", command=restart_program)
        fallback_button.pack(pady=20)

#-----------------------------------------------------------------
#wyświetla ekran końcowy gry z komunikatem o wygranej lub przegranej
def show_end_screen(result: str):
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

    # Przycisk
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)

    running = True
    while running:
        screen.fill(bg)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    running = False

        # Tekst główny
        title_surface = font_big.render(title, True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(title_surface, title_rect)

        # Przycisk
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, DARK_GRAY if button_rect.collidepoint(mouse_pos) else GRAY, button_rect, border_radius=10)
        button_text = font_small.render("Spróbuj ponownie", True, BLACK)
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
