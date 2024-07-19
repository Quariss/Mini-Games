from games import rock_paper_scissors, number_guessing, tic_tac_toe, hangman
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Küçük Oyunlar")

    def start_rock_paper_scissors():
        rock_paper_scissors()

    def start_number_guessing():
        number_guessing()

    def start_hangman():
        hangman()

    def start_tic_tac_toe():
        tic_tac_toe()

    tk.Label(root, text="Oynamak istediğiniz oyunu seçin.").pack()

    tk.Button(root, text="Taş-Kağıt-Makas", command=start_rock_paper_scissors).pack()
    tk.Button(root, text="Sayı-Tahmin", command=start_number_guessing).pack()
    tk.Button(root, text="Adam Asmaca", command=start_hangman).pack()
    tk.Button(root, text="XOX", command=start_tic_tac_toe).pack()


    tk.Button(root, text="Çıkış", command=root.quit).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
