import tkinter as tk
from tkinter import ttk
import graph_lib
# import numpy as np
# import pandas as pd
# pylint: disable=C0103


class child_box_visk(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_GUI()
        self.view = app

    def init_GUI(self):
        self.title("Анализ")
        self.geometry('340x135')
        self.resizable(False, False)

        # Фрейм окна
        summary_table_group = tk.LabelFrame(
            self, text='Диаграмма Бокса-Вискера')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_group = tk.Frame(summary_table_group)
        kach_col_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col = tk.Label(kach_col_group, text="Качественный столбец")
        lbl_kach_col.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col = ttk.Combobox(kach_col_group, values=["Номер сотрудника", "ФИО", "Город",
                                                                "Номер телефона", "Специальность",
                                                                "Часы", "Зарплата в час"])
        self.cb_kach_col.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col.current(0)

        numeral_group = tk.Frame(summary_table_group)
        numeral_group.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral = tk.Label(numeral_group, text="Численный столбец")
        lbl_numeral.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_numeral = ttk.Combobox(numeral_group, values=["Номер сотрудника", "ФИО", "Город",
                                                              "Номер телефона", "Специальность",
                                                              "Часы", "Зарплата в час"])
        self.cb_numeral.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_numeral.current(0)

        btn_start = ttk.Button(
            summary_table_group, text='Начать анализ', command=self.box_visk_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def box_visk_analyze(self):
        column_name_1_ru = self.cb_kach_col.get()
        column_name_2_ru = self.cb_numeral.get()
        column_name_1_eng = graph_lib.translate_to_eng(column_name_1_ru)
        column_name_2_eng = graph_lib.translate_to_eng(column_name_2_ru)
        var_1 = self.view.get_values(column_name_1_eng)
        var_2 = self.view.get_values(column_name_2_eng)
        graph_lib.box_whiskers(column_name_1_ru, column_name_2_ru, var_2)

if __name__ == "__main__":
    pass
