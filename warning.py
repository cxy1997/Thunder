class warning:
    def __init__(self, master):
        self.master = master
        self.s = 0
    def on(self):
        self.s = 1
        self.t = 120
        self.t1 = self.master.canvas.create_text(240, 300, text = '   Boss\nWarning', fill = '#FF0000', font = ('Arial', 48, 'normal'))
        self.p = []
        px = -60
        for i in range(10):
            px += 60
            self.p.append(self.master.canvas.create_polygon((px, 0), (px + 30, 0), (px, 80), (px - 30, 80), fill = 'red'))
            self.p.append(self.master.canvas.create_polygon((px, 510), (px + 30, 510), (px, 590), (px - 30, 590), fill = 'red'))
    def upd(self):
        if self.s == 1:
            for i in self.p:
                self.master.canvas.lift(i)
            self.master.canvas.lift(self.t1)
            if self.master.pause.get() == 0:
                self.t -= 1
            if self.t == 0:
                self.clear()
                self.master.boss.showup()
    def clear(self):
        if self.s == 1:
            for i in self.p:
                self.master.canvas.delete(i)
                del i
            self.master.canvas.delete(self.t1)
            del self.t1
            del self.t
            self.s = 0