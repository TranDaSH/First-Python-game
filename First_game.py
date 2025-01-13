import tkinter as tk
from tkinter import messagebox
import random


# Функция для игры "Камень, Ножницы, Бумага"
def rock_paper_scissors():
    def play():
        items = ['Камень', 'Ножницы', 'Бумага']
        computer_choice = random.choice(items)
        player_choice = player_var.get()

        result_text = f"Компьютер выбрал: {computer_choice}\nВы выбрали: {player_choice}\n\n"

        if computer_choice == player_choice:
            result_text += "Ничья!"
        elif (computer_choice == 'Камень' and player_choice == 'Ножницы') or \
             (computer_choice == 'Ножницы' and player_choice == 'Бумага') or \
             (computer_choice == 'Бумага' and player_choice == 'Камень'):
            result_text += "Компьютер победил!"
        else:
            result_text += "Вы победили!"

        messagebox.showinfo("Результат", result_text)

    # Окно для игры
    rps_window = tk.Toplevel()
    rps_window.title("Камень, Ножницы, Бумага")
    rps_window.geometry("300x200")

    tk.Label(rps_window, text="Выбери фигуру:").pack(pady=10)

    player_var = tk.StringVar(value="Камень")
    for item in ['Камень', 'Ножницы', 'Бумага']:
        tk.Radiobutton(rps_window, text=item, variable=player_var, value=item).pack()

    tk.Button(rps_window, text="Играть", command=play).pack(pady=20)


# Функция для игры "Угадай число"
def guess_the_number():
    def check_guess():
        nonlocal attempts, hints_remaining, hints_finished
        try:
            player_choice = int(guess_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число.")
            return

        attempts += 1
        attempts_label.config(text=f"Попытки: {attempts}")

        if player_choice == random_number:
            messagebox.showinfo("Победа!", f"Поздравляю! Ты угадал число c {attempts} попытки.")
            guess_window.destroy()
        else:
            result_text = "К сожалению, ты не угадал число, попробуй еще разок!"
            if hints_remaining > 0:
                hint = messagebox.askyesno("Подсказка", "Хочешь воспользоваться подсказкой?")
                if hint:
                    if player_choice > random_number:
                        result_text += "\nЧисло, которое загадал компьютер, меньше твоего!"
                    else:
                        result_text += "\nЧисло, которое загадал компьютер, больше твоего!"
                    hints_remaining -= 1
            elif not hints_finished:
                result_text += "\nВсе подсказки закончились, дальше придется угадывать самому."
                hints_finished = True

            messagebox.showinfo("Результат", result_text)

    # Окно для игры
    guess_window = tk.Toplevel()
    guess_window.title("Угадай число")
    guess_window.geometry("300x200")

    random_number = random.randint(1, 100)
    attempts = 0
    hints_remaining = 3
    hints_finished = False

    tk.Label(guess_window, text="Угадай число от 1 до 100:").pack(pady=10)

    guess_entry = tk.Entry(guess_window)
    guess_entry.pack(pady=10)

    attempts_label = tk.Label(guess_window, text="Попытки: 0")
    attempts_label.pack(pady=10)

    tk.Button(guess_window, text="Проверить", command=check_guess).pack(pady=20)


# Главное меню
def main_menu():
    root = tk.Tk()
    root.title("Главное меню")
    root.geometry("300x200")

    tk.Label(root, text="Выберите игру:").pack(pady=20)

    tk.Button(root, text="Камень, Ножницы, Бумага", command=rock_paper_scissors).pack(pady=10)
    tk.Button(root, text="Угадай число", command=guess_the_number).pack(pady=10)
    tk.Button(root, text="Выход", command=root.quit).pack(pady=10)

    root.mainloop()


# Запуск программы
main_menu()
