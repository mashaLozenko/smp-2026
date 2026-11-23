
import tkinter as tk

vikno = tk.Tk()
vikno.title("Калькулятор")

tk.Label(vikno, text="Перше:").grid(row=0, column=0, sticky="e", padx=8, pady=4)
pole_a = tk.Entry(vikno, width=14)
pole_a.grid(row=0, column=1, padx=8)

tk.Label(vikno, text="Друге:").grid(row=1, column=0, sticky="e", padx=8, pady=4)
pole_b = tk.Entry(vikno, width=14)
pole_b.grid(row=1, column=1, padx=8)

operatsiia = tk.StringVar(value="+")
ramka = tk.Frame(vikno)
ramka.grid(row=2, column=0, columnspan=2)

for znak in ("+", "−", "×", "÷"):
    tk.Radiobutton(ramka, text=znak, variable=operatsiia, value=znak).pack(side="left", padx=4)

tekst_rezultatu = tk.StringVar(value="—")
rezultat = tk.Label(
    vikno,
    textvariable=tekst_rezultatu,
    font=("Segoe UI", 16, "bold")
)
rezultat.grid(row=4, column=0, columnspan=2, pady=6)


def porakhuvaty(podiia=None):
    try:
        a = float(pole_a.get())
        b = float(pole_b.get())

        znak = operatsiia.get()

        if znak == "+":
            vidpovid = a + b
        elif znak == "−":
            vidpovid = a - b
        elif znak == "×":
            vidpovid = a * b
        elif znak == "÷":
            if b == 0:
                tekst_rezultatu.set("Помилка: ділення на нуль")
                return
            vidpovid = a / b

        tekst_rezultatu.set(f"Результат: {vidpovid:g}")

    except ValueError:
        tekst_rezultatu.set("Помилка: введіть два числа")


def ochystyty(podiia=None):
    pole_a.delete(0, tk.END)
    pole_b.delete(0, tk.END)
    tekst_rezultatu.set("—")


tk.Button(
    vikno,
    text="Порахувати",
    command=porakhuvaty
).grid(row=3, column=0, columnspan=2, pady=4)

pole_a.bind("<Return>", porakhuvaty)
pole_b.bind("<Return>", porakhuvaty)
vikno.bind("<Escape>", ochystyty)

vikno.mainloop()
