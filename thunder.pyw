from Tkinter import *
from tkMessageBox import *
from string import *
from math import *
from random import *
def bulletspeed(n):
    x=5+n
    if x>15:
        x=15
    return x
def firerate(n):
    x=63-3*n
    if x<6:
        x=6
    return x
def hit_the_boss(x,y):
    if not (90<=x<=330 and 70<=y<=234):
        return False
    if y<=200:
        return True
    if 136<=x<=188 or 232<=x<=284:
        return False
    return True
def myCmp(x,y):
    if x[1]>y[1]:
        return -1
    elif x[1]<y[1]:
        return 1
    else:
        return 0
def doNothing(event):
    return None
def conditionalUpper(s):
    if len(s)==1 and 'a'<=s<='z':
        return upper(s)
    else:
        return s
def processed(s):
    if has_counterpart(s) or (s in '.0123456789+-*/;\''):
        return '<Key-'+s+'>'
    else:
        return '<'+s+'>'
def has_counterpart(s):
    if len(s)==1:
        return 'a'<=s<='z' or 'A'<=s<='Z'
    else:
        return False
def counterpart(s):
    if 'a'<=s<='z':
        return upper(s)
    elif 'A'<=s<='Z':
        return lower(s)
def hpcl(n):
    if n>=60:
        return 'green'
    elif n>=30:
        return 'orange'
    else:
        return 'red'
class Help:
    def __init__(self,master):
        self.master=master
    def showup(self):
        self.master.pause.set(1)
        self.order=1
        self.root=Toplevel()
        self.root.title('How to play')
        self.root.iconbitmap('images\\help.ico')
        self.root.geometry('400x300')
        self.root.protocol('WM_DELETE_WINDOW',self.halt)
        self.canvas=Canvas(self.root,height=300,width=400)
        self.canvas.place(x=0,y=0)
        self.img=[]
        for i in range(6):
            self.img.append(PhotoImage(file='images\\train'+str(i+1)+'.gif'))
        self.pic=self.canvas.create_image(200,150,image=self.img[0])
        self.ba=Button(self.root,text='Last',command=self.l)
        self.bb=Button(self.root,text='Back',command=self.halt)
        self.bc=Button(self.root,text='Next',command=self.n)
        self.bb.place(x=182,y=190)
        self.bc.place(x=340,y=140)
        self.root.focus_set()
    def l(self):
        if self.order==2:
            self.ba.place_forget()
        if self.order==6:
            self.bc.place(x=340,y=140)
        self.order-=1
        self.canvas.delete(self.pic)
        self.pic=self.canvas.create_image(200,150,image=self.img[self.order-1])
    def n(self):
        if self.order==1:
            self.ba.place(x=24,y=140)
        if self.order==5:
            self.bc.place_forget()
        self.order+=1
        self.canvas.delete(self.pic)
        self.pic=self.canvas.create_image(200,150,image=self.img[self.order-1])
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
class Info:
    def __init__(self,master,experience):
        self.experience=experience
        self.master=master
        if not self.experience:
            self.showup()
    def showup(self):
        self.master.pause.set(1)
        self.order=1
        self.root=Toplevel()
        self.root.title('Game Introduction')
        self.root.iconbitmap('images\\hawx.ico')
        self.root.geometry('400x300')
        self.root.protocol('WM_DELETE_WINDOW',self.halt)
        self.canvas=Canvas(self.root,height=300,width=400)
        self.canvas.place(x=0,y=0)
        self.img=[]
        for i in range(4):
            self.img.append(PhotoImage(file='images\\plot'+str(i+1)+'.gif'))
        self.pic=self.canvas.create_image(200,150,image=self.img[0])
        self.ba=Button(self.root,text='Last',command=self.l)
        self.bb=Button(self.root,text='Back',command=self.halt)
        self.bc=Button(self.root,text='Next',command=self.n)
        self.bb.place(x=182,y=250)
        self.bc.place(x=260,y=250)
        self.root.focus_set()
    def l(self):
        if self.order==2:
            self.ba.place_forget()
        if self.order==4:
            self.bc.place(x=260,y=250)
        self.order-=1
        self.canvas.delete(self.pic)
        self.pic=self.canvas.create_image(200,150,image=self.img[self.order-1])
    def n(self):
        if self.order==1:
            self.ba.place(x=104,y=250)
        if self.order==3:
            self.bc.place_forget()
        self.order+=1
        self.canvas.delete(self.pic)
        self.pic=self.canvas.create_image(200,150,image=self.img[self.order-1])
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
        if not self.experience:
            self.master.he.showup()
        self.experience=True
class HP:
    def __init__(self,master):
        self.master=master
        self.r=self.master.canvas.create_rectangle(25,20,225,60,fill='green',outline='green')
        self.t=self.master.canvas.create_text(75,40,text='HP:100',fill='white',font=('Arial',20,'bold'))
        self.tt=self.master.canvas.create_text(400,50,text='Score:\n 0',fill='cyan',font=('Arial',20,'normal'))
    def upd(self):
        self.master.canvas.coords(self.r,25,20,self.master.sonic.hp*2+24,60)
        self.master.canvas.itemconfig(self.r,fill=hpcl(self.master.sonic.hp),outline=hpcl(self.master.sonic.hp))
        self.master.canvas.itemconfig(self.t,text='HP:'+str(self.master.sonic.hp))
        self.master.canvas.itemconfig(self.tt,text='Score:\n '+str(self.master.score))
        if self.master.sonic.hp==0:
            self.master.canvas.itemconfig(self.r,state='hidden')
        self.master.canvas.lift(self.r)
        self.master.canvas.lift(self.t)
        self.master.canvas.lift(self.tt)
class warning:
    def __init__(self,master):
        self.master=master
        self.s=0
    def on(self):
        self.s=1
        self.t=120
        self.t1=self.master.canvas.create_text(240,300,text='   Boss\nWarning',fill='#FF0000',font=('Arial',48,'normal'))
        self.p=[]
        px=-60
        for i in range(10):
            px+=60
            self.p.append(self.master.canvas.create_polygon((px,0),(px+30,0),(px,80),(px-30,80),fill='red'))
            self.p.append(self.master.canvas.create_polygon((px,510),(px+30,510),(px,590),(px-30,590),fill='red'))
    def upd(self):
        if self.s==1:
            for i in self.p:
                self.master.canvas.lift(i)
            self.master.canvas.lift(self.t1)
            if self.master.pause.get()==0:
                self.t-=1
            if self.t==0:
                self.clear()
                self.master.boss.showup()
    def clear(self):
        if self.s==1:
            for i in self.p:
                self.master.canvas.delete(i)
                del i
            self.master.canvas.delete(self.t1)
            del self.t1
            del self.t
            self.s=0
class ControlSet:
    def __init__(self,master):
        try:
            f=open('controldata.dat','r')
        except:
            f=open('controldata.dat','w')
            f.write('w\ns\na\nd')
            f.close()
            f=open('controldata.dat','r')
        self.master=master
        self.up=replace(f.readline(),'\n','')
        self.down=replace(f.readline(),'\n','')
        self.left=replace(f.readline(),'\n','')
        self.right=replace(f.readline(),'\n','')
        f.close()
        self.UP=StringVar()
        self.UP.set('Up: '+conditionalUpper(self.up))
        self.DOWN=StringVar()
        self.DOWN.set('Down: '+conditionalUpper(self.down))
        self.LEFT=StringVar()
        self.LEFT.set('Left: '+conditionalUpper(self.left))
        self.RIGHT=StringVar()
        self.RIGHT.set('Right: '+conditionalUpper(self.right))
        self.toApply()
    def initialize(self):
        self.unapply()
        self.up='w'
        self.down='s'
        self.left='a'
        self.right='d'
        self.UP.set('Up: '+conditionalUpper(self.up))
        self.DOWN.set('Down: '+conditionalUpper(self.down))
        self.LEFT.set('Left: '+conditionalUpper(self.left))
        self.RIGHT.set('Right: '+conditionalUpper(self.right))
        f=open('controldata.dat','w')
        f.write('w\ns\na\nd')
        f.close()
        self.toApply()
    def toApply(self):
        self.master.root.bind(processed(self.up),self.master.sonic.up)
        self.master.root.bind(processed(self.left),self.master.sonic.left)
        self.master.root.bind(processed(self.down),self.master.sonic.down)
        self.master.root.bind(processed(self.right),self.master.sonic.right)
        if has_counterpart(self.up):
            self.master.root.bind(processed(counterpart(self.up)),self.master.sonic.up)
        if has_counterpart(self.left):
            self.master.root.bind(processed(counterpart(self.left)),self.master.sonic.left)
        if has_counterpart(self.down):
            self.master.root.bind(processed(counterpart(self.down)),self.master.sonic.down)
        if has_counterpart(self.right):
            self.master.root.bind(processed(counterpart(self.right)),self.master.sonic.right)
    def alter(self):
        self.cg=False
        self.tempup=self.up
        self.tempdown=self.down
        self.templeft=self.left
        self.tempright=self.right
        self.master.temppause=self.master.pause.get()
        self.master.pause.set(1)
        self.master.top=Toplevel()
        self.master.top.title('Set Keys')
        self.master.top.geometry('300x400')
        self.master.top.iconbitmap('images\\keysettings.ico')
        self.master.canvas2=Canvas(self.master.top,height=400,width=300,bg='white')
        self.master.canvas2.place(x=0,y=0)
        self.master.girl=PhotoImage(file='images\\showgirl.gif')
        self.master.showgirl=self.master.canvas2.create_image(150,200,image=self.master.girl)
        self.master.canvas2.create_rectangle(8,10,294,75,fill='#FF0000',width=0)
        self.master.canvas2.create_text(166,20,text='Click on the button of direction which',fill='#00FFFF',font=('Times',12,'bold'))
        self.master.canvas2.create_text(139,42,text='you want to change and then press the',fill='#00FFFF',font=('Times',12,'bold'))
        self.master.canvas2.create_text(131,64,text='corresponding key on the keyboard.',fill='#00FFFF',font=('Times',12,'bold'))
        self.buttonok=Button(self.master.top,text='Confirm',command=self.confirm1)
        self.buttonok.place(x=86,y=324)
        self.buttoncancel=Button(self.master.top,text='Cancel',command=self.cancel)
        self.buttoncancel.place(x=176,y=324)
        self.buttonUp=Button(self.master.top,textvariable=self.UP)
        self.buttonUp.config(command=self.buttonUp.focus_set)
        self.buttonUp.place(x=142-2*len(self.UP.get()),y=100)
        self.buttonUp.bind('<Key>',self.changeup)
        self.buttonLeft=Button(self.master.top,textvariable=self.LEFT)
        self.buttonLeft.config(command=self.buttonLeft.focus_set)
        self.buttonLeft.place(x=52-2*len(self.LEFT.get()),y=180)
        self.buttonLeft.bind('<Key>',self.changeleft)
        self.buttonDown=Button(self.master.top,textvariable=self.DOWN)
        self.buttonDown.config(command=self.buttonDown.focus_set)
        self.buttonDown.place(x=142-2*len(self.DOWN.get()),y=260)
        self.buttonDown.bind('<Key>',self.changedown)
        self.buttonRight=Button(self.master.top,textvariable=self.RIGHT)
        self.buttonRight.config(command=self.buttonRight.focus_set)
        self.buttonRight.place(x=232-2*len(self.RIGHT.get()),y=180)
        self.buttonRight.bind('<Key>',self.changeright)
        self.master.top.protocol('WM_DELETE_WINDOW',self.confirm2)
        self.master.top.focus_set()
    def confirm1(self):
        self.change()
        self.cancel()
    def confirm2(self):
        if self.cg:
            if askokcancel('Confirm','Do you want to save these changes?'):
                self.change()
        self.cancel()
    def cancel(self):
        self.master.top.destroy()
        self.master.pause.set(self.master.temppause)
    def unapply(self):
        self.master.root.bind(processed(self.up),doNothing)
        self.master.root.bind(processed(self.left),doNothing)
        self.master.root.bind(processed(self.down),doNothing)
        self.master.root.bind(processed(self.right),doNothing)
        if has_counterpart(self.up):
            self.master.root.bind(processed(counterpart(self.up)),doNothing)
        if has_counterpart(self.left):
            self.master.root.bind(processed(counterpart(self.left)),doNothing)
        if has_counterpart(self.down):
            self.master.root.bind(processed(counterpart(self.down)),doNothing)
        if has_counterpart(self.right):
            self.master.root.bind(processed(counterpart(self.right)),doNothing)
    def change(self):
        self.unapply()
        self.up=self.tempup
        self.down=self.tempdown
        self.left=self.templeft
        self.right=self.tempright
        self.UP.set('Up: '+conditionalUpper(self.up))
        self.DOWN.set('Down: '+conditionalUpper(self.down))
        self.LEFT.set('Left: '+conditionalUpper(self.left))
        self.RIGHT.set('Right: '+conditionalUpper(self.right))
        self.toApply()
        f=open('controldata.dat','w')
        f.write(self.up+'\n'+self.down+'\n'+self.left+'\n'+self.right)
        f.close()
    def changeup(self,event):
        if event.keysym not in ['F1','F2','F3','F4','F9','F10','F11','F12','1','2',self.tempdown,self.templeft,self.tempright]:
            self.cg=True
            self.buttonUp.place_forget()
            self.tempup=event.keysym
            self.UP.set('Up: '+conditionalUpper(self.tempup))
            self.buttonUp.place(x=142-2*len(self.UP.get()),y=100)
        else:
            showwarning('Sorry, you can\'t do this!','This key has been occupied.')
            self.buttonUp.focus_set()
    def changedown(self,event):
        if event.keysym not in ['F1','F2','F3','F4','F9','F10','F11','F12','1','2',self.tempup,self.templeft,self.tempright]:
            self.cg=True
            self.buttonDown.place_forget()
            self.tempdown=event.keysym
            self.DOWN.set('Down: '+conditionalUpper(self.tempdown))
            self.buttonDown.place(x=142-2*len(self.DOWN.get()),y=260)
        else:
            showwarning('Sorry, you can\'t do this!','This key has been occupied.')
            self.buttonDown.focus_set()
    def changeleft(self,event):
        if event.keysym not in ['F1','F2','F3','F4','F9','F10','F11','F12','1','2',self.tempdown,self.tempup,self.tempright]:
            self.cg=True
            self.buttonLeft.place_forget()
            self.templeft=event.keysym
            self.LEFT.set('Left: '+conditionalUpper(self.templeft))
            self.buttonLeft.place(x=52-2*len(self.LEFT.get()),y=180)
        else:
            showwarning('Sorry, you can\'t do this!','This key has been occupied.')
            self.buttonLeft.focus_set()
    def changeright(self,event):
        if event.keysym not in ['F1','F2','F3','F4','F9','F10','F11','F12','1','2',self.tempdown,self.templeft,self.tempup]:
            self.cg=True
            self.buttonRight.place_forget()
            self.tempright=event.keysym
            self.RIGHT.set('Right: '+conditionalUpper(self.tempright))
            self.buttonRight.place(x=232-2*len(self.RIGHT.get()),y=180)
        else:
            showwarning('Sorry, you can\'t do this!','This key has been occupied.')
            self.buttonRight.focus_set()
class Background:
    def __init__(self,master):
        self.x=240
        self.y=-900
        self.number=1
        self.master=master
        self.img=PhotoImage(file='images\\bg1.gif')
        self.pic=self.master.canvas.create_image(self.x,self.y,image=self.img)
        self.master.canvas.lower(self.pic)
    def roll(self):
        self.master.canvas.move(self.pic,0,1)
        self.y+=1
        if self.y==1500:
            self.y=-900
            self.master.canvas.move(self.pic,0,-2400)
    def change(self):
        self.number=self.number%3+1
        self.img=PhotoImage(file='images\\bg'+str(self.number)+'.gif')
        self.pic=self.master.canvas.create_image(self.x,self.y,image=self.img)
        self.master.canvas.lower(self.pic)
class myPlane:
    def __init__(self,master):
        self.master=master
        self.aos_img=PhotoImage(file='images\\aos.gif')
        self.aos_pic=self.master.canvas.create_image(240,550,image=self.aos_img)
        self.master.canvas.itemconfig(self.aos_pic,state='hidden')
        self.status=1
        self.shield=0
        self.hp=100
        self.weaponmode=1
        self.step=12
        self.x=240
        self.y=540
        self.number=1
        self.img=PhotoImage(file='images\\plane1.gif')
        self.pic=self.master.canvas.create_image(self.x,self.y,image=self.img)
    def change(self):
        self.number=self.number%3+1
        self.img=PhotoImage(file='images\\plane'+str(self.number)+'.gif')
        self.pic=self.master.canvas.create_image(self.x,self.y,image=self.img)
        if self.master.gameover or not self.status:
            self.master.canvas.itemconfig(self.pic,state='hidden')
    def fire(self):
        if self.weaponmode==1:
            self.master.mb.new(self.x,self.y-20)
        elif self.weaponmode==2:
            self.master.mb.new(self.x-15,self.y-20)
            self.master.mb.new(self.x+15,self.y-20)
        elif self.weaponmode==3:
            self.master.mb.new(self.x-15,self.y-15)
            self.master.mb.new(self.x,self.y-25)
            self.master.mb.new(self.x+15,self.y-15)
    def scaleX(self):
        if self.number<3:
            return 33
        else:
            return 44
    def scaleY(self):
        if self.number<3:
            return 41
        else:
            return 33
    def left(self,event):
        if self.x-self.scaleX()>self.step and not self.master.pause.get() and not self.master.gameover:
            self.x-=self.step
            self.master.canvas.move(self.pic,-self.step,0)
            self.master.canvas.move(self.aos_pic,-self.step,0)
    def right(self,event):
        if self.x+self.scaleX()<480-self.step and not self.master.pause.get() and not self.master.gameover:
            self.x+=self.step
            self.master.canvas.move(self.pic,self.step,0)
            self.master.canvas.move(self.aos_pic,self.step,0)
    def up(self,event):
        if self.y-self.scaleY()>self.step and not self.master.pause.get() and not self.master.gameover:
            self.y-=self.step
            self.master.canvas.move(self.pic,0,-self.step)
            self.master.canvas.move(self.aos_pic,0,-self.step)
    def down(self,event):
        if self.y+self.scaleY()<588-self.step and not self.master.pause.get() and not self.master.gameover:
            self.y+=self.step
            self.master.canvas.move(self.pic,0,self.step)
            self.master.canvas.move(self.aos_pic,0,self.step)
class myMenu:
    def __init__(self,master):
        self.master=master
        self.mainmenu=Menu(self.master.root)
        self.master.root.config(menu=self.mainmenu)
        self.gamemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label='Game',menu=self.gamemenu)
        self.gamemenu.add_checkbutton(label='Pause           F1',variable=self.master.pause)
        self.gamemenu.add_command(label='Restart         F2',command=self.master.start)
        self.gamemenu.add_command(label='Main menu',command=self.master.mainmenu)
        self.gamemenu.add_separator()
        self.gamemenu.add_command(label='Exit Game   F12',command=self.master.quitcallback)
        self.controlmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label='Control',menu=self.controlmenu)
        self.controlmenu.add_command(label='Change Background  Num 1',command=self.master.galaxy.change)
        self.controlmenu.add_command(label='Change Plane            Num 2',command=self.master.sonic.change)
        self.controlmenu.add_command(label='Key Settings                    F3',command=self.master.cs.alter)
        self.controlmenu.add_command(label='Key Settings Initialize       F4',command=self.master.cs.initialize)
        self.helpmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label='Help',menu=self.helpmenu)
        self.helpmenu.add_command(label='Introductions       F9',command=self.master.introduction.showup)
        self.helpmenu.add_command(label='How to play        F10',command=self.master.he.showup)
        self.helpmenu.add_command(label='Highest scores    F11',command=self.master.scoreboard.showup)
class Linked_List:
    def __init__(self,x,y,master,hp=0,dx=0,dy=0):
        self.hp=hp
        self.t=0
        self.master=master
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self._next=False
        self._last=False
    def add(self,x,y,hp=0,dx=0,dy=0):
        p=self
        while p._next:
            p=p.next
        p.next=Linked_List(x,y,self.master,hp,dx,dy)
        p.next._last=True
        p._next=True
        p.next.last=p
        p=p.next
        p.pic=self.master.master.canvas.create_image(p.x,p.y,image=self.master.img)
def dlt(p):
    p.master.master.canvas.delete(p.pic)
    if not p._next:
        p.last._next=False
    else:
        p.last.next=p.next
        p.next.last=p.last
    del p
class Enemies:
    def __init__(self,master):
        self.n=0
        self.master=master
        self.img=PhotoImage(file='images\\enemy1.gif')
        self.data=Linked_List(-100,-100,self)
    def new(self,x,y):
        self.n+=1
        self.data.add(x,y,50*self.master.stage+50)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def up(self):
        p=self.data
        while p._next:
            p=p.next
            self.master.canvas.lift(p.pic)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def upd(self):
        p=self.data
        while p._next:
            p=p.next
            p.t+=1
            if p.t%firerate(self.master.stage)==firerate(self.master.stage)-1:
                self.master.eb.new(p.x,p.y)
                self.up()
    def showup(self,n):
        if n==1:
            self.new(160,120)
        elif n==2:
            self.new(120,160)
            self.new(360,160)
        elif n==3:
            self.new(240,200)
            self.new(160,140)
            self.new(320,140)
        elif n==4:
            self.new(240,100)
            self.new(240,220)
            self.new(120,160)
            self.new(360,160)
        elif n==5:
            self.new(240,280)
            self.new(159,221)
            self.new(321,221)
            self.new(190,86)
            self.new(290,86)
        elif n==6:
            self.new(240,186)
            self.new(300,290)
            self.new(180,290)
            self.new(120,186)
            self.new(360,186)
            self.new(300,82)
            self.new(180,82)
        elif n==7:
            self.master.w.on()
    def clear(self):
        p=self.data
        while p._next:
            dlt(p.next)
        self.n=0
class Blowups:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\bomb1.gif')
        self.data=Linked_List(-100,-100,self)
    def new(self,x,y):
        self.data.add(x,y)
    def upd(self):
        p=self.data
        while p._next:
            p=p.next
            p.t+=1
            if p.t==6:
                #p.master.master.canvas.delete(p.pic)
                p=p.last
                dlt(p.next)
            else:
                p.master.master.canvas.lift(p.pic)
    def clear(self):
        p=self.data
        while p._next:
            dlt(p.next)
class smallBlowups:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\bomb2.gif')
        self.data=Linked_List(-100,-100,self)
    def new(self,x,y):
        self.data.add(x,y)
    def upd(self):
        p=self.data
        while p._next:
            p=p.next
            p.t+=1
            if p.t==6:
                #p.master.master.canvas.delete(p.pic)
                p=p.last
                dlt(p.next)
            else:
                p.master.master.canvas.lift(p.pic)
    def clear(self):
        p=self.data
        while p._next:
            dlt(p.next)
def kill(p):
    p.master.master.canvas.delete(p.pic)
    p.master.master.bu.new(p.x,p.y)
    p.master.n-=1
    dlt(p)
class enemyBullets:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\enemybullet1.gif')
        self.data=Linked_List(-100,-100,self)
    def new(self,x,y):
        s=sqrt((self.master.sonic.x-x)**2+(self.master.sonic.y-y)**2)
        dx=int(round((self.master.sonic.x-x)*bulletspeed(self.master.stage)/(s+0.01)))
        dy=int(round((self.master.sonic.y-y)*bulletspeed(self.master.stage)/(s+0.01)))
        self.data.add(x,y,0,dx,dy)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def upd(self):
        p=self.data
        while p._next:
            p=p.next
            p.x+=p.dx
            p.y+=p.dy
            self.master.canvas.move(p.pic,p.dx,p.dy)
            if p.y<-40 or p.y>800 or p.x<-20 or p.x>500:
                p=p.last
                dlt(p.next)
            if (p.x-self.master.sonic.x)**2+(p.y-self.master.sonic.y)**2<401:
                self.master.sb.new(p.x,p.y)
                if self.master.sonic.shield==0:
                    self.master.sonic.hp-=10
                    self.master.score-=100
                    self.master.sonic.shield=10
                    if self.master.sonic.weaponmode>1:
                        self.master.sonic.weaponmode-=1
                else:
                    self.master.sonic.shield-=10
                    if self.master.sonic.shield<0:
                        self.master.sonic.shield=0
                self.master.canvas.delete(p.pic)
                if not p._next:
                    p.last._next=False
                    p=p.last
                    del p.next
                else:
                    p.last.next=p.next
                    p=p.last
                    del p.next.last
                    p.next.last=p
                if self.master.sonic.hp<=0 and not self.master.gameover:
                    self.master.gameover=True
                    self.master.sonic.hp=0
                    self.master.bu.new(self.master.sonic.x,self.master.sonic.y)
                    self.master.sonic.status=0
                    self.master.die()
    def clear(self):
        p=self.data
        while p._next:
            dlt(p.next)
class myBullets:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\mybullet.gif')
        self.data=Linked_List(-100,-100,self)
    def new(self,x,y):
        self.data.add(x,y)
        self.master.canvas.lift(self.master.sonic.pic)
        self.master.canvas.lift(self.master.sonic.aos_pic)
    def upd(self):
        p=self.data
        while p._next:
            p=p.next
            p.y-=6
            self.master.canvas.move(p.pic,0,-6)
            if p.y<-40:
                p=p.last
                dlt(p.next)
            if self.master.boss.status==0:
                q=self.master.enemies.data
                mark=True
                while q._next and mark:
                    q=q.next
                    if (p.x-q.x)**2+(p.y-q.y)**2<401:
                        q.hp-=25
                        mark=False
                        self.master.sb.new(p.x,p.y)
                        self.master.score+=25
                        p=p.last
                        dlt(p.next)
                        if q.hp<=0:
                            kill(q)
                            if randrange(6)==0:
                                self.master.p.add(q.x,q.y)
            else:
                if hit_the_boss(p.x,p.y):
                    self.master.sb.new(p.x,p.y)
                    self.master.score+=25
                    p=p.last
                    dlt(p.next)
                    self.master.boss.hp-=25
                    if self.master.boss.hp<=0:
                        self.master.boss.vanish()
    def clear(self):
        p=self.data
        while p._next:
            dlt(p.next)
class Scores:
    def __init__(self,master):
        self.landmark=True
        self.master=master
        self.data=[]
    def add(self,s):
        s=split(s)
        a=join(s[:-1],' ')
        self.data.append([a,int(s[-1])])
        self.data.sort(myCmp)
        if len(self.data)>5:
            del self.data[5]
    def showup(self):
        self.master.pause.set(1)
        self.root=Toplevel()
        self.root.title('Highest Scores')
        self.root.geometry('300x400')
        self.root.iconbitmap('images\\hs.ico')
        self.canvas=Canvas(self.root,height=400,width=300)
        self.canvas.place(x=0,y=0)
        self.img=PhotoImage(file='images\\general.gif')
        self.pic=self.canvas.create_image(150,200,image=self.img)
        for i in range(5):
            self.canvas.create_text(150,120+50*i,text=str(i+1)+'. '+self.data[i][0]+'  '+str(self.data[i][1]),fill='blue',font=('Arial',20))
        Button(self.root,text='Back',command=self.halt).place(x=140,y=350)
        self.root.protocol('WM_DELETE_WINDOW',self.halt)
        self.root.focus_set()
    def halt(self):
        self.root.destroy()
        self.master.pause.set(0)
        if not self.landmark:
            self.landmark=True
            self.master.homepage()
            self.master.canvas.itemconfig(self.master.health.r,state='hidden')
            self.master.canvas.itemconfig(self.master.health.t,state='hidden')
            self.master.canvas.itemconfig(self.master.health.tt,state='hidden')
            self.master.f.status=0
            self.master.canvas.delete(self.master.f.tt)
            self.master.enemies.clear()
            self.master.eb.clear()
            self.master.mb.clear()
            self.master.p.clear()
            self.master.canvas.itemconfig(self.master.sonic.aos_pic,state='hidden')
            self.master.bu.clear()
            self.master.sb.clear()
            if self.master.boss.status:
                self.master.boss.clear()
class Flag:
    def __init__(self,master):
        self.master=master
        self.status=0
    def showup(self):
        self.master.eb.clear()
        self.t=0
        self.status=1
        self.tt=self.master.canvas.create_text(240,300,text='Stage '+str(self.master.stage),fill='#FF9900',font=('Arial',42))
    def upd(self):
        self.t+=1
        if self.t==60:
            self.master.canvas.itemconfig(self.tt,text='Start')
        elif self.t==90:
            self.clear()
    def clear(self):
        if self.status==1:
            self.status=0
            self.master.canvas.delete(self.tt)
class Boss:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\ashroller.gif')
        self.status=0
        self.hp=1000
        self.lim=360
        self.lazer_img1=PhotoImage(file='images\\lazer1.gif')
        self.lazer_img2=PhotoImage(file='images\\lazer2.gif')
        self.lazer_img3=PhotoImage(file='images\\lazer3.gif')
        self.mark=[0,0,0]
        self.lazer_status=0
        self.hpBar=self.master.canvas.create_rectangle(40,70,440,75,width=0,outline='',fill='red')
        self.hpbar=self.master.canvas.create_rectangle(40,70,440,75,width=1,outline='white',fill='')
        self.master.canvas.itemconfig(self.hpbar,state='hidden')
        self.master.canvas.itemconfig(self.hpBar,state='hidden')
    def showup(self):
        self.pic=self.master.canvas.create_image(240,160,image=self.img)
        self.master.canvas.itemconfig(self.hpbar,state='normal')
        self.master.canvas.itemconfig(self.hpBar,state='normal')
        self.master.p.add(240,224)
        self.t=0
        self.status=1
    def vanish(self):
        self.lazer_status=0
        self.master.bu.new(240,224)
        self.master.bu.new(180,224)
        self.master.bu.new(3000,224)
        self.master.bu.new(307,200)
        self.master.bu.new(113,200)
        self.master.bu.new(162,150)
        self.master.bu.new(258,150)
        self.master.bu.new(240,150)
        self.master.bu.new(180,150)
        self.master.bu.new(300,150)
        self.master.bu.new(162,100)
        self.master.bu.new(258,100)
        self.master.bu.new(240,100)
        self.master.bu.new(180,100)
        self.master.bu.new(300,100)
        self.master.p.add(240,224)
        self.clear()
        self.mark=[0,0,0]
        self.hp=self.master.stage*500+1000
        self.lim-=30
        if self.lim<120:
            self.lim=120
        self.master.eb.clear()
        self.master.stage+=1
        self.master.wave=0
        self.master.f.showup()
    def fire(self):
        self.t+=1
        if self.t%self.lim==10:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.866)),int(round(bulletspeed(self.master.stage)*0.5)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.866)),int(round(bulletspeed(self.master.stage)*0.5)))
        elif self.t%self.lim==20:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.766)),int(round(bulletspeed(self.master.stage)*0.642)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.766)),int(round(bulletspeed(self.master.stage)*0.642)))
        elif self.t%self.lim==30:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.642)),int(round(bulletspeed(self.master.stage)*0.766)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.642)),int(round(bulletspeed(self.master.stage)*0.766)))
        elif self.t%self.lim==40:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.5)),int(round(bulletspeed(self.master.stage)*0.866)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.5)),int(round(bulletspeed(self.master.stage)*0.866)))
        elif self.t%self.lim==50:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.342)),int(round(bulletspeed(self.master.stage)*0.939)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.342)),int(round(bulletspeed(self.master.stage)*0.939)))
        elif self.t%self.lim==60:
            self.master.eb.data.add(328,235,0,int(round(bulletspeed(self.master.stage)*0.174)),int(round(bulletspeed(self.master.stage)*0.984)))
            self.master.eb.data.add(152,235,0,-int(round(bulletspeed(self.master.stage)*0.174)),int(round(bulletspeed(self.master.stage)*0.984)))
        elif self.t%self.lim==70:
            self.master.eb.data.add(328,235,0,0,bulletspeed(self.master.stage))
            self.master.eb.data.add(152,235,0,0,bulletspeed(self.master.stage))
        elif self.t%self.lim==80:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.174)),int(round(bulletspeed(self.master.stage)*0.984)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.174)),int(round(bulletspeed(self.master.stage)*0.984)))
        elif self.t%self.lim==90:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.342)),int(round(bulletspeed(self.master.stage)*0.939)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.342)),int(round(bulletspeed(self.master.stage)*0.939)))
        elif self.t%self.lim==100:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.5)),int(round(bulletspeed(self.master.stage)*0.866)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.5)),int(round(bulletspeed(self.master.stage)*0.866)))
        elif self.t%self.lim==110:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.642)),int(round(bulletspeed(self.master.stage)*0.766)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.642)),int(round(bulletspeed(self.master.stage)*0.766)))
        elif self.t%self.lim==120:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.766)),int(round(bulletspeed(self.master.stage)*0.642)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.766)),int(round(bulletspeed(self.master.stage)*0.642)))
        if self.t%self.lim==130:
            self.master.eb.data.add(328,235,0,-int(round(bulletspeed(self.master.stage)*0.866)),int(round(bulletspeed(self.master.stage)*0.5)))
            self.master.eb.data.add(152,235,0,int(round(bulletspeed(self.master.stage)*0.866)),int(round(bulletspeed(self.master.stage)*0.5)))
        if (self.t%self.lim)%firerate(self.master.stage)==5:
            self.master.eb.new(240,224)
        if (self.lim-self.t)%self.lim==121:
            self.l1=self.master.canvas.create_image(240,224,image=self.lazer_img1)
            self.mark[0]=1
            self.master.canvas.lift(self.pic)
        elif (self.lim-self.t)%self.lim==101:
            self.master.canvas.delete(self.l1)
            self.l2=self.master.canvas.create_image(240,243,image=self.lazer_img2)
            self.mark[0]=0
            self.mark[1]=1
            self.master.canvas.lift(self.pic)
        elif (self.lim-self.t)%self.lim==81:
            self.master.canvas.delete(self.l2)
            self.l3=self.master.canvas.create_image(240,392,image=self.lazer_img3)
            self.mark[1]=0
            self.mark[2]=1
            self.lazer_status=1
        elif (self.lim-self.t)%self.lim==21:
            self.master.canvas.delete(self.l3)
            self.mark[2]=0
            self.lazer_status=0
    def upd(self):
        if self.status:
            self.fire()
            if self.lazer_status:
                if self.master.sonic.y>84 and 180<self.master.sonic.x<300:
                    if self.master.sonic.shield==0:
                        self.master.sonic.hp-=self.master.stage
                        self.master.score-=10*self.master.stage
                        if self.master.sonic.hp<=0 and not self.master.gameover:
                            self.master.gameover=True
                            self.master.sonic.hp=0
                            self.master.sonic.status=0
                            self.master.bu.new(self.master.sonic.x,self.master.sonic.y)
                            self.master.die()
                        else:
                            self.master.sonic.shield-=self.master.stage
                            if self.master.sonic.shield<0:
                                self.master.sonic.shield=0
            if self.mark[0]:
                self.master.canvas.lift(self.l1)
            if self.mark[1]:
                self.master.canvas.lift(self.l2)
            if self.mark[2]:
                self.master.canvas.lift(self.l3)
            self.master.canvas.lift(self.pic)
            self.master.canvas.coords(self.hpBar,40,70,40+int(round(400.0/(self.master.stage*500+500)*self.hp)),75)
            self.master.canvas.lift(self.hpBar)
            self.master.canvas.lift(self.hpbar)
    def clear(self):
        if self.status:
            self.master.canvas.delete(self.pic)
            self.master.canvas.itemconfig(self.hpbar,state='hidden')
            self.master.canvas.itemconfig(self.hpBar,state='hidden')
            self.status=0
            if self.mark[0]:
                self.master.canvas.delete(self.l1)
            if self.mark[1]:
                self.master.canvas.delete(self.l2)
            if self.mark[2]:
                self.master.canvas.delete(self.l3)
def nd(n,x):
    if n==1 or n==3:
        return (x+2)%4
    elif n==2:
        return x+1
    elif n==4:
        return x-1
class pcg:
    def __init__(self,x,y,direction,master):
        self.x=x
        self.y=y
        self.direction=direction
        self.master=master
        self.pic=self.master.master.canvas.create_image(self.x,self.y,image=self.master.img)
    def upd(self):
        if 20>self.x+dX[self.direction]:
            self.direction=nd(2,self.direction)
        elif self.x+dX[self.direction]>460:
            self.direction=nd(4,self.direction)
        self.x+=dX[self.direction]
        if 20>self.y+dY[self.direction]:
            self.direction=nd(1,self.direction)
        elif self.y+dY[self.direction]>590:
            self.direction=nd(3,self.direction)
        self.y+=dY[self.direction]
        self.master.master.canvas.move(self.pic,dX[self.direction],dY[self.direction])
class Packages:
    def __init__(self,master):
        self.master=master
        self.img=PhotoImage(file='images\\package.gif')
        self.data=[]
        self.length=0
    def clear(self):
        for i in self.data:
            self.master.canvas.delete(i.pic)
        del self.data
        self.data=[]
        self.length=0
    def add(self,x,y):
        self.data.append(pcg(x,y,randint(2,3),self))
        self.length+=1
    def upd(self):
        x=[]
        for j in range(self.length):
            i=self.data[j]
            i.upd()
            if (i.x-self.master.sonic.x)**2+(i.y-self.master.sonic.y)**2<2000:
                if self.master.sonic.hp<120:
                    self.master.sonic.hp+=25
                    if self.master.sonic.hp>120:
                        self.master.sonic.hp=120
                elif self.master.sonic.weaponmode<3:
                    self.master.sonic.weaponmode+=1
                else:
                    self.master.sonic.shield+=240
                x=[j]+x
                self.master.score+=100
        self.length-=len(x)
        for i in x:
            self.master.canvas.delete(self.data[i].pic)
            del self.data[i]
        if not self.master.boss.status:
            for i in self.data:
                self.master.canvas.lift(i.pic)
            self.master.enemies.up()
class Interface:
    def __init__(self):
        self.gameover=True
        self.t=0
        self.stage=1
        self.wave=0
        self.score=0
        self.root=Tk()
        self.root.title('Thunder')
        self.root.geometry('480x610')
        self.root.iconbitmap('images\\thunder.ico')
        self.pause=IntVar()
        self.canvas=Canvas(self.root,height=600,width=480,bg='white')
        self.canvas.place(x=0,y=0)
        self.galaxy=Background(self)
        self.mb=myBullets(self)
        self.enemies=Enemies(self)
        self.boss=Boss(self)
        self.eb=enemyBullets(self)
        self.sonic=myPlane(self)
        self.canvas.itemconfig(self.sonic.pic,state='hidden')
        self.sb=smallBlowups(self)
        self.bu=Blowups(self)
        self.w=warning(self)
        self.f=Flag(self)
        self.health=HP(self)
        self.p=Packages(self)
        self.canvas.itemconfig(self.health.r,state='hidden')
        self.canvas.itemconfig(self.health.t,state='hidden')
        self.canvas.itemconfig(self.health.tt,state='hidden')
        self.he=Help(self)
        try:
            f=open('userdata.dat','r')
        except:
            f=open('userdata.dat','w')
            f.write('False\nPython 0\nPascal 0\nCauchy 0\nTom 0\nJerry 0')
            f.close()
            f=open('userdata.dat','r')
        self.introduction=Info(self,eval(f.readline()))
        self.scoreboard=Scores(self)
        for i in range(5):
            self.scoreboard.add(f.readline())
        f.close()
        self.landmark=True
        self.cs=ControlSet(self)
        self.menu=myMenu(self)
        self.startgif=PhotoImage(file='images\\startbutton.gif')
        self.startbutton=Button(self.root,image=self.startgif,bd=-2,relief='flat',command=self.start)
        self.settingsgif=PhotoImage(file='images\\settingsbutton.gif')
        self.settingsbutton=Button(self.root,image=self.settingsgif,bd=-2,relief='flat',command=self.cs.alter)
        self.howtoplaygif=PhotoImage(file='images\\howtoplaybutton.gif')
        self.howtoplaybutton=Button(self.root,image=self.howtoplaygif,bd=-2,relief='flat',command=self.he.showup)
        self.highscoresgif=PhotoImage(file='images\\highscoresbutton.gif')
        self.highscoresbutton=Button(self.root,image=self.highscoresgif,bd=-2,relief='flat',command=self.scoreboard.showup)
        self.quitgamegif=PhotoImage(file='images\\quitgamebutton.gif')
        self.quitgamebutton=Button(self.root,image=self.quitgamegif,bd=-2,relief='flat',command=self.quitcallback)
        self.title_img=PhotoImage(file='images\\title.gif')
        self.railgun_img=PhotoImage(file='images\\bilibili.gif')
        self.homepage()
        self.root.protocol('WM_DELETE_WINDOW',self.quitcallback)
        self.root.bind('<F1>',self.Pause)
        self.root.bind('<F12>',self.eventquit)
        self.root.bind('<Key-1>',self.changeBackground)
        self.root.bind('<Key-2>',self.changePlane)
        self.root.bind('<F3>',self.keysettings)
        self.root.bind('<F4>',self.controlInitialize)
        self.root.bind('<F9>',self.introduce)
        self.root.bind('<F10>',self.howtoplay)
        self.root.bind('<F11>',self.hsshow)
        self.root.bind('<F2>',self.begin)
        self.root.after(16,self.game)
        self.root.mainloop()
    def homepage(self):
        self.landmark=True
        self.startbutton.place(x=180,y=160)
        self.settingsbutton.place(x=172,y=230)
        self.howtoplaybutton.place(x=140,y=300)
        self.highscoresbutton.place(x=150,y=370)
        self.quitgamebutton.place(x=160,y=440)
        self.title_pic=self.canvas.create_image(240,90,image=self.title_img)
        self.railgun_pic=self.canvas.create_image(240,440,image=self.railgun_img)
        self.pa=self.canvas.create_text(370,562,text='Developed by Chen Xiangyu\n          All rights reserved.',fill='white',font=('Arial',12))
    def start(self):
        if self.landmark:
            self.landmark=False
            self.startbutton.place_forget()
            self.settingsbutton.place_forget()
            self.howtoplaybutton.place_forget()
            self.highscoresbutton.place_forget()
            self.quitgamebutton.place_forget()
            self.canvas.delete(self.pa)
            self.canvas.delete(self.railgun_pic)
            self.canvas.delete(self.title_pic)
        self.pause.set(0)
        self.gameover=False
        self.t=0
        self.stage=1
        self.wave=0
        self.score=0
        self.canvas.itemconfig(self.health.r,state='normal')
        self.canvas.itemconfig(self.health.t,state='normal')
        self.canvas.itemconfig(self.health.tt,state='normal')
        self.sonic.shield=0
        self.sonic.hp=100
        self.sonic.status=1
        self.sonic.weaponmode=1
        self.sonic.x=240
        self.sonic.y=540
        self.canvas.delete(self.sonic.pic)
        self.canvas.delete(self.sonic.aos_pic)
        self.sonic.pic=self.canvas.create_image(240,540,image=self.sonic.img)
        self.sonic.aos_pic=self.canvas.create_image(240,550,image=self.sonic.aos_img)
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
        self.goodwin=Toplevel()
        self.goodwin.title('You died!')
        self.goodwin.geometry('600x375')
        self.goodwin.iconbitmap('images\\sss_icon.ico')
        self.cccanvas=Canvas(self.goodwin,height=375,width=600)
        self.cccanvas.place(x=0,y=0)
        self.sss_img=PhotoImage(file='images\\sss.gif')
        self.sss_pic=self.cccanvas.create_image(300,187,image=self.sss_img)
        self.uname=StringVar()
        self.eeentry=Entry(self.goodwin,textvariable=self.uname)
        self.eeentry.place(x=230,y=144)
        self.Nb=Button(self.goodwin,text='Confirm',command=self.newhighscore)
        self.Nb.place(x=270,y=174)
        self.eeentry.bind('<Return>',self.nh)
        self.goodwin.protocol('WM_DELETE_WINDOW',self.newhighscore)
        self.eeentry.focus_set()
    def mainmenu(self):
        self.gameover=True
        self.canvas.itemconfig(self.health.r,state='hidden')
        self.canvas.itemconfig(self.health.t,state='hidden')
        self.canvas.itemconfig(self.health.tt,state='hidden')
        self.f.status=0
        self.canvas.delete(self.f.tt)
        self.enemies.clear()
        self.eb.clear()
        self.mb.clear()
        self.p.clear()
        self.bu.clear()
        self.sb.clear()
        self.w.clear()
        self.f.clear()
        self.canvas.itemconfig(self.sonic.aos_pic,state='hidden')
        if self.boss.status:
            self.boss.clear()
        if self.sonic.status:
            self.canvas.delete(self.sonic.pic)
            self.sonic.status=0
        self.homepage()
    def nh(self,event):
        self.newhighscore()
    def newhighscore(self):
        if lstrip(self.uname.get())<>'':
            self.scoreboard.add(lstrip(rstrip(self.uname.get()))+' '+str(self.score))
            self.goodwin.destroy()
            if askokcancel('Play Again?','Do you want to have another try?'):
                self.start()
            else:
                self.scoreboard.landmark=False
                self.scoreboard.showup()
        else:
            showerror('Error','That\'s not a correct name.')
            self.eeentry.focus_set()
    def begin(self,event):
        self.start()
    def hsshow(self,event):
        self.scoreboard.showup()
    def howtoplay(self,event):
        self.he.showup()
    def controlInitialize(self,event):
        self.cs.initialize()
    def changeBackground(self,event):
        self.galaxy.change()
    def changePlane(self,event):
        self.sonic.change()
    def Pause(self,event):
        self.pause.set(1-self.pause.get())
        self.temppause=self.pause.get()
    def eventquit(self,event):
        self.quitcallback()
    def quitcallback(self):
        self.pause.set(1)
        if askokcancel('Quit','Do you really want to quit?'):
            f=open('userdata.dat','w')
            f.write(str(self.introduction.experience)+'\n'+self.scoreboard.data[0][0]+' '+str(self.scoreboard.data[0][1])+'\n'+self.scoreboard.data[1][0]+' '+str(self.scoreboard.data[1][1])+'\n'+self.scoreboard.data[2][0]+' '+str(self.scoreboard.data[2][1])+'\n'+self.scoreboard.data[3][0]+' '+str(self.scoreboard.data[3][1])+'\n'+self.scoreboard.data[4][0]+' '+str(self.scoreboard.data[4][1]))
            f.close()
            self.root.destroy()
        else:
            self.pause.set(0)
    def keysettings(self,event):
        self.cs.alter()
    def introduce(self,event):
        self.introduction.showup()
    def game(self):
        if not self.pause.get():
            self.galaxy.roll()
        if not self.pause.get() and not self.gameover:
            self.t+=1
            if self.sonic.shield>0 and self.f.status==0 and self.w.s==0:
                self.sonic.shield-=1
            if self.enemies.n==0 and self.boss.status==0 and self.f.status==0 and self.w.s==0:
                self.wave+=1
                self.enemies.showup(self.wave)
            self.mb.upd()
            self.eb.upd()
            self.enemies.upd()
            if self.sonic.shield>0:
                self.canvas.itemconfig(self.sonic.aos_pic,state='normal')
            else:
                self.canvas.itemconfig(self.sonic.aos_pic,state='hidden')
            self.boss.upd()
            self.sb.upd()
            self.bu.upd()
            if self.t%6==0 and self.f.status==0 and self.w.s==0:
                self.sonic.fire()
            self.p.upd()
            self.health.upd()
        if not self.pause.get() and not self.gameover:
            self.w.upd()
            self.f.upd()
        self.root.after(16,self.game)
dX=[-3,3,-3,3]
dY=[-3,-3,3,3]
win=Interface()
