from Tkinter import PhotoImage
from utils import bulletspeed, firerate

class Boss:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\ashroller.gif')
        self.status = 0
        self.hp = 1000
        self.lim = 360
        self.lazer_img1 = PhotoImage(file = 'images\\lazer1.gif')
        self.lazer_img2 = PhotoImage(file = 'images\\lazer2.gif')
        self.lazer_img3 = PhotoImage(file = 'images\\lazer3.gif')
        self.mark = [0, 0, 0]
        self.lazer_status = 0
        self.hpBar = self.master.canvas.create_rectangle(40, 70, 440, 75, width = 0, outline = '', fill = 'red')
        self.hpbar = self.master.canvas.create_rectangle(40, 70, 440, 75, width = 1, outline = 'white', fill = '')
        self.master.canvas.itemconfig(self.hpbar, state = 'hidden')
        self.master.canvas.itemconfig(self.hpBar, state = 'hidden')

    def showup(self):
        self.pic = self.master.canvas.create_image(240, 160, image = self.img)
        self.master.canvas.itemconfig(self.hpbar, state = 'normal')
        self.master.canvas.itemconfig(self.hpBar, state = 'normal')
        self.master.p.add(240, 224)
        self.t = 0
        self.status = 1

    def vanish(self):
        self.lazer_status = 0
        self.master.bu.new(240, 224)
        self.master.bu.new(180, 224)
        self.master.bu.new(3000, 224)
        self.master.bu.new(307, 200)
        self.master.bu.new(113, 200)
        self.master.bu.new(162, 150)
        self.master.bu.new(258, 150)
        self.master.bu.new(240, 150)
        self.master.bu.new(180, 150)
        self.master.bu.new(300, 150)
        self.master.bu.new(162, 100)
        self.master.bu.new(258, 100)
        self.master.bu.new(240, 100)
        self.master.bu.new(180, 100)
        self.master.bu.new(300, 100)
        self.master.p.add(240, 224)
        self.clear()
        self.mark = [0, 0, 0]
        self.hp = self.master.stage * 500 + 1000
        self.lim -= 30
        if self.lim < 120:
            self.lim = 120
        self.master.eb.clear()
        self.master.stage += 1
        self.master.wave = 0
        self.master.f.showup()

    def fire(self):
        self.t += 1
        if self.t % self.lim == 10:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.866)), int(round(bulletspeed(self.master.stage) * 0.5)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.866)), int(round(bulletspeed(self.master.stage) * 0.5)))
        elif self.t % self.lim == 20:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.766)), int(round(bulletspeed(self.master.stage) * 0.642)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.766)), int(round(bulletspeed(self.master.stage) * 0.642)))
        elif self.t % self.lim == 30:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.642)), int(round(bulletspeed(self.master.stage) * 0.766)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.642)), int(round(bulletspeed(self.master.stage) * 0.766)))
        elif self.t % self.lim == 40:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.5)), int(round(bulletspeed(self.master.stage) * 0.866)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.5)), int(round(bulletspeed(self.master.stage) * 0.866)))
        elif self.t % self.lim == 50:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.342)), int(round(bulletspeed(self.master.stage) * 0.939)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.342)), int(round(bulletspeed(self.master.stage) * 0.939)))
        elif self.t % self.lim == 60:
            self.master.eb.data.add(328, 235, 0, int(round(bulletspeed(self.master.stage) * 0.174)), int(round(bulletspeed(self.master.stage) * 0.984)))
            self.master.eb.data.add(152, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.174)), int(round(bulletspeed(self.master.stage) * 0.984)))
        elif self.t % self.lim == 70:
            self.master.eb.data.add(328, 235, 0, 0, bulletspeed(self.master.stage))
            self.master.eb.data.add(152, 235, 0, 0, bulletspeed(self.master.stage))
        elif self.t % self.lim == 80:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.174)), int(round(bulletspeed(self.master.stage) * 0.984)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.174)), int(round(bulletspeed(self.master.stage) * 0.984)))
        elif self.t % self.lim == 90:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.342)), int(round(bulletspeed(self.master.stage) * 0.939)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.342)), int(round(bulletspeed(self.master.stage) * 0.939)))
        elif self.t % self.lim == 100:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.5)), int(round(bulletspeed(self.master.stage) * 0.866)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.5)), int(round(bulletspeed(self.master.stage) * 0.866)))
        elif self.t % self.lim == 110:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.642)), int(round(bulletspeed(self.master.stage) * 0.766)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.642)), int(round(bulletspeed(self.master.stage) * 0.766)))
        elif self.t % self.lim == 120:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.766)), int(round(bulletspeed(self.master.stage) * 0.642)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.766)), int(round(bulletspeed(self.master.stage) * 0.642)))
        if self.t % self.lim == 130:
            self.master.eb.data.add(328, 235, 0, -int(round(bulletspeed(self.master.stage) * 0.866)), int(round(bulletspeed(self.master.stage) * 0.5)))
            self.master.eb.data.add(152, 235, 0, int(round(bulletspeed(self.master.stage) * 0.866)), int(round(bulletspeed(self.master.stage) * 0.5)))
        if (self.t % self.lim) % firerate(self.master.stage) == 5:
            self.master.eb.new(240, 224)
        if (self.lim - self.t) % self.lim == 121:
            self.l1 = self.master.canvas.create_image(240, 224, image = self.lazer_img1)
            self.mark[0] = 1
            self.master.canvas.lift(self.pic)
        elif (self.lim - self.t) % self.lim == 101:
            self.master.canvas.delete(self.l1)
            self.l2 = self.master.canvas.create_image(240, 243, image = self.lazer_img2)
            self.mark[0] = 0
            self.mark[1] = 1
            self.master.canvas.lift(self.pic)
        elif (self.lim - self.t) % self.lim == 81:
            self.master.canvas.delete(self.l2)
            self.l3 = self.master.canvas.create_image(240, 392, image = self.lazer_img3)
            self.mark[1] = 0
            self.mark[2] = 1
            self.lazer_status = 1
        elif (self.lim - self.t) % self.lim == 21:
            self.master.canvas.delete(self.l3)
            self.mark[2] = 0
            self.lazer_status = 0

    def upd(self):
        if self.status:
            self.fire()
            if self.lazer_status:
                if self.master.sonic.y > 84 and 180 < self.master.sonic.x < 300:
                    if self.master.sonic.shield == 0:
                        self.master.sonic.hp -= self.master.stage
                        self.master.score -= 10 * self.master.stage
                        if self.master.sonic.hp <= 0 and not self.master.gameover:
                            self.master.gameover = True
                            self.master.sonic.hp = 0
                            self.master.sonic.status = 0
                            self.master.bu.new(self.master.sonic.x, self.master.sonic.y)
                            self.master.die()
                        else:
                            self.master.sonic.shield -= self.master.stage
                            if self.master.sonic.shield < 0:
                                self.master.sonic.shield = 0
            if self.mark[0]:
                self.master.canvas.lift(self.l1)
            if self.mark[1]:
                self.master.canvas.lift(self.l2)
            if self.mark[2]:
                self.master.canvas.lift(self.l3)
            self.master.canvas.lift(self.pic)
            self.master.canvas.coords(self.hpBar, 40, 70, 40 + int(round(400.0 / (self.master.stage * 500+500) * self.hp)), 75)
            self.master.canvas.lift(self.hpBar)
            self.master.canvas.lift(self.hpbar)

    def clear(self):
        if self.status:
            self.master.canvas.delete(self.pic)
            self.master.canvas.itemconfig(self.hpbar, state = 'hidden')
            self.master.canvas.itemconfig(self.hpBar, state = 'hidden')
            self.status = 0
            if self.mark[0]:
                self.master.canvas.delete(self.l1)
            if self.mark[1]:
                self.master.canvas.delete(self.l2)
            if self.mark[2]:
                self.master.canvas.delete(self.l3)