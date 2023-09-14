import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Рассчитать η")
        self.geometry("500x500")


        self.file1_button = tk.Button(self, text="Выбрать I(ti) файл", command=self.choose_file1)
        self.file2_button = tk.Button(self, text="Выбрать I0(ti) файл", command=self.choose_file2)
        self.delta_t0_label = tk.Label(self, text="Δt0:")
        self.delta_t0_entry = tk.Entry(self)
        self.delta_t_label = tk.Label(self, text="Δt:")
        self.delta_t_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Рассчитать η", command=self.calculate_eta)
        self.eta_label = tk.Label(self, text="η = ")
        self.graph_button = tk.Button(self, text="График", command=self.plot_graph)
        self.graph_button2 = tk.Button(self, text="График η-P", command=self.plot_eta_results)


        self.file1_button.pack(pady=10)
        self.file2_button.pack(pady=10)
        self.delta_t0_label.pack()
        self.delta_t0_entry.pack()
        self.delta_t_label.pack()
        self.delta_t_entry.pack()
        self.calculate_button.pack(pady=10)
        self.eta_label.pack(pady=10)
        self.graph_button.pack(pady=10)
        self.graph_button2.pack(pady=10)

        self.df1 = pd.DataFrame()
        self.df2 = pd.DataFrame()

        # Массивы
        self.t = []
        self.I = []
        self.I0 = []

    def choose_file1(self):
        file1 = filedialog.askopenfilename(title="Выбрать I(ti) файл", filetypes=[("Excel files", "*.xlsx")])
        self.df1 = pd.read_excel(file1)
        self.t = self.df1["CH1"].tolist()
        self.I = self.df1["CH2"].tolist()

    def choose_file2(self):
        file2 = filedialog.askopenfilename(title="Выбрать I0(ti) файл", filetypes=[("Excel files", "*.xlsx")])
        self.df2 = pd.read_excel(file2)
        self.I0 = self.df2["CH2"].tolist()

    def calculate_eta(self):
        delta_t0 = float(self.delta_t0_entry.get())
        delta_t = float(self.delta_t_entry.get())

        sum_i_squared = np.sum(np.array(self.I)**2 )
        sum_i0_squared = np.sum(np.array(self.I0)**2  )

        eta = 1 - (delta_t * sum_i_squared) / (delta_t0 * sum_i0_squared)

        self.eta_label.config(text=f"η = {eta}")

        with open("eta.txt", "a") as file:
            file.write(str(eta) + "\n")

    def plot_graph(self):
        plt.plot(self.t, self.I, label="I(ti)")
        plt.plot(self.t, self.I0, label="I0(ti)")
        plt.xlabel("t")
        plt.ylabel("I")
        plt.legend()
        plt.show()

    def save_eta_to_file(self, eta):
        with open("eta.txt", "a") as file:
            file.write("\n" + str(eta))

    def plot_eta_results(self):
        file_path = filedialog.askopenfilename(title="Выбрать файл с результатами eta", filetypes=[("Excel files", "*.xlsx")])
        df = pd.read_excel(file_path)
        P = df["P, Па"].tolist()
        eta = df["eta"].tolist()

        plt.plot(P, eta)
        plt.xlabel("P, Па")
        plt.ylabel("eta")
        plt.title("График η от P")
        plt.show()


app = App()
app.mainloop()
