
"""Робота 10: форма реєстрації через PLACE.

Запуск:     python praktyka/10-maket/form_place.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — place")
vikno.geometry("380x300")

# Заголовок
zagolovok = tk.Label(vikno, text="Реєстрація", font=("Arial", 18, "bold"))
zagolovok.place(x=120, y=15)

# Ім'я
tk.Label(vikno, text="Імʼя").place(x=20, y=65)
tk.Entry(vikno).place(x=110, y=65, width=240)

# Пошта
tk.Label(vikno, text="Пошта").place(x=20, y=100)
tk.Entry(vikno).place(x=110, y=100, width=240)

# Телефон
tk.Label(vikno, text="Телефон").place(x=20, y=135)
tk.Entry(vikno).place(x=110, y=135, width=240)

# Пароль
tk.Label(vikno, text="Пароль").place(x=20, y=170)
tk.Entry(vikno, show="•").place(x=110, y=170, width=240)

# Прапорець згоди
zgoda = tk.BooleanVar()
tk.Checkbutton(
    vikno,
    text="Погоджуюсь з умовами",
    variable=zgoda
).place(x=20, y=205)

# Кнопки внизу праворуч
tk.Button(vikno, text="Скасувати").place(x=120, y=255, width=100)
tk.Button(vikno, text="Зареєструватись").place(x=230, y=255, width=130)

vikno.mainloop()
