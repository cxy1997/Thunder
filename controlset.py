from Tkinter import Toplevel, Canvas, PhotoImage, Button, StringVar
from tkMessageBox import showwarning
from string import replace
from utils import conditionalUpper, processed, has_counterpart, counterpart, doNothing

class ControlSet:
    def __init__(self, master):
        try:
            f = open('controldata.dat', 'r')
        except:
            f = open('controldata.dat', 'w')
            f.write('w\ns\na\nd')
            f.close()
            f = open('controldata.dat', 'r')
        self.master = master
        self.up = replace(f.readline(), '\n', '')
        self.down = replace(f.readline(), '\n', '')
        self.left = replace(f.readline(), '\n', '')
        self.right = replace(f.readline(), '\n', '')
        f.close()
        self.UP = StringVar()
        self.UP.set('Up: ' + conditionalUpper(self.up))
        self.DOWN = StringVar()
        self.DOWN.set('Down: ' + conditionalUpper(self.down))
        self.LEFT = StringVar()
        self.LEFT.set('Left: ' + conditionalUpper(self.left))
        self.RIGHT = StringVar()
        self.RIGHT.set('Right: ' + conditionalUpper(self.right))
        self.toApply()

    def initialize(self):
        self.unapply()
        self.up = 'w'
        self.down = 's'
        self.left = 'a'
        self.right = 'd'
        self.UP.set('Up: ' + conditionalUpper(self.up))
        self.DOWN.set('Down: ' + conditionalUpper(self.down))
        self.LEFT.set('Left: ' + conditionalUpper(self.left))
        self.RIGHT.set('Right: ' + conditionalUpper(self.right))
        with open('controldata.dat', 'w') as f:
            f.write('w\ns\na\nd')
        self.toApply()

    def toApply(self):
        self.master.root.bind(processed(self.up), self.master.sonic.up)
        self.master.root.bind(processed(self.left), self.master.sonic.left)
        self.master.root.bind(processed(self.down), self.master.sonic.down)
        self.master.root.bind(processed(self.right), self.master.sonic.right)
        if has_counterpart(self.up):
            self.master.root.bind(processed(counterpart(self.up)), self.master.sonic.up)
        if has_counterpart(self.left):
            self.master.root.bind(processed(counterpart(self.left)), self.master.sonic.left)
        if has_counterpart(self.down):
            self.master.root.bind(processed(counterpart(self.down)), self.master.sonic.down)
        if has_counterpart(self.right):
            self.master.root.bind(processed(counterpart(self.right)), self.master.sonic.right)

    def alter(self):
        self.cg = False
        self.tempup = self.up
        self.tempdown = self.down
        self.templeft = self.left
        self.tempright = self.right
        self.master.temppause = self.master.pause.get()
        self.master.pause.set(1)
        self.master.top = Toplevel()
        self.master.top.title('Set Keys')
        self.master.top.geometry('300x400')
        self.master.top.iconbitmap('images\\keysettings.ico')
        self.master.canvas2 = Canvas(self.master.top, height = 400, width = 300, bg = 'white')
        self.master.canvas2.place(x = 0, y = 0)
        self.master.girl = PhotoImage(file = 'images\\showgirl.gif')
        self.master.showgirl = self.master.canvas2.create_image(150, 200, image = self.master.girl)
        self.master.canvas2.create_rectangle(8, 10, 294, 75, fill = '#FF0000', width = 0)
        self.master.canvas2.create_text(166, 20, text = 'Click on the button of direction which', fill = '#00FFFF', font = ('Times', 12, 'bold'))
        self.master.canvas2.create_text(139, 42, text = 'you want to change and then press the', fill = '#00FFFF', font = ('Times', 12, 'bold'))
        self.master.canvas2.create_text(131, 64, text = 'corresponding key on the keyboard.', fill = '#00FFFF', font = ('Times', 12, 'bold'))
        self.buttonok = Button(self.master.top, text = 'Confirm', command = self.confirm1)
        self.buttonok.place(x = 86, y = 324)
        self.buttoncancel = Button(self.master.top, text = 'Cancel', command = self.cancel)
        self.buttoncancel.place(x = 176, y = 324)
        self.buttonUp = Button(self.master.top, textvariable = self.UP)
        self.buttonUp.config(command = self.buttonUp.focus_set)
        self.buttonUp.place(x = 142 - 2 * len(self.UP.get()), y = 100)
        self.buttonUp.bind('<Key>', self.changeup)
        self.buttonLeft = Button(self.master.top, textvariable = self.LEFT)
        self.buttonLeft.config(command = self.buttonLeft.focus_set)
        self.buttonLeft.place(x = 52 - 2 * len(self.LEFT.get()), y = 180)
        self.buttonLeft.bind('<Key>', self.changeleft)
        self.buttonDown = Button(self.master.top, textvariable = self.DOWN)
        self.buttonDown.config(command = self.buttonDown.focus_set)
        self.buttonDown.place(x = 142 - 2 * len(self.DOWN.get()), y = 260)
        self.buttonDown.bind('<Key>', self.changedown)
        self.buttonRight = Button(self.master.top, textvariable = self.RIGHT)
        self.buttonRight.config(command = self.buttonRight.focus_set)
        self.buttonRight.place(x = 232 - 2 * len(self.RIGHT.get()), y = 180)
        self.buttonRight.bind('<Key>', self.changeright)
        self.master.top.protocol('WM_DELETE_WINDOW', self.confirm2)
        self.master.top.focus_set()

    def confirm1(self):
        self.change()
        self.cancel()

    def confirm2(self):
        if self.cg:
            if askokcancel('Confirm', 'Do you want to save these changes?'):
                self.change()
        self.cancel()

    def cancel(self):
        self.master.top.destroy()
        self.master.pause.set(self.master.temppause)

    def unapply(self):
        self.master.root.bind(processed(self.up), doNothing)
        self.master.root.bind(processed(self.left), doNothing)
        self.master.root.bind(processed(self.down), doNothing)
        self.master.root.bind(processed(self.right), doNothing)
        if has_counterpart(self.up):
            self.master.root.bind(processed(counterpart(self.up)), doNothing)
        if has_counterpart(self.left):
            self.master.root.bind(processed(counterpart(self.left)), doNothing)
        if has_counterpart(self.down):
            self.master.root.bind(processed(counterpart(self.down)), doNothing)
        if has_counterpart(self.right):
            self.master.root.bind(processed(counterpart(self.right)), doNothing)

    def change(self):
        self.unapply()
        self.up = self.tempup
        self.down = self.tempdown
        self.left = self.templeft
        self.right = self.tempright
        self.UP.set('Up: ' + conditionalUpper(self.up))
        self.DOWN.set('Down: ' + conditionalUpper(self.down))
        self.LEFT.set('Left: ' + conditionalUpper(self.left))
        self.RIGHT.set('Right: ' + conditionalUpper(self.right))
        self.toApply()
        with open('controldata.dat', 'w') as f:
            f.write(self.up + '\n' + self.down + '\n' + self.left + '\n' + self.right)

    def changeup(self, event):
        if event.keysym not in ['F1', 'F2', 'F3', 'F4', 'F9', 'F10', 'F11', 'F12', '1', '2', self.tempdown, self.templeft, self.tempright]:
            self.cg = True
            self.buttonUp.place_forget()
            self.tempup = event.keysym
            self.UP.set('Up: ' + conditionalUpper(self.tempup))
            self.buttonUp.place(x = 142 - 2 * len(self.UP.get()), y = 100)
        else:
            showwarning('Sorry, you can\'t do this!', 'This key has been occupied.')
            self.buttonUp.focus_set()

    def changedown(self, event):
        if event.keysym not in ['F1', 'F2', 'F3', 'F4', 'F9', 'F10', 'F11', 'F12', '1', '2', self.tempup, self.templeft, self.tempright]:
            self.cg = True
            self.buttonDown.place_forget()
            self.tempdown = event.keysym
            self.DOWN.set('Down: ' + conditionalUpper(self.tempdown))
            self.buttonDown.place(x = 142 - 2 * len(self.DOWN.get()), y = 260)
        else:
            showwarning('Sorry,  you can\'t do this!', 'This key has been occupied.')
            self.buttonDown.focus_set()

    def changeleft(self, event):
        if event.keysym not in ['F1', 'F2', 'F3', 'F4', 'F9', 'F10', 'F11', 'F12', '1', '2', self.tempdown, self.tempup, self.tempright]:
            self.cg = True
            self.buttonLeft.place_forget()
            self.templeft = event.keysym
            self.LEFT.set('Left: ' + conditionalUpper(self.templeft))
            self.buttonLeft.place(x = 52 - 2 * len(self.LEFT.get()), y = 180)
        else:
            showwarning('Sorry,  you can\'t do this!', 'This key has been occupied.')
            self.buttonLeft.focus_set()

    def changeright(self, event):
        if event.keysym not in ['F1', 'F2', 'F3', 'F4', 'F9', 'F10', 'F11', 'F12', '1', '2', self.tempdown, self.templeft, self.tempup]:
            self.cg = True
            self.buttonRight.place_forget()
            self.tempright = event.keysym
            self.RIGHT.set('Right: ' + conditionalUpper(self.tempright))
            self.buttonRight.place(x = 232 - 2 * len(self.RIGHT.get()), y = 180)
        else:
            showwarning('Sorry, you can\'t do this!', 'This key has been occupied.')
            self.buttonRight.focus_set()