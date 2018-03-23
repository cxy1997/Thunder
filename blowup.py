from Tkinter import PhotoImage
from linked_list import Linked_List, dlt

class Blowups:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\bomb1.gif')
        self.data = Linked_List(-100, -100, self)

    def new(self, x, y):
        self.data.add(x, y)

    def upd(self):
        p = self.data
        while p._next:
            p = p.next
            p.t += 1
            if p.t == 6:
                p = p.last
                dlt(p.next)
            else:
                p.master.master.canvas.lift(p.pic)

    def clear(self):
        p = self.data
        while p._next:
            dlt(p.next)

class smallBlowups:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\bomb2.gif')
        self.data = Linked_List(-100, -100, self)

    def new(self, x, y):
        self.data.add(x, y)

    def upd(self):
        p = self.data
        while p._next:
            p = p.next
            p.t += 1
            if p.t == 6:
                p = p.last
                dlt(p.next)
            else:
                p.master.master.canvas.lift(p.pic)

    def clear(self):
        p = self.data
        while p._next:
            dlt(p.next)