from Tkinter import PhotoImage

class fighter:
    def __init__(self, master):
        self.master = master
        self.aos_img = PhotoImage(file = 'images\\aos.gif')
        self.aos_pic = self.master.canvas.create_image(240, 550, image = self.aos_img)
        self.master.canvas.itemconfig(self.aos_pic, state = 'hidden')
        self.status = 1
        self.shield = 0
        self.hp = 100
        self.weaponmode = 1
        self.step = 12
        self.x = 240
        self.y = 540
        self.number = 1
        self.img = PhotoImage(file = 'images\\plane1.gif')
        self.pic = self.master.canvas.create_image(self.x, self.y, image = self.img)

    def change(self):
        self.number = self.number % 3 + 1
        self.img = PhotoImage(file = 'images\\plane' + str(self.number) + '.gif')
        self.pic = self.master.canvas.create_image(self.x, self.y, image = self.img)
        if self.master.gameover or not self.status:
            self.master.canvas.itemconfig(self.pic, state = 'hidden')

    def fire(self):
        if self.weaponmode == 1:
            self.master.mb.new(self.x, self.y - 20)
        elif self.weaponmode == 2:
            self.master.mb.new(self.x - 15, self.y - 20)
            self.master.mb.new(self.x + 15, self.y - 20)
        elif self.weaponmode == 3:
            self.master.mb.new(self.x - 15, self.y - 15)
            self.master.mb.new(self.x, self.y - 25)
            self.master.mb.new(self.x + 15, self.y - 15)

    def scaleX(self):
        return 33 if self.number < 3 else 44

    def scaleY(self):
        return 41 if self.number < 3 else 33

    def left(self, event):
        if self.x - self.scaleX() > self.step and not self.master.pause.get() and not self.master.gameover:
            self.x -= self.step
            self.master.canvas.move(self.pic, -self.step, 0)
            self.master.canvas.move(self.aos_pic, -self.step, 0)

    def right(self, event):
        if self.x + self.scaleX() < 480 - self.step and not self.master.pause.get() and not self.master.gameover:
            self.x += self.step
            self.master.canvas.move(self.pic, self.step, 0)
            self.master.canvas.move(self.aos_pic, self.step, 0)

    def up(self, event):
        if self.y - self.scaleY() > self.step and not self.master.pause.get() and not self.master.gameover:
            self.y -= self.step
            self.master.canvas.move(self.pic, 0, -self.step)
            self.master.canvas.move(self.aos_pic, 0, -self.step)

    def down(self, event):
        if self.y + self.scaleY() < 588 - self.step and not self.master.pause.get() and not self.master.gameover:
            self.y += self.step
            self.master.canvas.move(self.pic, 0, self.step)
            self.master.canvas.move(self.aos_pic, 0, self.step)