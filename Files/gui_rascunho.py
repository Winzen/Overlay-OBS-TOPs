from tkinter import Tk, Button, Canvas, BOTH, TOP, Label, Entry, CENTER
import threading
from html_top8_video import make_top8_video
from top16_html import rodape_html


class Janela:

    def __init__(self):
        self.window = Tk()
        self.window.title("BRK Overlays")
        self.window.iconbitmap(r"icon\brk.ico")
        self.menus_center = self.menu_left = self.entry = self.news = self.menus_top = None

        self.window.geometry("500x150")
        self.window.eval('tk::PlaceWindow . center')
        self.window.resizable(width=False, height=False)

        self.window.rowconfigure([0, 1], minsize=50, weight=1)

        self.window.columnconfigure([0, 1], minsize=50, weight=1)

        self.telas()

        self.entry_link()
        self.button()
        self.label_info_status()

        self.window.mainloop()

    def telas(self):

        self.menus_top = Canvas(bg="#023047", width=350, height=50, master=self.window)
        self.menus_top.pack(side=TOP, fill=BOTH)

        label = Label(self.menus_top, text="Gerador de Top 8/Top 16", font=('helvetica', 16, 'bold'), bg="#023047",
                      fg="#ffb703")
        label.place(anchor=CENTER, relx=0.5, rely=0.5)

        self.menus_center = Canvas(bg="#219ebc", width=350, height=50,
                                   master=self.window)
        self.menus_center.pack(side=TOP, fill=BOTH)

        self.menu_left = Canvas(bg="#8ecae6", width=350, height=50, master=self.window)
        self.menu_left.pack(side=TOP, fill=BOTH)

    def entry_link(self):

        label = Label(self.menus_center, text="Link EVENTO AQUI:", font=('helvetica', 9, 'bold'), bg="#219ebc")
        label.place(anchor=CENTER, relx=0.15, rely=0.5)
        self.entry = Entry(self.menus_center, width=50)
        self.entry.place(anchor=CENTER, relx=0.60, rely=0.5)

    def button(self):

        button1 = Button(master=self.menu_left, command=self.thredad1,
                         text='Top 8', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        button1.place(anchor=CENTER, relx=0.08, rely=0.5)

        button2 = Button(master=self.menu_left, command=self.thredad2,
                         text='Top 16', bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        button2.place(anchor=CENTER, relx=0.18, rely=0.5)

    def label_info_status(self):
        self.news = Label(self.menu_left, text="Nenhum Evento colocado", font=('helvetica', 9, 'bold'), bg="#8ecae6")
        self.news.place(anchor=CENTER, relx=0.60, rely=0.5)

    def make_image_top8(self):

        self.news.config(text="Processando..")

        self.window.update()

        img_top8 = make_top8_video(self.entry.get())

        self.news.config(text=img_top8, width=50)

    def thredad1(self):
        thre1 = threading.Thread(target=self.make_image_top8)
        thre1.start()

    def make_image_top16(self):

        self.news.config(text="Processando..")

        self.window.update()

        img_top8 = rodape_html(self.entry.get())

        self.news.config(text=img_top8, width=50)

    def thredad2(self):
        thre1 = threading.Thread(target=self.make_image_top16)
        thre1.start()
