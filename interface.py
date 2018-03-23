from Tkinter import Tk, IntVar, Canvas, PhotoImage, Entry, Button, StringVar, Toplevel
from tkMessageBox import askokcancel
from string import lstrip, rstrip
from background import Background
from bullet import kill, enemyBullets, myBullets
from enemy import Enemies
from boss import Boss
from fighter import fighter
from blowup import Blowups, smallBlowups
from warning import warning
from flag import Flag
from hp import HP
from package import nd, pcg, Packages
from help import Help
from info import Info
from score import Scores
from controlset import ControlSet
from mymenu import myMenu

class Interface:
    def __init__(self):
        self.gameover = True
        self.t = 0
        self.stage = 1
        self.wave = 0
        self.score = 0
        self.root = Tk()
        self.root.title('Thunder')
        self.root.geometry('480x610')
        self.root.iconbitmap('images\\thunder.ico')
        self.pause = IntVar()
        self.canvas = Canvas(self.root, height = 600, width = 480, bg = 'white')
        self.canvas.place(x = 0, y = 0)
        self.galaxy = Background(self)
        self.mb = myBullets(self)
        self.enemies = Enemies(self)
        self.boss = Boss(self)
        self.eb = enemyBullets(self)
        self.sonic = fighter(self)
        self.canvas.itemconfig(self.sonic.pic, state = 'hidden')
        self.sb = smallBlowups(self)
        self.bu = Blowups(self)
        self.w = warning(self)
        self.f = Flag(self)
        self.health = HP(self)
        self.p = Packages(self)
        self.canvas.itemconfig(self.health.r, state = 'hidden')
        self.canvas.itemconfig(self.health.t, state = 'hidden')
        self.canvas.itemconfig(self.health.tt, state = 'hidden')
        self.he = Help(self)
        try:
            f = open('userdata.dat', 'r')
        except:
            f = open('userdata.dat', 'w')
            f.write('False\nPython 0\nPascal 0\nCauchy 0\nTom 0\nJerry 0')
            f.close()
            f = open('userdata.dat', 'r')
        self.introduction = Info(self, eval(f.readline()))
        self.scoreboard = Scores(self)
        for i in range(5):
            self.scoreboard.add(f.readline())
        f.close()
        self.landmark = True
        self.cs = ControlSet(self)
        self.menu = myMenu(self)
        self.startgif = PhotoImage(file = 'images\\startbutton.gif')
        self.startbutton = Button(self.root, image = self.startgif, bd = -2, relief = 'flat', command = self.start)
        self.settingsgif = PhotoImage(file = 'images\\settingsbutton.gif')
        self.settingsbutton = Button(self.root, image = self.settingsgif, bd = -2, relief = 'flat', command = self.cs.alter)
        self.howtoplaygif = PhotoImage(file = 'images\\howtoplaybutton.gif')
        self.howtoplaybutton = Button(self.root, image = self.howtoplaygif, bd = -2, relief = 'flat', command = self.he.showup)
        self.highscoresgif = PhotoImage(file = 'images\\highscoresbutton.gif')
        self.highscoresbutton = Button(self.root, image = self.highscoresgif, bd = -2, relief = 'flat', command = self.scoreboard.showup)
        self.quitgamegif = PhotoImage(file = 'images\\quitgamebutton.gif')
        self.quitgamebutton = Button(self.root, image = self.quitgamegif, bd = -2, relief = 'flat', command = self.quitcallback)
        self.title_img = PhotoImage(file = 'images\\title.gif')
        self.railgun_img = PhotoImage(file = 'images\\bilibili.gif')
        self.homepage()
        self.root.protocol('WM_DELETE_WINDOW', self.quitcallback)
        self.root.bind('<F1>', self.Pause)
        self.root.bind('<F12>', self.eventquit)
        self.root.bind('<Key-1>', self.changeBackground)
        self.root.bind('<Key-2>', self.changePlane)
        self.root.bind('<F3>', self.keysettings)
        self.root.bind('<F4>', self.controlInitialize)
        self.root.bind('<F9>', self.introduce)
        self.root.bind('<F10>', self.howtoplay)
        self.root.bind('<F11>', self.hsshow)
        self.root.bind('<F2>', self.begin)
        self.root.after(16, self.game)
        self.root.mainloop()

    def homepage(self):
        self.landmark = True
        self.startbutton.place(x = 180, y = 160)
        self.settingsbutton.place(x = 172, y = 230)
        self.howtoplaybutton.place(x = 140, y = 300)
        self.highscoresbutton.place(x = 150, y = 370)
        self.quitgamebutton.place(x = 160, y = 440)
        self.title_pic = self.canvas.create_image(240, 90, image = self.title_img)
        self.railgun_pic = self.canvas.create_image(240, 440, image = self.railgun_img)
        self.pa = self.canvas.create_text(370, 562, text = 'Developed by Xiangyu Chen\n          All rights reserved.', fill = 'white', font = ('Arial', 12))
    
    def start(self):
        if self.landmark:
            self.landmark = False
            self.startbutton.place_forget()
            self.settingsbutton.place_forget()
            self.howtoplaybutton.place_forget()
            self.highscoresbutton.place_forget()
            self.quitgamebutton.place_forget()
            self.canvas.delete(self.pa)
            self.canvas.delete(self.railgun_pic)
            self.canvas.delete(self.title_pic)
        self.pause.set(0)
        self.gameover = False
        self.t = 0
        self.stage = 1
        self.wave = 0
        self.score = 0
        self.canvas.itemconfig(self.health.r, state = 'normal')
        self.canvas.itemconfig(self.health.t, state = 'normal')
        self.canvas.itemconfig(self.health.tt, state = 'normal')
        self.sonic.shield = 0
        self.sonic.hp = 100
        self.sonic.status = 1
        self.sonic.weaponmode = 1
        self.sonic.x = 240
        self.sonic.y = 540
        self.canvas.delete(self.sonic.pic)
        self.canvas.delete(self.sonic.aos_pic)
        self.sonic.pic = self.canvas.create_image(240, 540, image = self.sonic.img)
        self.sonic.aos_pic = self.canvas.create_image(240, 550, image = self.sonic.aos_img)
        self.enemies.clear()
        self.eb.clear()
        self.mb.clear()
        self.p.clear()
        self.bu.clear()
        self.sb.clear()
        self.w.clear()
        self.f.clear()
        if self.boss.status:
            self.boss.clear()
        self.f.showup()

    def die(self):
        self.canvas.delete(self.sonic.pic)
        self.pause.set(1)
        self.goodwin = Toplevel()
        self.goodwin.title('You died!')
        self.goodwin.geometry('600x375')
        self.goodwin.iconbitmap('images\\sss_icon.ico')
        self.cccanvas = Canvas(self.goodwin, height = 375, width = 600)
        self.cccanvas.place(x = 0, y = 0)
        self.sss_img = PhotoImage(file = 'images\\sss.gif')
        self.sss_pic = self.cccanvas.create_image(300, 187, image = self.sss_img)
        self.uname = StringVar()
        self.eeentry = Entry(self.goodwin, textvariable = self.uname)
        self.eeentry.place(x = 230, y = 144)
        self.Nb = Button(self.goodwin, text = 'Confirm', command = self.newhighscore)
        self.Nb.place(x = 270, y = 174)
        self.eeentry.bind('<Return>', self.nh)
        self.goodwin.protocol('WM_DELETE_WINDOW', self.newhighscore)
        self.eeentry.focus_set()

    def mainmenu(self):
        self.gameover = True
        self.canvas.itemconfig(self.health.r, state = 'hidden')
        self.canvas.itemconfig(self.health.t, state = 'hidden')
        self.canvas.itemconfig(self.health.tt, state = 'hidden')
        self.f.status = 0
        self.canvas.delete(self.f.tt)
        self.enemies.clear()
        self.eb.clear()
        self.mb.clear()
        self.p.clear()
        self.bu.clear()
        self.sb.clear()
        self.w.clear()
        self.f.clear()
        self.canvas.itemconfig(self.sonic.aos_pic, state = 'hidden')
        if self.boss.status:
            self.boss.clear()
        if self.sonic.status:
            self.canvas.delete(self.sonic.pic)
            self.sonic.status = 0
        self.homepage()

    def nh(self, event):
        self.newhighscore()

    def newhighscore(self):
        if lstrip(self.uname.get()) != '':
            self.scoreboard.add(lstrip(rstrip(self.uname.get())) + ' ' + str(self.score))
            self.goodwin.destroy()
            if askokcancel('Play Again?', 'Do you want to have another try?'):
                self.start()
            else:
                self.scoreboard.landmark = False
                self.scoreboard.showup()
        else:
            showerror('Error', 'That\'s not a correct name.')
            self.eeentry.focus_set()

    def begin(self, event):
        self.start()

    def hsshow(self, event):
        self.scoreboard.showup()

    def howtoplay(self, event):
        self.he.showup()

    def controlInitialize(self, event):
        self.cs.initialize()

    def changeBackground(self, event):
        self.galaxy.change()

    def changePlane(self, event):
        self.sonic.change()

    def Pause(self, event):
        self.pause.set(1-self.pause.get())
        self.temppause = self.pause.get()

    def eventquit(self, event):
        self.quitcallback()

    def quitcallback(self):
        self.pause.set(1)
        if askokcancel('Quit', 'Do you really want to quit?'):
            with open('userdata.dat', 'w') as f:
                f.write(str(self.introduction.experience) + '\n' + self.scoreboard.data[0][0] + ' ' + str(self.scoreboard.data[0][1]) + '\n' + self.scoreboard.data[1][0] + ' ' + str(self.scoreboard.data[1][1]) + '\n' + self.scoreboard.data[2][0] + ' ' + str(self.scoreboard.data[2][1]) + '\n' + self.scoreboard.data[3][0] + ' ' + str(self.scoreboard.data[3][1]) + '\n'+self.scoreboard.data[4][0] + ' ' + str(self.scoreboard.data[4][1]))
            self.root.destroy()
        else:
            self.pause.set(0)

    def keysettings(self, event):
        self.cs.alter()

    def introduce(self, event):
        self.introduction.showup()

    def game(self):
        if not self.pause.get():
            self.galaxy.roll()
        if not self.pause.get() and not self.gameover:
            self.t += 1
            if self.sonic.shield>0 and self.f.status == 0 and self.w.s == 0:
                self.sonic.shield -= 1
            if self.enemies.n == 0 and self.boss.status == 0 and self.f.status == 0 and self.w.s == 0:
                self.wave += 1
                self.enemies.showup(self.wave)
            self.mb.upd()
            self.eb.upd()
            self.enemies.upd()
            if self.sonic.shield>0:
                self.canvas.itemconfig(self.sonic.aos_pic, state = 'normal')
            else:
                self.canvas.itemconfig(self.sonic.aos_pic, state = 'hidden')
            self.boss.upd()
            self.sb.upd()
            self.bu.upd()
            if self.t % 6 == 0 and self.f.status == 0 and self.w.s == 0:
                self.sonic.fire()
            self.p.upd()
            self.health.upd()
        if not self.pause.get() and not self.gameover:
            self.w.upd()
            self.f.upd()
        self.root.after(16, self.game)