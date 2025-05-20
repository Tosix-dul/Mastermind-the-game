import pygame
import tkinter.messagebox
import funkcje



#Okno gry
pygame.init()
running = True

#przykladowy przycisk; do usuniecia pozniej
b1 = funkcje.Circ_Pushbutton((255,0,0),(250,250),50)


window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mastermind")
while running:
    b1.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if b1.is_clicked(event):
            #tymczasowe
            print("Button!!!")
    pygame.display.update()
#Okno wygranej
    # if guess == answer:
    #    win = True
    #    tkinter.messagebox.showinfo("WYGRANA")