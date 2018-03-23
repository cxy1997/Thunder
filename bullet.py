from Tkinter import PhotoImage
from math import sqrt
from random import randrange
from linked_list import Linked_List, dlt
from utils import bulletspeed, hit_the_boss

def kill(p):
    p.master.master.canvas.delete(p.pic)
    p.master.master.bu.new(p.x, p.y)
    p.master.n -= 1
    dlt(p)

class enemyBullets:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\enemybullet1.gif')
        self.data = Linked_List(-100, -100, self)

    def new(self, x, y):
        s = sqrt((self.master.sonic.x - x) ** 2 + (self.master.sonic.y - y) ** 2)
        dx = int(round((self.master.sonic.x - x) * bulletspeed(self.master.stage) / (s + 0.01)))
        dy = int(round((self.master.sonic.y - y) * bulletspeed(self.master.stage) / (s + 0.01)))
        self.data.add(x, y, 0, dx, dy)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)

    def upd(self):
        p = self.data
        while p._next:
            p = p.next
            p.x += p.dx
            p.y += p.dy
            self.master.canvas.move(p.pic, p.dx, p.dy)
            if p.y <- 40 or p.y > 800 or p.x <- 20 or p.x > 500:
                p = p.last
                dlt(p.next)
            if (p.x - self.master.sonic.x) ** 2 + (p.y - self.master.sonic.y) ** 2 < 401:
                self.master.sb.new(p.x, p.y)
                if self.master.sonic.shield == 0:
                    self.master.sonic.hp -= 10
                    self.master.score -= 100
                    self.master.sonic.shield = 10
                    if self.master.sonic.weaponmode > 1:
                        self.master.sonic.weaponmode -= 1
                else:
                    self.master.sonic.shield -= 10
                    if self.master.sonic.shield < 0:
                        self.master.sonic.shield = 0
                self.master.canvas.delete(p.pic)
                if not p._next:
                    p.last._next = False
                    p = p.last
                    del p.next
                else:
                    p.last.next = p.next
                    p = p.last
                    del p.next.last
                    p.next.last = p
                if self.master.sonic.hp <= 0 and not self.master.gameover:
                    self.master.gameover = True
                    self.master.sonic.hp = 0
                    self.master.bu.new(self.master.sonic.x, self.master.sonic.y)
                    self.master.sonic.status = 0
                    self.master.die()

    def clear(self):
        p = self.data
        while p._next:
            dlt(p.next)

class myBullets:
    def __init__(self, master):
        self.master = master
        self.img = PhotoImage(file = 'images\\mybullet.gif')
        self.data = Linked_List(-100, -100, self)
    def new(self, x, y):
        self.data.add(x, y)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def upd(self):
        p = self.data
        while p._next:
            p = p.next
            p.y -= 6
            self.master.canvas.move(p.pic, 0, -6)
            if p.y <- 40:
                p = p.last
                dlt(p.next)
            if self.master.boss.status == 0:
                q = self.master.enemies.data
                mark = True
                while q._next and mark:
                    q = q.next
                    if (p.x - q.x) ** 2 + (p.y - q.y) ** 2 < 401:
                        q.hp -= 25
                        mark = False
                        self.master.sb.new(p.x, p.y)
                        self.master.score += 25
                        p = p.last
                        dlt(p.next)
                        if q.hp <= 0:
                            kill(q)
                            if randrange(6) == 0:
                                self.master.p.add(q.x, q.y)
            else:
                if hit_the_boss(p.x, p.y):
                    self.master.sb.new(p.x, p.y)
                    self.master.score += 25
                    p = p.last
                    dlt(p.next)
                    self.master.boss.hp -= 25
                    if self.master.boss.hp <= 0:
                        self.master.boss.vanish()
    def clear(self):
        p = self.data
        while p._next:
            dlt(p.next)