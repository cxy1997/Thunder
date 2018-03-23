class Linked_List:
    def __init__(self, x, y, master, hp = 0, dx = 0, dy = 0):
        self.hp = hp
        self.t = 0
        self.master = master
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self._next = False
        self._last = False
    def add(self, x, y, hp = 0, dx = 0, dy = 0):
        p = self
        while p._next:
            p = p.next
        p.next = Linked_List(x, y, self.master, hp, dx, dy)
        p.next._last = True
        p._next = True
        p.next.last = p
        p = p.next
        p.pic = self.master.master.canvas.create_image(p.x, p.y, image = self.master.img)
def dlt(p):
    p.master.master.canvas.delete(p.pic)
    if not p._next:
        p.last._next = False
    else:
        p.last.next = p.next
        p.next.last = p.last
    del p