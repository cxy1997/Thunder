from Tkinter import Toplevel, Canvas, PhotoImage, Button

class Help:
    def __init__(self, master):
        self.master = master

    def showup(self):
        self.master.pause.set(1)
        self.order = 1
        self.root = Toplevel()
        self.root.title('How to play')
        self.root.iconbitmap('images\\help.ico')
        self.root.geometry('400x300')
        self.root.protocol('WM_DELETE_WINDOW', self.halt)
        self.canvas = Canvas(self.root, height=300, width=400)
        self.canvas.place(x = 0, y = 0)
        self.img = []
        for i in range(6):
            self.img.append(PhotoImage(file = 'images\\train' + str(i + 1) + '.gif'))
        self.pic = self.canvas.create_image(200, 150, image = self.img[0])
        self.ba = Button(self.root, text = 'Last', command = self.last)
        self.bb = Button(self.root, text = 'Back', command = self.halt)
        self.bc = Button(self.root, text = 'Next', command = self.next)
        self.bb.place(x = 182, y = 190)
        self.bc.place(x = 340, y = 140)
        self.root.focus_set()

    def last(self):
        if self.order == 2:
            self.ba.place_forget()
        if self.order == 6:
            self.bc.place(x = 340, y = 140)
        self.order -= 1
        self.canvas.delete(self.pic)
        self.pic = self.canvas.create_image(200, 150, image = self.img[self.order - 1])

    def next(self):
        if self.order == 1:
            self.ba.place(x = 24, y = 140)
        if self.order == 5:
            self.bc.place_forget()
        self.order += 1
        self.canvas.delete(self.pic)
        self.pic = self.canvas.create_image(200, 150, image = self.img[self.order - 1])
        
    def halt(self):
        self.root.destroy()
        del self.root
        del self.order
        del self.canvas
        del self.img
        del self.pic
        del self.ba
        del self.bb
        del self.bc
        self.master.pause.set(0)