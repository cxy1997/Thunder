from Tkinter import Toplevel, Canvas, PhotoImage, Button
from string import split, join
from utils import myCmp

class Scores:
    def __init__(self, master):
        self.landmark = True
        self.master = master
        self.data = []

    def add(self, s):
        s = split(s)
        a = join(s[:-1], ' ')
        self.data.append([a, int(s[-1])])
        self.data.sort(myCmp)
        if len(self.data) > 5:
            del self.data[5]

    def showup(self):
        self.master.pause.set(1)
        self.root = Toplevel()
        self.root.title('Highest Scores')
        self.root.geometry('300x400')
        self.root.iconbitmap('images\\hs.ico')
        self.canvas = Canvas(self.root, height = 400, width = 300)
        self.canvas.place(x = 0, y = 0)
        self.img = PhotoImage(file = 'images\\general.gif')
        self.pic = self.canvas.create_image(150, 200, image = self.img)
        for i in range(5):
            self.canvas.create_text(150, 120 + 50 * i, text = str(i + 1) + '. ' + self.data[i][0] + '  ' + str(self.data[i][1]), fill = 'blue', font = ('Arial', 20))
        Button(self.root, text = 'Back', command = self.halt).place(x = 140, y = 350)
        self.root.protocol('WM_DELETE_WINDOW', self.halt)
        self.root.focus_set()

    def halt(self):
        self.root.destroy()
        self.master.pause.set(0)
        if not self.landmark:
            self.landmark = True
            self.master.homepage()
            self.master.canvas.itemconfig(self.master.health.r, state = 'hidden')
            self.master.canvas.itemconfig(self.master.health.t, state = 'hidden')
            self.master.canvas.itemconfig(self.master.health.tt, state = 'hidden')
            self.master.f.status = 0
            self.master.canvas.delete(self.master.f.tt)
            self.master.enemies.clear()
            self.master.eb.clear()
            self.master.mb.clear()
            self.master.p.clear()
            self.master.canvas.itemconfig(self.master.sonic.aos_pic, state = 'hidden')
            self.master.bu.clear()
            self.master.sb.clear()
            if self.master.boss.status:
                self.master.boss.clear()