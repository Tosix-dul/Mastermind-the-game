import random
from tkinter import messagebox, font
import pygame

#pygame.init()
#running = True
#
#while running:
#    pass
#    window = pygame.display.set_mode((500, 500))
#    pygame.display.set_caption("Mastermind")
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

#funkcja losuje kod dla komputera w postaci listy 4 intów
def losuj_kod(liczba_kolorow,dlugosc=4):
    return [random.randint(1,liczba_kolorow) for _ in range(dlugosc)]

#kolor1 to tylko zmienna, która ma być zamieniona na kolor
slownik_kolorow ={
    1: "kolor1",
    2: "kolor2",
    3: "kolor3",
    4: "kolor4",
    5: "kolor5",
    6: "kolor6"
}

#funkcja zamienia liczby na kolory i wypisuje je w postaci czytelnej
def wypisz_kod(kod, slownik):
    czytelny_kod = [slownik[liczba] for liczba in kod]
    print("Kod:", " ".join(czytelny_kod))

#ograniczona_liczba_prob
# Po jej przekroczeniu bez zgadnięcia - komunikat o przegranej i wypisanie szukanego kodu
#to nie musi być w funkcji, można w samych ifach

def ograniczona_liczba_prob(limit_prob, szukany_kod, odpowiedz_uzytkownika, liczba_prob=0):
    if liczba_prob == limit_prob:
        if odpowiedz_uzytkownika != szukany_kod:
            text_surface = font.render(f"Kod: {szukany_kod}", True, WHITE)
            messagebox.showinfo("Przegrana")
    return

#konwersja inputu na string cyfr
def Input_Conv (odpowiedz_uzytkownika): #gotowe, do zmiany dopiero w sprincie 2.
    dict_color = {"Purple":1,"Blue":2,"Green":3,"Orange":4}
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

#okno wygranej
def winwindow(odpowiedz_uzytkownika, szukany_kod):
    if odpowiedz_uzytkownika != szukany_kod:
        win = True
        tkinter.messagebox.showinfo("WYGRANA")
        show_popup = False
        reset_game( )

# rysowanie poprzednich strzalow
def draw_circles (size_of_guess, n0_of_guesses, window):
    for i in range(n0_of_guesses):
        for j in range(size_of_guess):
            pygame.draw.circle(window, (211, 211, 211), (100 + 50 * j, 25 + 50 * i), 24, 1)

def draw_answer (button , odpowiedz_uzytkownika , row_counter, window):
    button.draw_as_answer(window,(100+50*(len(odpowiedz_uzytkownika)-1),25+50*row_counter))

def cancel_answer(window, odpowiedz_uzytkownika , row_counter):
    pygame.draw.circle(window,(0,0,0),(100 + 50 * (len(odpowiedz_uzytkownika)-1), 25 + 50 * row_counter),26)
    pygame.draw.circle(window, (211, 211, 211), (100 + 50 * (len(odpowiedz_uzytkownika)-1), 25 + 50 * row_counter), 24, 1)


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

def draw_button(window,image_path,size,place):
    drawing = pygame.transform.scale((pygame.image.load(image_path).convert_alpha()),size)
    window.blit(drawing,place)
    rect = drawing.get_rect(left=place[0], top=place[1])
    return rect

