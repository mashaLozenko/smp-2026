
"""Робота 10: форма реєстрації через GRID.

Запуск:     python praktyka/10-maket/form_grid.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — grid")
vikno.geometry("440x320")

# Налаштування стовпців і відступів
vikno.columnconfigure(1, weight=1)
vikno.rowconfigure(6, weight=1)

# Заголовок
zagolovok = tk.Label(vikno, text="Реєстрація", font=("Arial", 18, "bold"))
zagolovok.grid(row=0, column=0, columnspan=2, pady=15)

# Ім'я
tk.Label(vikno, text="Імʼя").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(vikno).grid(row=1, column=1, sticky="ew", padx=10, pady=5)

# Пошта
tk.Label(vikno, text="Пошта").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Entry(vikno).grid(row=2, column=1, sticky="ew", padx=10, pady=5)

# Телефон
tk.Label(vikno, text="Телефон").grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Entry(vikno).grid(row=3, column=1, sticky="ew", padx=10, pady=5)

# Пароль
tk.Label(vikno, text="Пароль").grid(row=4, column=0, sticky="w", padx=10, pady=5)
tk.Entry(vikno, show="•").grid(row=4, column=1, sticky="ew", padx=10, pady=5)

# Прапорець згоди
zgoda = tk.BooleanVar()
tk.Checkbutton(
    vikno,
    text="Погоджуюсь з умовами",
    variable=zgoda
).grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=10)

# Кнопки внизу праворуч
knopky = tk.Frame(vikno)
knopky.grid(row=7, column=0, columnspan=2, sticky="e", padx=10, pady=15)

tk.Button(knopky, text="Скасувати", command=vikno.destroy).pack(side="left", padx=5)
tk.Button(knopky, text="Зареєструватись").pack(side="left", padx=5)

vikno.mainloop()

