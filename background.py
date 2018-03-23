from Tkinter import PhotoImage

class Background:
    def __init__(self, master):
        self.x = 240
        self.y = -900
        self.number = 1
        self.master = master
        self.img = PhotoImage(file = 'images\\bg1.gif')
        self.pic = self.master.canvas.create_image(self.x, self.y, image = self.img)
        self.master.canvas.lower(self.pic)

    def roll(self):
        self.master.canvas.move(self.pic, 0, 1)
        self.y += 1
        if self.y == 1500:
            self.y = -900
            self.master.canvas.move(self.pic, 0, -2400)

    def change(self):
        self.number = self.number % 3 + 1
        self.img = PhotoImage(file = 'images\\bg' + str(self.number) + '.gif')
        self.pic = self.master.canvas.create_image(self.x, self.y, image = self.img)
        self.master.canvas.lower(self.pic)