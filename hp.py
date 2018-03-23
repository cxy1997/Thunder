from utils import hpcl

class HP:
    def __init__(self, master):
        self.master = master
        self.r = self.master.canvas.create_rectangle(25, 20, 225, 60, fill = 'green', outline = 'green')
        self.t = self.master.canvas.create_text(75, 40, text = 'HP:100', fill = 'white', font = ('Arial', 20, 'bold'))
        self.tt = self.master.canvas.create_text(400, 50, text = 'Score:\n 0', fill='cyan', font=('Arial', 20, 'normal'))
    def upd(self):
        self.master.canvas.coords(self.r, 25, 20, self.master.sonic.hp * 2 + 24, 60)
        self.master.canvas.itemconfig(self.r, fill = hpcl(self.master.sonic.hp), outline = hpcl(self.master.sonic.hp))
        self.master.canvas.itemconfig(self.t, text = 'HP:' + str(self.master.sonic.hp))
        self.master.canvas.itemconfig(self.tt, text = 'Score:\n ' + str(self.master.score))
        if self.master.sonic.hp == 0:
            self.master.canvas.itemconfig(self.r, state = 'hidden')
        self.master.canvas.lift(self.r)
        self.master.canvas.lift(self.t)
        self.master.canvas.lift(self.tt)