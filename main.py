import pygame
import tkinter.messagebox


#konwersja inputu na string cyfr
def Input_Conv (answer = []): #gotowe, do zmiany dopiero w sprincie 2.
    len = 4
    dict_color = {"kolor1":"1","kolor2":"2","kolor3":"3","kolor4":"4"}
    answer = [str(input(f"Wpisz {i + 1}. kolor: ")) for i in range(len)] #tymczasowe, potem bedzie podawane jako parametr funkcji
    answer = [dict_color[answer[i]] for i in range(len(answer))]
    return answer

def Is_Correct (conv_answer,solution): #niegotowe
    corr = ['r' for i in range(len(conv_answer))]
    mem = [i for i in range(len(conv_answer))]
    solution_cpy = solution.copy()
    # sprawdzenie dobrych kolorow
    for i in range(len(conv_answer)):
        if solution[i] == conv_answer[i]:
            corr[i] = 'g'
            mem.remove(i)
            solution_cpy.remove(ex[i])
    return corr



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