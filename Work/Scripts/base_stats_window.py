import tkinter as tk
from tkinter import ttk
import list_processing as lp

# pylint: disable=C0103


class base_stats_window(tk.Toplevel):

    def __init__(self, parent, column_names_ru):
        """
        Конструктор окна вывода базовой статистики
        ----------
        Параметры:
                parent - класс родителя
                column_names_ru - названия колонок на русском языке
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.column_names_ru = column_names_ru
        self.parent = parent
        self.title("Базовая статистика")
        self.geometry(self.parent.cfg["Window sizes"]["base_stats_window"])
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        # Меню
        mainmenu = tk.Menu(self)
        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Экспорт в excel", command=lambda:self.parent.give_excel(self.dataframe,False))
        mainmenu.add_cascade(label="Экспорт", menu=filemenu)
        self.config(menu=mainmenu)
        # Фрейм окна
        base_stats_window = tk.LabelFrame(
            self, text="Параметры")
        base_stats_window.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Размер, ширина колонок и таблица
        number_of_columns = len(self.column_names_ru)
        self.width = lp.good_looking_columns(number_of_columns)
        self.column_names_eng = [lp.translate_to_eng(
            self.column_names_ru[x]) for x in range(number_of_columns)]
        self.tree = ttk.Treeview(
            base_stats_window, columns=self.column_names_eng, height=20, show="headings")
        for i in range(len(self.column_names_eng)):
            self.tree.column(self.column_names_eng[i],
                             width=self.width, anchor=tk.CENTER)
            self.tree.heading(self.column_names_eng[i], text=self.column_names_ru[i])

        tree_scrollbar_vertical = tk.Scrollbar(
            base_stats_window, orient="vertical", command=self.tree.yview)
        tree_scrollbar_vertical.pack(side=tk.RIGHT, fill="y")

        tree_scrollbar_horizontal = tk.Scrollbar(
            base_stats_window, orient="horizontal", command=self.tree.xview)
        tree_scrollbar_horizontal.pack(side=tk.BOTTOM, fill="x")

        self.tree.pack(pady=5)
        self.clever_insert_values()
        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def clever_insert_values(self):
        """
        Вставка данных в таблицу базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        self.column_names_eng.remove("properties")
        self.column_names_ru.remove("Свойства")
        if self.parent.filtered == 0:
            self.dataframe=lp.base_stats(self.parent.database.dataframe_all, self.column_names_ru)
        else:
            self.dataframe=lp.base_stats(self.parent.filtered_database.dataframe_all, self.column_names_ru)
        
        for i in range(len(self.dataframe.index)):
            row = sum(self.dataframe.iloc[[i]].values.tolist(), [])
            self.tree.insert("", "end", values=row)
