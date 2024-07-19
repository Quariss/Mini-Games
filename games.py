import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from unittest import result


def rock_paper_scissors():
    choices = ['taş', 'kağıt', 'makas']
    user_score = 0
    computer_score = 0

    game_window = tk.Toplevel()
    game_window.title('Taş-Kağıt-Makas')

    def play_game(user_choice):
        nonlocal user_score, computer_score
        computer_choice = random.choice(choices)
        result = ""

        if user_choice == computer_choice:
            result = 'Berabere!'

        elif (user_choice == "taş" and computer_choice == "makas") or \
                (user_choice == "makas" and computer_choice == "kağıt") or \
                (user_choice == "kağıt" and computer_choice == "taş"):
            result = "Kazandınız!"
            user_score += 1

        else:
            result = "Kaybettiniz!"
            computer_score += 1

        messagebox.showinfo("Sonuç",
                            f"Bilgisayarın seçimi: {computer_choice}\n{result}\n\nSkor: Siz {user_score}, Bilgisayar: {computer_score}")

    tk.Label(game_window, text="Seçiminizi yapın.").pack()

    for choice in choices:
        tk.Button(game_window, text=choice, command=lambda c=choice: play_game(c)).pack()

    tk.Button(game_window, text="Çıkış", command=game_window.destroy).pack()


def number_guessing():
    number = random.randint(1, 100)
    attempts = 0

    game_window = tk.Toplevel()
    game_window.title("Sayı Tahmin Oyunu")

    def check_guess():
        nonlocal attempts
        guess = entry.get()
        if guess.isdigit():
            guess = int(guess)
        else:
            messagebox.showerror("Hata", "Lütfen bir sayı giriniz")
            return

        attempts += 1

        if guess < number:
            result.set("Tuttuğum sayı daha büyük")

        elif guess > number:
            result.set("Tuttuğum sayı daha küçük")

        else:
            messagebox.showinfo("Tebrikler", f"{attempts} denemede doğru tahmin ettiniz.")
            game_window.destroy()

    result = tk.StringVar()
    result.set("1 ile 100 arasında sayı tuttum, tahmin edin!")

    tk.Label(game_window, textvariable=result).pack()

    entry = tk.Entry(game_window)
    entry.pack()

    tk.Button(game_window, text="Tahmin et", command=check_guess).pack()
    tk.Button(game_window, text="Çıkış", command=game_window.destroy).pack()


def hangman():
    words_tr = {
        'Kolay': ["python", "tkinter", "programlama", "bilgisayar", "oyun"],
        'Orta': ["internet", "yazılım", "donanım", "teknoloji", "veritabanı"],
        'Zor': ["siber", "mühendislik", "değerlendirme", "dijitalleştirme", "kriptografi", ]
    }
    words_en = {
        'Easy': ["python", "tkinter", "programming", "computer", "game"],
        'Medium': ["internet", "software", "hardware", "technology", "database"],
        'Hard': ["Cyber", "engineering", "assessment", "digitization", "cryptography"]
    }
    words = {}
    word = []
    attempts = 6

    def start_game(language):
        nonlocal words, word
        if language == 'tr':
            words = words_tr
            difficulties = ["Kolay", "Orta", "Zor"]
        elif language == 'en':
            words = words_en
            difficulties = ["Easy", "Medium", "Hard"]
        select_difficulty(difficulties)

    def select_difficulty(difficulties):
        difficulty_window = tk.Toplevel()
        difficulty_window.title("Zorluk Seçimi")

        tk.Label(difficulty_window, text="Lütfen zorluk seviyesini seçin").pack()
        for difficulty in difficulties:
            tk.Button(difficulty_window, text=difficulty,
                      command=lambda d=difficulty: start_game_with_difficulty(d, difficulty_window)).pack()

    def start_game_with_difficulty(difficulty, window):
        nonlocal word, attempts
        word = random.choice(words[difficulty])
        attempts = 10 if difficulty == "Kolay" or difficulty == "Easy" else 6 if difficulty == "Orta" or difficulty == "Medium" else 4
        attempts_display.set(f"Kalan deneme hakkınız {attempts}")
        window.destroy()
        game_window.deiconify()
        update_word_display()

    language_selection_window = tk.Toplevel()
    language_selection_window.title("Dil Seçimi")

    tk.Label(language_selection_window, text="Lütfen dili seçin").pack()
    tk.Button(language_selection_window, text="Türkçe", command=lambda: start_game('tr')).pack()
    tk.Button(language_selection_window, text="English", command=lambda: start_game('en')).pack()

    game_window = tk.Toplevel()
    game_window.withdraw()
    game_window.title("Adam Asmaca")

    guess_letters = []

    def update_word_display():
        display_word.set(' '.join([letter if letter in guess_letters else '_' for letter in word]))

    def update_guess_letters_display():
        guess_letters_display.set(' '.join(guess_letters))

    def guess():
        nonlocal attempts
        guess = entry.get().lower()
        entry.delete(0, tk.END)

        if len(guess) == 1:
            if guess in guess_letters:
                messagebox.showwarning("Uyarı", "Bu harfi zaten tahmin ettiniz.")
            elif guess in word:
                guess_letters.append(guess)
                update_word_display()
                # update_guess_letters_display()
                if all(letter in guess_letters for letter in word):
                    messagebox.showinfo("Tebrikler", "Kelimeyi buldunuz")
                    game_window.destroy()

            else:
                attempts -= 1
                guess_letters.append(guess)
                update_guess_letters_display()
                attempts_display.set(f"Kalan deneme hakkınız {attempts}")
                if attempts == 0:
                    messagebox.showinfo("Kaybettiniz", f"Kelime : {word}")
                    game_window.destroy()

        else:
            if guess == word:
                messagebox.showinfo("Tebrikler", "Kelimeyi buldunuz.")
                game_window.destroy()
            else:
                messagebox.showinfo("Yanlış Tahmin", "Yanlış tahmin tekrar deneyin.")
                attempts -= 1
                attempts_display.set(f"Kalan deneme {attempts}")
                if attempts == 0:
                    messagebox.showinfo("Kaybettiniz", f"Kelime : {word}")
                    game_window.destroy()

    display_word = tk.StringVar()
    update_word_display()
    attempts_display = tk.StringVar()
    attempts_display.set(f"Kalan deneme hakkınız {attempts}")
    guess_letters_display = tk.StringVar()
    guess_letters_display.set('')

    tk.Label(game_window, textvariable=display_word).pack()
    tk.Label(game_window, textvariable=attempts_display).pack()
    tk.Label(game_window, text="Tahmin Edilen Harfler:").pack()
    tk.Label(game_window, textvariable=guess_letters_display).pack()

    entry = tk.Entry(game_window)
    entry.pack()

    tk.Button(game_window, text="Tahmin Et", command=guess).pack()
    tk.Button(game_window, text="Çıkış", command=game_window.destroy).pack()


def tic_tac_toe():
    game_window = tk.Toplevel()
    game_window.title("Tic-Tac-Toe")

    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_mode = None

    def check_winner():
        for i in range(3):
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
                return board[i * 3]
            if board[i] == board[i + 3] == board[i + 6] != ' ':
                return board[i]
        if board[0] == board[4] == board[8] != ' ':
            return board[0]
        if board[2] == board[4] == board[6] != ' ':
            return board[2]

        if ' ' not in board:
            return 'D'
        return None

    def computer_move():
        empty_cell = [i for i, cell in enumerate(board) if cell == ' ']
        if empty_cell:
            idx = random.choice(empty_cell)
            make_move(idx, is_computer=True)

    def make_move(idx, is_computer=False):
        nonlocal current_player
        if board[idx] == ' ':
            board[idx] = current_player
            buttons[idx].config(text=current_player)
            winner = check_winner()
            if winner:
                if winner == 'D':
                    messagebox.showinfo("Berabere", "Oyun berabere bitti.")
                else:
                    messagebox.showinfo("Kazanan", f"{winner} kazandı")
                game_window.destroy()

            else:
                current_player = 'O' if current_player == 'X' else 'X'
                if game_mode == 'single' and not is_computer and current_player == 'O':
                    computer_move()

    def start_game(mode):
        nonlocal game_mode
        game_mode = mode
        for widget in game_window.winfo_children():
            widget.destroy()
        draw_board()

    def draw_board():
        nonlocal buttons
        buttons = []
        for i in range(9):
            button = tk.Button(game_window, text=' ', font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: make_move(i))
            button.grid(row=i // 3, column=i % 3)
            buttons.append(button)
        tk.Button(game_window, text='Çıkış', command=game_window.destroy).grid(row=3, column=3)

    tk.Label(game_window, text='Oyun Modunu Seçin:').pack()
    tk.Button(game_window, text='Tek Oyunculu', command=lambda: start_game('single')).pack()
    tk.Button(game_window, text='Çift Oyunculu', command=lambda: start_game('duo')).pack()

    buttons = []
