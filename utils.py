from string import upper, lower

def bulletspeed(n):
    x=5 + n
    if x > 15:
        x = 15
    return x

def firerate(n):
    x=63 - 3 * n
    if x < 6:
        x = 6
    return x

def hit_the_boss(x, y):
    if not (90 <= x <= 330 and 70 <= y <= 234):
        return False
    if y <= 200:
        return True
    if 136 <= x <= 188 or 232 <= x <= 284:
        return False
    return True

def myCmp(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    else:
        return 0

def doNothing(event):
    return None

def conditionalUpper(s):
    if len(s) == 1 and 'a' <= s <= 'z':
        return upper(s)
    else:
        return s

def processed(s):
    if has_counterpart(s) or (s in '.0123456789+-*/;\''):
        return '<Key-' + s + '>'
    else:
        return '<' + s + '>'

def has_counterpart(s):
    if len(s) == 1:
        return 'a' <= s <= 'z' or 'A' <= s <= 'Z'
    else:
        return False

def counterpart(s):
    if 'a' <= s <= 'z':
        return upper(s)
    elif 'A' <= s <= 'Z':
        return lower(s)

def hpcl(n):
    if n >= 60:
        return 'green'
    elif n >= 30:
        return 'orange'
    else:
        return 'red'