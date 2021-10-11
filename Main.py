import tkinter.messagebox as m
import tkinter as t


def fixer(arr):
    for i in range(len(arr)):
        if int(arr[i]) == arr[i]:
            arr[i] = int(arr[i])
def fixar(var):
    if int(var) == var:
        return int(var)
    else:
        return var
def positive_medium(self, array):
    fixer(array)
    array = list(filter(lambda f: f > 0, array))
    return sum(array)/len(array) if array else 0

def del_all_by_name(array, todelete):
    fixer(array)
    return list(map(lambda z: int(z) if z%1 == 0 else z, filter(lambda x: x != todelete, array)))

def sticker(array1, array2):
    fixer(array1)
    fixer(array2)
    new_array = []
    for x, y in zip(array1, array2):
        new_array.append(x)
        new_array.append(y)
    return new_array

def to_n_further(array, key, n):
    fixer(array)
    key = fixar(key)
    if key not in array:
        print("Такого элемента нет")
        return
    if array.index(key) + n >= len(array):
        array.remove(key)
        array.append(key)
    else:
        temp = array.index(key)
        array = array[:temp] + array[temp + 1:temp + 1 + n] + [key] + array[temp + 1 + n:]
    return array

def copy_part(begin, amount, array):
    fixer(array)
    return array[begin: begin + amount]

def reverse(array):
    fixer(array)
    return array[-1::-1]

def common(array1, array2):
    fixer(array1)
    fixer(array2)
    return list(set([i for i in array1 if i in array2]))

def swap(array, first, second):
    fixer(array)
    array[first - 1], array[second - 1] = array[second - 1], array[first - 1]
    return array

def compareList(array1, array2):
    fixer(array1)
    fixer(array2)
    for x, y in zip(array1, array2):
        if x != y:
            return "Списки не равны"
    return "Списки равны"

def every_second_item(array):
    fixer(array)
    return array[1::2]

def gr_eq_sm(array, key):
    key = fixar(key)
    fixer(array)
    greater = 0
    equal = 0
    smaller = 0
    for i in array:
        if i > key:
            greater += 1
        elif i < key:
            smaller += 1
        else:
            equal += 1
    return "Больше:%s; \tМеньше:%s; \nРавные:%s"%(greater, smaller, equal)

def move_n_backwards(array, k, n):
    fixer(array)
    temp = array[k - 1]
    array.remove(temp)
    return array[:k - n - 1] + [temp] + array[k - n - 1:]

def range_sep(array, r):
    fixer(array)
    arr1 = [i for i in array if i in r]
    arr2 = [i for i in array if i not in r]
    
    return "Попадают в диапазон: %s,\nНе попадают: %s"%(" ".join(list(map(str, arr1))), " ".join(list(map(str, arr2))))

def Uniqum(array):
    fixer(array)
    return list(set(array))

def mirror_repeat(array):
    fixer(array)
    for i in reversed(array):
        array.append(i)
    return array

class Handler(object):
    win_name = "1 Вариант"
    tbox1 = "Вычислить среднее арифметическое положительных элементов непустого списка."
    tbox2 = ""
    example = "1 0 5 4 -5 25.5"
    error_enter = "Неверный формат ввода данных. Вводить можно только целые и дробные числа через пробел. См. пример."
    handling_func = positive_medium
    win_x, win_y = 650, 350
    win_height, win_width  = 300, 500
    example_x, example_y = 375, 125
    termbox_x, termbox_y =  100, 3
    res_label_x, res_label_y = 5, 185
    get_res_x, get_res_y = 115, 175
    resbox_x, resbox_y = 5, 225
    enter_label_text = "Введите элементы списка через пробел:"
    enter_x, enter_y, enter_length = 5, 145, 32
    enter, resbox, termbox = 0, 0, 0
    add = 0
    stop = False
    
    def __init__(self, win_name):
        self.win_name = win_name
    def start(self):
        #self.add = t.Tk()
        self.add.title(self.win_name)
        self.add["bg"] = "light goldenrod yellow"
        self.add.geometry("%sx%s+%s+%s"%(self.win_width, self.win_height, self.win_x, self.win_y))
        self.add.resizable(width = False, height = False)
        
        t.Label(self.add, text = "Формулировка задания", font = ("New Times Roman", 20, "bold"), bg = "light goldenrod yellow").pack()
        self.termbox = t.Text(self.add, width = self.termbox_x, height = self.termbox_y, bg = "light goldenrod yellow", wrap = "word", bd = 3)
        self.termbox.insert(1.0, self.tbox1)
        self.termbox.config(font = ("New Times Roman", 14, "italic"), relief = "flat")
        self.termbox.bind('<KeyRelease>', self.__still)
        self.termbox.bind('<KeyPress>', self.__still)
        self.termbox.pack()

        t.Label(self.add, text = self.enter_label_text, font = ("New Times Roman", 14), bg = "light goldenrod yellow").pack(anchor = "w")

        rdata = ""
        self.enter =  t.Entry(self.add, font = ("New Times Roman", 14), width = self.enter_length)
        self.enter.place(x = self.enter_x, y = self.enter_y)

        example = t.Button(self.add, text = "Пример", font = ("New Times Roman", 14, "bold"), command = self.__but_example)
        example.place(x = self.example_x, y = self.example_y)
        t.Label(self.add, text = "Результат:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = self.res_label_x, y = self.res_label_y)

        get_res = t.Button(self.add, text = "Получить результат", font = ("New Times Roman", 14, "bold"), command = self.fetch_data)
        get_res.place(x = self.get_res_x, y = self.get_res_y)

        self.resbox = t.Text(self.add, width = 44, height = 2, bg = "floral white", wrap = "word", bd = 3)
        self.resbox.config(font = ("New Times Roman", 14, "italic"), relief = "ridge")
        self.stable_resbox()
        self.resbox.place(x = self.resbox_x, y = self.resbox_y)
        self.add.bind("<KeyRelease>", self.key_handler)
        self.add.mainloop()

    def key_handler(self, e):
        if self.stop:
            return
        if e.keycode == 27:
            self.single_window()
        elif e.keycode == 13:
            self.fetch_data()
        #print(e)
    def __but_example(self):
        l_text = self.example
        main.unbind('<Configure>')
        m.showinfo("Пример", l_text)
        self.add.attributes("-topmost", True)
        self.add.attributes("-topmost", False)
        main.bind('<Configure>', stable_pos)
            
    def fetch_data(self):
        
        rdata = self.enter.get()
        try:
            data = list(map(lambda z: float(z) if z.count(".") else int(z), rdata.split()))
            if not data:
                self.call_error("Список пустой")
                return
            
            self.tbox2 = self.handling_func(data)
            self.stable_resbox()

            
        except ValueError:
            self.call_error(self.error_enter)
    
    def __still(self, e):
        if e.keycode in (17, 67):
            return
        if self.termbox.get(1.0, "end") != self.tbox1:
            self.termbox.delete(1.0, "end")
            self.termbox.insert(1.0, self.tbox1)
    
    def stillres(self, e):
        if e.keycode in (17, 67):
            return
        
        if self.resbox.get(1.0, "end") != self.tbox2:
            self.resbox.delete(1.0, "end")
            self.resbox.insert(1.0, self.tbox2)
    def single_window(self):
        try:
            self.add.destroy()
            self.add = 0
        except:
            pass
    def call_error(self, text):
            l_text = text
            main.unbind('<Configure>')
            self.stop = True
            m.showerror("Ошибка", l_text)
            self.add.attributes("-topmost", True)
            self.add.attributes("-topmost", False)
            main.bind('<Configure>', stable_pos)
            self.stop = False

    def stable_resbox(self):
        self.resbox.delete(1.0, "end")
        self.resbox.insert(1.0, self.tbox2)
        self.resbox.bind('<KeyRelease>', self.stillres)
        self.resbox.bind('<KeyPress>', self.stillres)        
#----

hand = 0
def but_1():
    global hand
    if hand:
        hand.single_window()
        
    hand = Handler("1 вариант")
    hand.add = t.Tk()
    hand.start()
    
def but_2():#2 вариант
    def fetch_data(): #сбор и обработка данных с кнопки "Получить результат"
        global hand
        rlist = hand.enter.get().split() #Получение данных с строки ввода списка
        ritem = enter2.get().replace(" ", "")#Получение данных с строки ввода значения
        try:
            if not rlist or not ritem:#Обработка случая, если какие-то данные не введены
                hand.call_error("Список пустой или значение не задано.")#вызов окна с ошибкой
                return
        
            data = list(map(float, rlist))#Преобразование строки в список
            key =  float(ritem)            
            hand.tbox2 = hand.handling_func(data, key)#Вызов обрабатывающей функции и получение ответа
            hand.stable_resbox()#Вывод ответа и поддержание неизменяемости многострочного текстового поля
        except ValueError:
            print("!")
            hand.call_error(hand.error_enter)#вызов окна с ошибкой при вводе посторонних символов
    
    global hand
    if hand: #Если доп. окно уже существует(не обязательно именно этого варианта), оно удаляется
        hand.single_window()

    #Кастомизация 
    hand = Handler("2 вариант") #Создание экзмепляра класса + название окна
    hand.tbox1 = "Требуется просмотреть список и удалить элементы, у которых информационные поля равны некоторому заданному значению."#Задание
    hand.example = "Список: 1 0 5 4 -5 25.5 \nЗначение: 5"#Пример верного ввода данных
    hand.error_enter = "Неверный формат ввода данных. Вводить можно только целые и дробные числа. См. пример."#Ошибка при вводе посторонних знаков, например букв
    hand.handling_func = del_all_by_name #функция, обратывающая данные -> выполняющая задание
    hand.example_y =  175 #высота кнопки 'Пример'
    hand.add = t.Tk() #создание графического окна
    hand.fetch_data = fetch_data #переопределение функции обработки введённых данных
    
    t.Label(hand.add, text = "Значение:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 375, y = 115)#Лейбл
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 8) #Вторая строка для ввода
    enter2.place(x = 375, y = 145) #Размещение в окне
    hand.start() #Начало работы окна, запуск бесконечного событийного цикла

def but_3():
    global hand
    if hand:
        hand.single_window()
          
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get()
        rdata2 = enter2.get()
        try:
            data = list(map(lambda x: float(x) if x.count(".") else int(x), rdata.split()))
            data2 = list(map(lambda x: float(x) if x.count(".") else int(x), rdata2.split()))
            
            if len(data) != len(data2):
                hand.call_error("Списки должны быть равной длины, чтобы чередование было возможным.")
                return
            
            self.tbox2 = self.handling_func(data, data2)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)
            
    if hand:
        hand.single_window()
    hand = Handler("3 вариант")
    hand.tbox1  = "Склеить два списка, чередуя их элементы "
    hand.enter_label_text = "Введите элементы первого списка через пробел:"
    hand.example = "Первый список: 1 0 -5 25.5 \nВторой список:  1 2 3.2"
    hand.example_y =  175
    hand.termbox_y =  1
    hand.enter_y = 95
    hand.handling_func = sticker
    hand.fetch_data = fetch_data
    hand.add = t.Tk()
    
    t.Label(hand.add, text = "Введите элементы второго списка через пробел:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 120)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 32)
    enter2.place(x = 5, y = 145)
    hand.start()  


def but_4():
    global hand
    if hand:
        hand.single_window()
      
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get().split()
        rdata2 = enter2.get().replace(" ", "")
        rdata3 = enter3.get().replace(" ", "")
        try:
            if not rdata or not rdata2 or not rdata3:
                hand.call_error("Не все данные введены.")
                return

            arr = list(map(lambda x: float(x) if x.count(".") else int(x), rdata))
            key =  float(rdata2) if rdata2.count(".") else int(rdata2)
            n = int(rdata3)
            if n <= 0:
                hand.call_error("n должно быть целым положительным числом.")
                return
            if key not in arr:
                hand.call_error("Указанного элемента в списке нет.")
                return
            if n + arr.index(key) >= len(arr):
                hand.call_error("Передвижение элемента на указанное кол-во позиций(%s) невозможно.\nВыход за пределы списка."%(n))
                return                
            self.tbox2 = self.handling_func(arr, key, n)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)

    hand = Handler("4 вариант")
    hand.tbox1  = "Написать программу передвижения элемента на n позиций вперед."
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "Список: 1 0 -5 25.5 \nn:  2\nЭлемент: 1"
    hand.example_y =  180
    hand.termbox_y =  2
    hand.enter_y = 120
    hand.error_enter = "Неверный формат ввода данных. Список может состоять дробных и целых чисел, n может быть только целым числом. См. пример."
    hand.handling_func = to_n_further
    hand.res_label_y = 180
    hand.get_res_y = 180
    
    hand.add = t.Tk()
    t.Label(hand.add, text = "Передвигаемый элемент:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 145)
    t.Label(hand.add, text = "Значение n:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 378, y = 93)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter2.place(x = 240, y = 150)
    enter3 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter3.place(x = 380, y = 120)
    hand.fetch_data = fetch_data
    
    hand.start() 

def but_5():
    global hand
    if hand:
        hand.single_window()
      
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get().split()
        rdata2 = enter2.get().replace(" ", "")
        rdata3 = enter3.get().replace(" ", "")
        try:
            if not rdata or not rdata2 or not rdata3:
                hand.call_error("Не все данные введены.")
                return

            arr = list(map(lambda x: float(x) if x.count(".") else int(x), rdata))
            start =  int(rdata2)
            amount = int(rdata3)
            
            if start >= len(arr) or start < 0:
                hand.call_error("Начальный индекс может быть только целым положительным числом, не превышающим размер списка.")
                return
            if amount <= 0 or start + amount > len(arr):
                hand.call_error("Кол-во элементов должно быть положительным числом и не должно превышать возможное кол-во элементов.")
                return                
            self.tbox2 = self.handling_func(start, amount, arr)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)

    hand = Handler("5 вариант")
    hand.tbox1  = "Выборочное копирование списка – с указанием начала и количества элементов копируемой части "
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "Список: 1 0 -5 25.5 \nНачальный индекс:  2\nКол-во: 1\nВнимание! Индексы начинаются с 0."
    hand.example_y =  180
    hand.termbox_y =  2
    hand.enter_y = 120
    hand.error_enter = "Неверный формат ввода данных. Список может состоять дробных и целых чисел, Количество/начальный индекс могут быть только целыми числами. См. пример."
    hand.handling_func = copy_part
    hand.res_label_y = 180
    hand.get_res_y = 180
    
    hand.add = t.Tk()
    t.Label(hand.add, text = "Начальный индекс:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 145)
    t.Label(hand.add, text = "Количество:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 378, y = 93)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter2.place(x = 185, y = 150)
    enter3 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter3.place(x = 380, y = 120)
    hand.fetch_data = fetch_data
    
    hand.start() 

def but_6():
    global hand
    if hand:
        hand.single_window()
          
    hand = Handler("6 вариант")
    hand.tbox1  = "Инверсия порядка элементов в списке "
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "1 0 -5 25.5 1 2 3.2"
    hand.handling_func = reverse
    hand.add = t.Tk()
    hand.start() 

def but_7():
    global hand
    if hand:
        hand.single_window()
          
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get()
        rdata2 = enter2.get()
        try:
            data = list(map(lambda x: float(x) if x.count(".") else int(x), rdata.split()))
            data2 = list(map(lambda x: float(x) if x.count(".") else int(x), rdata2.split()))
            
            
            self.tbox2 = self.handling_func(data, data2)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)
            
    if hand:
        hand.single_window()
    hand = Handler("7 вариант")
    hand.tbox1  = "Создать список содержащий элементы общие для двух списков."
    hand.enter_label_text = "Введите элементы первого списка через пробел:"
    hand.example = "Первый список: 1 0 -5 25.5 \nВторой список:  1 2 3.2"
    hand.example_y =  210
    hand.termbox_y =  1
    hand.win_height = 335
    hand.enter_y = 130
    hand.res_label_y += 35
    hand.resbox_y += 35
    hand.get_res_y += 35
    hand.termbox_y  = 2
    hand.handling_func = common
    hand.fetch_data = fetch_data
    hand.add = t.Tk()
    
    t.Label(hand.add, text = "Введите элементы второго списка через пробел:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 155)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 32)
    enter2.place(x = 5, y = 182)
    hand.start()  

def but_8():
    global hand
    if hand:
        hand.single_window()
      
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get().split()
        rdata2 = enter2.get()
        rdata3 = enter3.get()
        try:
            if not rdata or not rdata2.replace(" ", "") or not rdata3.replace(" ", ""):
                hand.call_error("Не все данные введены.")
                return

            arr = list(map(lambda x: float(x) if x.count(".") else int(x), rdata))
            if len(arr) < 2:
                hand.call_error("Чтобы совершать операции обмена, длина массива должна быть не меньше двух.")
                return
            
            n1 = int(rdata2)
            n2 = int(rdata3)
            
            if max(n1, n2) > len(arr) or min(n1, n2) <= 0 or n1 == n2:
                hand.call_error("Номера могут быть только целыми различными положительными числами, не превышающими размер списка.")
                return          
            self.tbox2 = self.handling_func(arr, n1, n2)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)

    hand = Handler("8 вариант")
    hand.tbox1  = "Обмен значений двух элементов с данными номерами: swap(список,номер1,номер2)"
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "Список: 1 0 -5 25.5 \nПервый номер:  2\nВторой номер: 1. \nВнимание! Номера начинаются с 1."
    hand.example_y =  180
    hand.termbox_y =  2
    hand.enter_y = 120
    hand.error_enter = "Неверный формат ввода данных. Список может состоять дробных и целых чисел, номера могут быть только целыми числами. См. пример."
    hand.handling_func = swap
    hand.res_label_y = 180
    hand.get_res_y = 180
    
    hand.add = t.Tk()
    t.Label(hand.add, text = "Номер1:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 145)
    t.Label(hand.add, text = "Номер2:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 378, y = 93)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter2.place(x = 100, y = 150)
    enter3 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter3.place(x = 380, y = 120)
    hand.fetch_data = fetch_data
    
    hand.start() 

def but_9():
    global hand
    if hand:
        hand.single_window()
          
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get()
        rdata2 = enter2.get()
        try:
            data = list(map(lambda x: float(x) if x.count(".") else int(x), rdata.split()))
            data2 = list(map(lambda x: float(x) if x.count(".") else int(x), rdata2.split()))
            
            if len(data) != len(data2):
                hand.call_error("Списки должны быть равной длины.")
                return
            self.tbox2 = self.handling_func(data, data2)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)
            
    if hand:
        hand.single_window()
    hand = Handler("9 вариант")
    hand.tbox1  = "Сравнение двух списков равной длины, также списки могут содержать повторяющиеся элементы."
    hand.enter_label_text = "Введите элементы первого списка через пробел:"
    hand.example = "Первый список: 1 -5 25.5 \nВторой список:  1 2 3.2"
    hand.example_y =  210
    hand.win_height = 335
    hand.enter_y = 130
    hand.res_label_y += 35
    hand.resbox_y += 35
    hand.get_res_y += 35
    hand.termbox_y  = 2
    hand.handling_func = compareList
    hand.fetch_data = fetch_data
    hand.add = t.Tk()
    
    t.Label(hand.add, text = "Введите элементы второго списка через пробел:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 155)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 32)
    enter2.place(x = 5, y = 182)
    hand.start() 

def but_10():
    global hand
    if hand:
        hand.single_window()
          
    hand = Handler("10 вариант")
    hand.tbox1  = "Построить список, содержащий каждый второй элемент исходного списка "
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.handling_func = every_second_item
    hand.example = "Первый список: 1 0 -5 25.5"
    hand.add = t.Tk()
    hand.start() 

def but_11():
    def fetch_data():
        global hand
        rlist = hand.enter.get().split()
        ritem = enter2.get().replace(" ", "")
        try:
            if not rlist or not ritem:
                hand.call_error("Список пустой или значение не задано.")
                return
        
            data = list(map(float, rlist))
            key =  float(ritem)            
            hand.tbox2 = hand.handling_func(data, key)
            hand.stable_resbox()
        except ValueError:
            print("!")
            hand.call_error(hand.error_enter)
    
    global hand
    if hand:
        hand.single_window()

    hand = Handler("11 вариант")
    hand.tbox1 = "Подсчет количества равных, больших и меньших по значению элементов относительно заданного значения."
    hand.example = "Список: 1 0 5 4 -5 25.5 \nЗначение: 5"
    hand.error_enter = "Неверный формат ввода данных. Вводить можно только целые и дробные числа. См. пример."
    hand.handling_func = gr_eq_sm
    hand.example_y =  175 
    hand.add = t.Tk() 
    hand.fetch_data = fetch_data 
    
    t.Label(hand.add, text = "Значение:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 375, y = 115)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 8) 
    enter2.place(x = 375, y = 145) 
    hand.start() 

def but_12():
    global hand
    if hand:
        hand.single_window()
      
    def fetch_data():
        self = None
        if hand:
            self = hand
        rdata = self.enter.get().split()
        rdata2 = enter2.get()
        rdata3 = enter3.get()
        try:
            if not rdata or not rdata2.replace(" ", "") or not rdata3.replace(" ", ""):
                hand.call_error("Не все данные введены.")
                return

            arr = list(map(lambda x: float(x) if x.count(".") else int(x), rdata))
            k =  int(rdata2)
            n = int(rdata3)
            
            if k not in range(1,len(arr)+1) :
                hand.call_error("Значение k выходит за пределы списка.")
                return
            if k - n <= 0:
                hand.call_error("Передвижение элемента на указанное кол-во позиций(%s) невозможно.\nВыход за пределы списка."%(n))
                return                
            self.tbox2 = self.handling_func(arr, k, n)
            self.stable_resbox()
            
        except ValueError:
            hand.call_error(self.error_enter)

    hand = Handler("12 вариант")
    hand.tbox1  = "Написать программу передвижения k –го элемента на n позиций назад."
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "Список: 1 0 -5 25.5 \nn:  2\nk: 1"
    hand.example_y =  180
    hand.termbox_y =  2
    hand.enter_y = 120
    hand.error_enter = "Неверный формат ввода данных. Список может состоять дробных и целых чисел, n и k могут быть только целыми положительными числами. См. пример."
    hand.handling_func = move_n_backwards
    hand.res_label_y = 180
    hand.get_res_y = 180
    
    hand.add = t.Tk()
    t.Label(hand.add, text = "Значение k:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 145)
    t.Label(hand.add, text = "Значение n:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 378, y = 93)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter2.place(x = 120, y = 150)
    enter3 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 6)
    enter3.place(x = 380, y = 120)
    hand.fetch_data = fetch_data
    
    hand.start() 

def but_13():
    global hand
    if hand:
        hand.single_window()
      
    def fetch_data():
        global hand
        rdata = hand.enter.get().split()
        rdata2 = enter2.get().split()
        try:
            if not rdata or not rdata2:
                hand.call_error("Не все данные введены.")
                return
            
            if len(rdata2) != 2:
                hand.call_error("Диапазон может состоять только из двух чисел.")
                return
            
            data = list(map(lambda z: float(z) if z.count(".") else int(z), rdata))
            rang = list(map(int, rdata2))
            print(rang)
            rang[-1] += 1

            
            hand.tbox2 = hand.handling_func(data, range(*rang))
            hand.stable_resbox()

            
        except ValueError:
            hand.call_error(hand.error_enter)    
    hand = Handler("13 вариант")
    hand.tbox1  = "Построить список1 из элементов исходного списка, не попадающих в заданный диапазон значений, и список2 из элементов исходного списка, попадающих в заданный диапазон значений"
    hand.enter_label_text = "Введите элементы первого списка через пробел:"
    hand.error_enter = "Неверный формат ввода данных. Элементы списка - дробные и целые числа через пробел, границы диапазона - целые числа через пробел"
    hand.example = "Cписок: 1 0 -5 25.5 \nДиапазон:  5 25\nВнимание! Обе границы диапазона нестрогие [5, 25]"
    hand.example_y = 175 + 75
    hand.enter_y = 105 + 75
    hand.termbox_y = 4
    hand.handling_func = range_sep
    hand.fetch_data = fetch_data
    hand.win_height += 75
    hand.res_label_y += 75
    hand.resbox_y += 75
    hand.get_res_y += 75
    
    
    hand.add = t.Tk()
    t.Label(hand.add, text = "Введите границы диапазона через пробел:", font = ("New Times Roman", 14), bg = "light goldenrod yellow").place(x = 0, y = 140 + 75)
    enter2 = t.Entry(hand.add, font = ("New Times Roman", 14), width = 7)
    enter2.place(x = 400, y = 135 + 75)
    hand.start() 

def but_14():
    global hand
    if hand:
        hand.single_window()
          
    hand = Handler("14 вариант")
    hand.tbox1  = "Из списка, возможно содержащего одинаковые элементы, сформировать список, в который войдут все уникальные элементы исходного списка без повторений"
    hand.enter_label_text = "Введите элементы списка через пробел:"
    hand.example = "1 2 3.2 2 2 4 2"
    hand.handling_func = Uniqum
    hand.add = t.Tk()
    hand.start() 

def but_15():
    global hand
    if hand:
        hand.single_window()
        
    hand = Handler("15 вариант")
    hand.tbox1 = "Из исходного списка сформировать другой, состоящий из элементов первого, к которым присоединены элементы первого в обратном порядке. "
    hand.example = "1 0 5 4 -5 25.5"
    hand.error_enter = "Неверный формат ввода данных. Вводить можно только целые и дробные числа через пробел. См. пример."
    hand.handling_func = mirror_repeat
    hand.win_width += 20
    
    hand.add = t.Tk()
    hand.start()
#----
def stable_pos(e):
    main.geometry("800x600+500+200")

def mouse_click(e):
    print(e)
l1_text = """Дополнительные задания к 2 лабораторной работе СиАОД
Сделал студент группы ПИН/б-21-1-о
Тимошенко А. А."""
l2_text_1 = "Чтобы проверить:"
l2_text_2 = "Нажмите по варианту, чтобы увидеть задание и интерфейс для проверки."
main = t.Tk()
main.title("Дополнительные задания к 2 лабораторной работе")
main["bg"] = "floral white"
main.geometry("800x600+500+200")
main.resizable(width = False, height = False)
main.bind('<Configure>', stable_pos) #неподвижность окна
#main.overrideredirect(True)

l_info = t.Label(text = l1_text, font = ("New Times Roman", 20))
l_info.config(bd = 25, bg = "floral white")
l_info.pack()

l_about_1 = t.Label(text = l2_text_1, font = ("New Times Roman", 20, "bold"), cursor = "star")
l_about_1.config(bg = "floral white")
l_about_1.pack(anchor = "w")

l_about_2 = t.Label(text = l2_text_2, font = ("New Times Roman", 16, "italic"), cursor = "star")
l_about_2.config(bg = "floral white")
l_about_2.pack(anchor = "w")

t.Label(text = "Варианты: ", font = ("New Times Roman", 20, "bold"), bg = "floral white", bd = 50).pack()

for i in range(1, 16):
    exec("var_%s = t.Button(text = \"%s вариант\", bg = \"light grey\", width = 17, height = 3, command = but_%s, bd = 3)"%(i, i, i))
    exec("var_%s.config(font = (\"New Times Roman\", 10, \"bold\"))"%(i))
    exec("var_%s.place(x = %s, y = %s)"%(i, 20 + 153*((i - 1)%5), 350 + 75*((i - 1)//5)))
main.mainloop()
