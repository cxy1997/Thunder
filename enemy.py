from Tkinter import PhotoImage
from linked_list import Linked_List, dlt
from utils import firerate

class Enemies:
    def __init__(self, master):
        self.n = 0
        self.master = master
        self.img = PhotoImage(file='images\\enemy1.gif')
        self.data = Linked_List(-100, -100, self)
    def new(self, x, y):
        self.n += 1
        self.data.add(x, y, 50*self.master.stage + 50)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def up(self):
        p = self.data
        while p._next:
            p = p.next
            self.master.canvas.lift(p.pic)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def upd(self):
        p = self.data
        while p._next:
            p = p.next
            p.t += 1
            if p.t % firerate(self.master.stage) == firerate(self.master.stage) - 1:
                self.master.eb.new(p.x, p.y)
                self.up()
    def showup(self, n):
        if n == 1:
            self.new(160, 120)
        elif n == 2:
            self.new(120, 160)
            self.new(360, 160)
        elif n == 3:
            self.new(240, 200)
            self.new(160, 140)
            self.new(320, 140)
        elif n == 4:
            self.new(240, 100)
            self.new(240, 220)
            self.new(120, 160)
            self.new(360, 160)
        elif n == 5:
            self.new(240, 280)
            self.new(159, 221)
            self.new(321, 221)
            self.new(190, 86)
            self.new(290, 86)
        elif n == 6:
            self.new(240, 186)
            self.new(300, 290)
            self.new(180, 290)
            self.new(120, 186)
            self.new(360, 186)
            self.new(300, 82)
            self.new(180, 82)
        elif n == 7:
            self.master.w.on()
    def clear(self):
        p = self.data
        while p._next:
            dlt(p.next)
        self.n = 0