
"""Робота 10: форма реєстрації через PACK.

Запуск:     python praktyka/10-maket/form_pack.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — pack")
vikno.geometry("440x320")

# Заголовок
zagolovok = tk.Label(vikno, text="Реєстрація", font=("Arial", 18, "bold"))
zagolovok.pack(pady=15)

# Ім'я
ryadok1 = tk.Frame(vikno)
ryadok1.pack(fill="x", padx=10, pady=5)

tk.Label(ryadok1, text="Імʼя", width=10, anchor="w").pack(side="left")
tk.Entry(ryadok1).pack(side="left", fill="x", expand=True)

# Пошта
ryadok2 = tk.Frame(vikno)
ryadok2.pack(fill="x", padx=10, pady=5)

tk.Label(ryadok2, text="Пошта", width=10, anchor="w").pack(side="left")
tk.Entry(ryadok2).pack(side="left", fill="x", expand=True)

# Телефон
ryadok3 = tk.Frame(vikno)
ryadok3.pack(fill="x", padx=10, pady=5)

tk.Label(ryadok3, text="Телефон", width=10, anchor="w").pack(side="left")
tk.Entry(ryadok3).pack(side="left", fill="x", expand=True)

# Пароль
ryadok4 = tk.Frame(vikno)
ryadok4.pack(fill="x", padx=10, pady=5)

tk.Label(ryadok4, text="Пароль", width=10, anchor="w").pack(side="left")
tk.Entry(ryadok4, show="•").pack(side="left", fill="x", expand=True)

# Прапорець згоди
zgoda = tk.BooleanVar()
tk.Checkbutton(
    vikno,
    text="Погоджуюсь з умовами",
    variable=zgoda
).pack(anchor="w", padx=10, pady=10)

# Кнопки внизу праворуч
knopky = tk.Frame(vikno)
knopky.pack(side="bottom", fill="x", padx=10, pady=15)

tk.Button(knopky, text="Зареєструватись").pack(side="right", padx=5)
tk.Button(knopky, text="Скасувати", command=vikno.destroy).pack(side="right", padx=5)

vikno.mainloop()
