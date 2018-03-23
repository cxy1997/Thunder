from Tkinter import PhotoImage
from random import randint

dX=[-3,3,-3,3]
dY=[-3,-3,3,3]

def nd(n, x):
    if n == 1 or n == 3:
        return (x + 2) % 4
    elif n == 2:
        return x + 1
    elif n == 4:
        return x - 1

class pcg:
    def __init__(self, x, y, direction, master):
        self.x = x
        self.y = y
        self.direction = direction
        self.master = master
        self.pic = self.master.master.canvas.create_image(self.x, self.y, image = self.master.img)

    def upd(self):
        if 20 > self.x + dX[self.direction]:
            self.direction = nd(2, self.direction)
        elif self.x + dX[self.direction] > 460:
            self.direction = nd(4, self.direction)
        self.x += dX[self.direction]
        if 20 > self.y + dY[self.direction]:
            self.direction = nd(1, self.direction)
        elif self.y + dY[self.direction] > 590:
            self.direction = nd(3, self.direction)
        self.y += dY[self.direction]
        self.master.master.canvas.move(self.pic, dX[self.direction], dY[self.direction])

class Packages:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\package.gif')
        self.data = []
        self.length = 0

    def clear(self):
        for i in self.data:
            self.master.canvas.delete(i.pic)
        del self.data
        self.data = []
        self.length = 0

    def add(self, x, y):
        self.data.append(pcg(x, y, randint(2, 3), self))
        self.length += 1

    def upd(self):
        x = []
        for j in range(self.length):
            i = self.data[j]
            i.upd()
            if (i.x - self.master.sonic.x) ** 2 + (i.y - self.master.sonic.y) ** 2 < 2000:
                if self.master.sonic.hp < 120:
                    self.master.sonic.hp += 25
                    if self.master.sonic.hp > 120:
                        self.master.sonic.hp = 120
                elif self.master.sonic.weaponmode < 3:
                    self.master.sonic.weaponmode += 1
                else:
                    self.master.sonic.shield += 240
                x = [j]+x
                self.master.score += 100
        self.length -= len(x)
        for i in x:
            self.master.canvas.delete(self.data[i].pic)
            del self.data[i]
        if not self.master.boss.status:
            for i in self.data:
                self.master.canvas.lift(i.pic)
            self.master.enemies.up()