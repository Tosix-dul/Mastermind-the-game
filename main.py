import pygame
import tkinter.messagebox


#konwersja inputu na string cyfr
def Input_Conv (answer = []): #gotowe, do zmiany dopiero w sprincie 2.
    len = 4
    dict_color = {"kolor1":"1","kolor2":"2","kolor3":"3","kolor4":"4"}
    answer = [str(input(f"Wpisz {i + 1}. kolor: ")) for i in range(len)] #tymczasowe, potem bedzie podawane jako parametr funkcji
    answer = [dict_color[answer[i]] for i in range(len(answer))]
    return answer


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