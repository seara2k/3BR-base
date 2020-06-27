import tkinter as tk
from tkinter import ttk, messagebox

# pylint: disable=C0103


class child_add(tk.Toplevel):

    def __init__(self, parent, fate):
        """
        Конструктор окна добавления элемента
        ----------
        Параметры:
                parent - класс родителя
                fate - функция, которую будет выполнять окно(либо добавление элемента, либо изменение)
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.row=""
        self.fate = fate
        self.parent = parent
        if self.fate == "add":
            self.title("Добавить элемент")
        elif self.fate == "change":
            self.title("Изменить элемент")
        elif self.fate == "filter":
            self.title("Выбрать фильтрацию")
        self.geometry(self.parent.cfg["Window sizes"]["add_element_window"])
        self.resizable(False, False)
        self.init_GUI()


    def init_GUI(self):
        """
        Конструктор интерфейса окна добавления элемента
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        # Фрейм окна
        adding_frame = tk.LabelFrame(self, text='Параметры')
        adding_frame.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)


        id_subframe = tk.Frame(adding_frame)
        id_subframe.pack(side=tk.TOP, fill=tk.X)

        id_label=tk.Label(id_subframe, text="Номер сотрудника")
        id_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Номер сотрудника"].tolist()))
            values.insert(0, "")
            self.id_combobox = ttk.Combobox(id_subframe, values=values)
            self.id_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.id_combobox.current(0)
        else:
            self.id_entry = ttk.Entry(id_subframe)
            self.id_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        full_name_subframe = tk.Frame(adding_frame)
        full_name_subframe.pack(side=tk.TOP, fill=tk.X)

        full_name_label=tk.Label(full_name_subframe, text="ФИО")
        full_name_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["ФИО"].tolist()))
            values.insert(0, "")
            self.full_name_combobox = ttk.Combobox(full_name_subframe, values=values)
            self.full_name_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.full_name_combobox.current(0)
        else:
            self.full_name_entry = ttk.Entry(full_name_subframe)
            self.full_name_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)            

        city_subframe = tk.Frame(adding_frame)
        city_subframe.pack(side=tk.TOP, fill=tk.X)

        city_label=tk.Label(city_subframe, text="Город")
        city_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Город"].tolist()))
            values.insert(0, "")
            self.city_combobox = ttk.Combobox(city_subframe, values=values)
            self.city_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.city_combobox.current(0)
        else:
            self.city_entry = ttk.Entry(city_subframe)
            self.city_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)   

        phone_number_subframe = tk.Frame(adding_frame)
        phone_number_subframe.pack(side=tk.TOP, fill=tk.X)

        phone_number_label=tk.Label(phone_number_subframe, text="Номер телефона")
        phone_number_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Номер телефона"].tolist()))
            values.insert(0, "")
            self.phone_number_combobox = ttk.Combobox(phone_number_subframe, values=values)
            self.phone_number_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.phone_number_combobox.current(0)
        else:
            self.phone_number_entry = ttk.Entry(phone_number_subframe)
            self.phone_number_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X) 

        speciality_subframe = tk.Frame(adding_frame)
        speciality_subframe.pack(side=tk.TOP, fill=tk.X)

        speciality_label=tk.Label(speciality_subframe, text="Специальность")
        speciality_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Специальность"].tolist()))
            values.insert(0, "")
            self.speciality_combobox = ttk.Combobox(speciality_subframe, values=values)
            self.speciality_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.speciality_combobox.current(0)
        else:
            self.speciality_entry = ttk.Entry(speciality_subframe)
            self.speciality_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X) 


        time_subframe = tk.Frame(adding_frame)
        time_subframe.pack(side=tk.TOP, fill=tk.X)

        time_label=tk.Label(time_subframe, text="Часы")
        time_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Часы"].tolist()))
            values.insert(0, "")
            self.time_combobox = ttk.Combobox(time_subframe, values=values)
            self.time_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.time_combobox.current(0)
        else:
            self.time_entry = ttk.Entry(time_subframe)
            self.time_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)


        pays_an_hour_subframe = tk.Frame(adding_frame)
        pays_an_hour_subframe.pack(side=tk.TOP, fill=tk.X)

        pays_an_hour_label=tk.Label(pays_an_hour_subframe, text="Зарплата в час")
        pays_an_hour_label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values=list(set(self.parent.database.dataframe_all["Зарплата в час"].tolist()))
            values.insert(0, "")
            self.pays_an_hour_combobox = ttk.Combobox(pays_an_hour_subframe, values=values)
            self.pays_an_hour_combobox.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.pays_an_hour_combobox.current(0)
        else:
            self.pays_an_hour_entry = ttk.Entry(pays_an_hour_subframe)
            self.pays_an_hour_entry.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        if self.parent.chosen_tree()=="tree_1":
            self.speciality_entry.config(state="disabled")
            self.time_entry.config(state="disabled")
            self.pays_an_hour_entry.config(state="disabled")
        elif self.parent.chosen_tree()=="tree_2":
            self.full_name_entry.config(state="disabled")         
            self.city_entry.config(state="disabled")   
            self.phone_number_entry.config(state="disabled")
            self.pays_an_hour_entry.config(state="disabled")
        elif self.parent.chosen_tree()=="tree_3":
            self.id_entry.config(state="disabled")
            self.full_name_entry.config(state="disabled")         
            self.phone_number_entry.config(state="disabled")
            self.time_entry.config(state="disabled")


        if self.fate == "change":
            tree = self.parent.chosen_tree()
            self.row = getattr(self.parent, tree).item(
                getattr(self.parent, tree).selection())["values"]

            if tree=="tree_1":
                self.id_entry.insert(0, self.row[0])
                self.full_name_entry.insert(0, self.row[1])
                self.city_entry.insert(0, self.row[2])
                self.phone_number_entry.insert(0, self.row[3])
            if tree=="tree_2":
                self.id_entry.insert(0, self.row[0])
                self.speciality_entry.insert(0, self.row[4])
                self.time_entry.insert(0, self.row[5])
            if tree=="tree_3":
                self.city_entry.insert(0, self.row[2])
                self.speciality_entry.insert(0, self.row[4])
                self.pays_an_hour_entry.insert(0, self.row[6])


        button_frame = tk.Frame(adding_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)
        clear_button = ttk.Button(
            button_frame, text="Очистить поля", command=self.clear)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5,
                       fill=tk.X, expand=1)
        start_button = ttk.Button(
            button_frame, text="Подтвердить", command=self.start)
        start_button.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)


    def start(self):
        if self.fate=="add":
            if self.parent.chosen_tree()=="tree_1" and self.check_input():
                self.parent.add([int(self.id_entry.get()),
                                 str(self.full_name_entry.get()),
                                 str(self.city_entry.get()),
                                 str(self.phone_number_entry.get())])

            if self.parent.chosen_tree()=="tree_2" and self.check_input():
                self.parent.add([int(self.id_entry.get()),
                                 str(self.speciality_entry.get()),
                                 int(self.time_entry.get())])

            if self.parent.chosen_tree()=="tree_3" and self.check_input():
                self.parent.add([str(self.city_entry.get()),
                                 str(self.speciality_entry.get()),
                                 int(self.pays_an_hour_entry.get())])

        elif self.fate == "change":
            if self.parent.chosen_tree()=="tree_1" and self.check_input():
                self.parent.change([int(self.id_entry.get()),
                                 str(self.full_name_entry.get()),
                                 str(self.city_entry.get()),
                                 str(self.phone_number_entry.get())])

            if self.parent.chosen_tree()=="tree_2" and self.check_input():
                self.parent.change([int(self.id_entry.get()),
                                 str(self.speciality_entry.get()),
                                 int(self.time_entry.get())])

            if self.parent.chosen_tree()=="tree_3" and self.check_input():
                self.parent.change([str(self.city_entry.get()),
                                 str(self.speciality_entry.get()),
                                 int(self.pays_an_hour_entry.get())])
            self.destroy()

        elif self.fate == "filter":
            self.parent.filtered_dataframe = self.parent.filter(self.id_entry.get(),
                                                    self.full_name_entry.get(),
                                                    self.city_entry.get(),
                                                    self.phone_number_entry.get(),
                                                    self.speciality_entry.get(),
                                                    self.time_entry.get(),
                                                    self.pays_an_hour_entry.get())

            self.parent.refresh_from_database(self.parent.filtered_dataframe)
            self.parent.filtered = 1
            self.destroy()

    def check_input(self):
        if self.parent.chosen_tree()=="tree_1":

            correct_output = ["int", "str", "str", "str"]
            input_array = [self.id_entry.get(),
                                 self.full_name_entry.get(),
                                 self.city_entry.get(),
                                 self.phone_number_entry.get()]

            if self.row ==input_array:
                return True
            output = []
            for item in input_array:
                try:
                    temp = int(item)
                    if item==self.phone_number_entry.get():
                        output.append("str")
                    else:
                        output.append("int")    
                except ValueError:
                    temp = str(item)
                    output.append("str")
            if correct_output != output or input_array.count("") != 0:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Ввод должен быть в формате:\nЧисло\nСтрока\nСтрока\nСтрока или число\nТакже недопускается пустой ввод.",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

            if self.parent.database.dataframe_1["Номер сотрудника"].tolist().count(int(self.id_entry.get())) >= 1:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Такой номер сотрудника уже есть",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

            if self.parent.database.dataframe_1["ФИО"].tolist().count(self.full_name_entry.get()) >= 1 and self.parent.database.dataframe_1["Город"].tolist().count(self.city_entry.get()) >= 1 and self.parent.database.dataframe_1["Номер телефона"].tolist().count(self.phone_number_entry.get()) >= 1:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Такая комбинация данных уже есть",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False
            

        if self.parent.chosen_tree()=="tree_2":

            correct_output = ["int", "str", "int"]
            input_array = [self.id_entry.get(),
                                 self.speciality_entry.get(),
                                 self.time_entry.get()]
            if self.row ==input_array:
                return True
            output = []
            for item in input_array:
                try:
                    temp = int(item)
                    output.append("int")
                except ValueError:
                    temp = str(item)
                    output.append("str")

            if correct_output != output or input_array.count("") != 0:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Ввод должен быть в формате:\nЧисло\nСтрока\nЧисло\nТакже недопускается пустой ввод.",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

            if self.parent.database.dataframe_2["Номер сотрудника"].tolist().count(int(self.id_entry.get())) >= 1:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Такой номер сотрудника уже есть",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

            if self.parent.database.dataframe_2["Специальность"].tolist().count(self.speciality_entry.get()) >= 1 and self.parent.database.dataframe_2["Часы"].tolist().count(int(self.time_entry.get())) >= 1:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Такая комбинация данных уже есть",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False


        if self.parent.chosen_tree()=="tree_3":


            correct_output = ["str", "str", "int"]
            input_array = [self.city_entry.get(),
                                 self.speciality_entry.get(),
                                 self.pays_an_hour_entry.get()]
            if self.row ==input_array:
                return True
            output = []
            for item in input_array:
                try:
                    temp = int(item)
                    output.append("int")
                except ValueError:
                    temp = str(item)
                    output.append("str")

            if correct_output != output or input_array.count("") != 0:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Ввод должен быть в формате:\nСтрока\nСтрока\nЧисло\nТакже недопускается пустой ввод.",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

            if self.parent.database.dataframe_3["Город"].tolist().count(self.city_entry.get()) >= 1 and self.parent.database.dataframe_3["Специальность"].tolist().count(self.speciality_entry.get()) >= 1 :
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Такая комбинация данных уже есть",
                    parent=self)
                self.grab_set()
                self.focus_set()
                return False

        return True






    # def go(self):
    #     """
    #     Начало работы окна, либо добавление либо изменение значений таблицы
    #     ----------
    #     Параметры: -
    #     ----------
    #     Возвращает: -
    #     ----------
    #     Автор: Литвинов В.С.
    #     """
    #     if self.fate == "add":
    #         if self.check_input():
    #             if self.parent.get_values("ID").count(self.entry_ID.get()) >= 1:
    #                 messagebox.showerror(
    #                     title="Ошибка ввода",
    #                     message="Такой номер сотрудника уже есть", parent=self)
    #                 self.grab_set()
    #                 self.focus_set()
    #             else:
    #                 self.parent.add([int(self.entry_ID.get()),
    #                                  str(self.entry_Full_Name.get(
    #                                  )),
    #                                  str(self.entry_City.get(
    #                                  )),
    #                                  str(self.entry_Phone_Number.get(
    #                                  )),
    #                                  str(self.entry_Speciality.get(
    #                                  )),
    #                                  int(self.entry_Time.get(
    #                                  )),
    #                                  int(self.entry_Pays_An_Hour.get())])
    #         else:
    #             messagebox.showerror(
    #                 title="Ошибка ввода",
    #                 message="Ввод должен быть в формате:\nЧисло\nСтрока\nСтрока\nСтрока или число\nСтрока\nЧисло\nЧисло\nТакже недопускается пустой ввод.",
    #                 parent=self)
    #             self.grab_set()
    #             self.focus_set()
    #     if self.fate == "change":
    #         if self.check_input():
    #             if (self.parent.get_values("ID").count(self.entry_ID.get()) >= 1) and (int(self.entry_ID.get()) != self.id_check):
    #                 messagebox.showerror(
    #                     title="Ошибка ввода",
    #                     message="Такой номер сотрудника уже есть", parent=self)
    #                 self.grab_set()
    #                 self.focus_set()
    #             else:
    #                 self.parent.change_row(self.row[0], [int(self.entry_ID.get()),
    #                                                      str(self.entry_Full_Name.get(
    #                                                      )),
    #                                                      str(self.entry_City.get(
    #                                                      )),
    #                                                      str(self.entry_Phone_Number.get(
    #                                                      )),
    #                                                      str(self.entry_Speciality.get(
    #                                                      )),
    #                                                      int(self.entry_Time.get(
    #                                                      )),
    #                                                      int(self.entry_Pays_An_Hour.get())])
    #                 self.destroy()
    #         else:
    #             messagebox.showerror(
    #                 title="Ошибка ввода",
    #                 message="Ввод должен быть в формате:\nчисло\nстрока\nстрока\nстрока или число\nстрока\nчисло\nчисло,\nТакже недопускается пустой ввод.",
    #                 parent=self)
    #             self.grab_set()
    #             self.focus_set()
    #         self.parent.eg_btn_edit.config(state="disabled")


    def clear(self):
        """
        Очиста значений, введённых в окно добавления элемента
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.fate == "filter":
            self.id_combobox.current(0)
            self.full_name_combobox.current(0)
            self.city_combobox.current(0)
            self.phone_number_combobox.current(0)
            self.speciality_combobox.current(0)
            self.time_combobox.current(0)
            self.pays_an_hour_combobox.current(0)
        else:
            self.id_entry.delete(0, tk.END)
            self.full_name_entry.delete(0, tk.END)
            self.phone_number_entry.delete(0, tk.END)
            self.city_entry.delete(0, tk.END)
            self.speciality_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.pays_an_hour_entry.delete(0, tk.END)
