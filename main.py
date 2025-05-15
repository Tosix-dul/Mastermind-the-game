import pygame
import tkinter.messagebox

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