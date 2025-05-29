#funjcja okna dialogowego; Poziom 1, Poziom 2, Poziom 3, Wyjdź, “Stwórz swój własny poziom”, Customizacja, Zasady gry
# #Definicje do przycisków
def start_poziom(nr):
    print(f"Uruchamiam poziom {nr}")
    root.destroy()
    run_game(poziom=nr)

def stworz_poziom():
    messagebox.showinfo("Stwórz poziom", "Tutaj możesz stworzyć swój własny poziom.")

def customizacja():
    messagebox.showinfo("Customizacja", "Opcje personalizacji gracza.")

def zasady_gry():
    messagebox.showinfo("Zasady gry", "Tutaj znajdują się zasady gry...")

def wyjdz():
    root.destroy()
    sys.exit()

# Główne okno tkinter
root = tkinter.Tk()
root.title("Mastermind")
root.geometry("300x400")

# Przyciski
tkinter.Button(root, text="Poziom 1", command=lambda: start_poziom(1), width=25).pack(pady=5)
tkinter.Button(root, text="Poziom 2", command=lambda: start_poziom(2), width=25).pack(pady=5)
tkinter.Button(root, text="Poziom 3", command=lambda: start_poziom(3), width=25).pack(pady=5)

tkinter.Button(root, text="Stwórz swój własny poziom", command=stworz_poziom, width=25).pack(pady=5)
tkinter.Button(root, text="Customizacja", command=customizacja, width=25).pack(pady=5)
tkinter.Button(root, text="Zasady gry", command=zasady_gry, width=25).pack(pady=5)
tkinter.Button(root, text="Wyjdź", command=wyjdz, width=25).pack(pady=10)

# Start GUI
root.mainloop()
