from Tkinter import Menu

class myMenu:
    def __init__(self, master):
        self.master = master
        self.mainmenu = Menu(self.master.root)
        self.master.root.config(menu = self.mainmenu)
        self.gamemenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label = 'Game', menu = self.gamemenu)
        self.gamemenu.add_checkbutton(label = 'Pause           F1', variable = self.master.pause)
        self.gamemenu.add_command(label = 'Restart         F2', command = self.master.start)
        self.gamemenu.add_command(label = 'Main menu', command = self.master.mainmenu)
        self.gamemenu.add_separator()
        self.gamemenu.add_command(label = 'Exit Game   F12', command = self.master.quitcallback)
        self.controlmenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label = 'Control', menu = self.controlmenu)
        self.controlmenu.add_command(label = 'Change Background  Num 1', command = self.master.galaxy.change)
        self.controlmenu.add_command(label = 'Change Plane            Num 2', command = self.master.sonic.change)
        self.controlmenu.add_command(label = 'Key Settings                    F3', command = self.master.cs.alter)
        self.controlmenu.add_command(label = 'Key Settings Initialize       F4', command = self.master.cs.initialize)
        self.helpmenu = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label = 'Help', menu = self.helpmenu)
        self.helpmenu.add_command(label = 'Introductions       F9', command = self.master.introduction.showup)
        self.helpmenu.add_command(label = 'How to play        F10', command = self.master.he.showup)
        self.helpmenu.add_command(label = 'Highest scores    F11', command = self.master.scoreboard.showup)