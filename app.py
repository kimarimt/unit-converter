import tkinter as tk


class App(tk.Tk):
    font = ('Arial', 16)

    def __init__(self):
        super().__init__()
        self.kilometers = tk.IntVar()
        self.miles_textfield = tk.Entry(width=8)
        self.miles_unit_label = tk.Label(text='Miles', font=self.font)
        self.is_equal_to_label = tk.Label(text='is equal to', font=self.font)
        self.kilometers_label = tk.Label(
            textvariable=self.kilometers, font=self.font)
        self.kilometers_unit_label = tk.Label(text='Km', font=self.font)
        self.calc_button = tk.Button(
            text="Calculate",
            font=self.font,
            command=self.calculate
        )

        self.title('Unit Converter')
        self.geometry('300x150')
        self.resizable(False, False)
        self.miles_textfield.place(x=120, y=25)
        self.miles_unit_label.place(x=205, y=25)
        self.is_equal_to_label.place(x=30, y=55)
        self.kilometers_label.place(x=155, y=55)
        self.kilometers_unit_label.place(x=212, y=55)
        self.calc_button.place(x=110, y=85)

    def calculate(self):
        miles = int(self.miles_textfield.get())
        result = round(miles / 1.60934)
        self.kilometers.set(result)
