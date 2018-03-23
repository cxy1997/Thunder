class Flag:
    def __init__(self, master):
        self.master = master
        self.status = 0

    def showup(self):
        self.master.eb.clear()
        self.t = 0
        self.status = 1
        self.tt = self.master.canvas.create_text(240, 300, text = 'Stage ' + str(self.master.stage), fill = '#FF9900', font = ('Arial', 42))
    
    def upd(self):
        self.t += 1
        if self.t == 60:
            self.master.canvas.itemconfig(self.tt, text = 'Start')
        elif self.t == 90:
            self.clear()
            
    def clear(self):
        if self.status == 1:
            self.status = 0
            self.master.canvas.delete(self.tt)