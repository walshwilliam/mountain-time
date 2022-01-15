import random
def map():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    e = random.randint(0, 100)
    
    if a < 20:
        f = "/\\"
    elif a < 30:
        f = "__"
    elif a < 45:
        f = "____"
    elif a < 60:
        f = "_"
    elif a < 65:
        f = "/\^/\\"
    else:
        f = "____"
        
    if b < 20:
        g = "/\\"
    elif b < 30:
        g = "__"
    elif b < 45:
        g = "____"
    elif b < 60:
        g = "_"
    elif b < 65:
        g = "/\^/\\"
    else:
        g = "____"
        
    if c < 20:
        h = "/\\"
    elif c < 30:
        h = "__"
    elif c < 45:
        h = "____"
    elif c < 60:
        h = "_"
    elif c < 65:
        h = "/\^/\\"
    else:
        h = "____"
        
    if d < 20:
        i = "/\\"
    elif d < 30:
        i = "__"
    elif d < 45:
        i = "____"
    elif d < 60:
        i = "_"
    elif d < 65:
        i = "/\^/\\"
    else:
        i = "____"
        
    if e < 20:
        j = "/\\"
    elif e < 30:
        j = "__"
    elif e < 45:
        j = "____"
    elif e < 60:
        j = "_"
    elif e < 65:
        j = "/\^/\\"
    else:
        j = "____"
        
    print(f + g + h + i + j)
def date():
    x = random.randint(1600, 2000)
    month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    if x % 4 == 0 and x % 400 != 100 and x % 400 != 200 and x % 400 != 300:
        y = random.randint(0, 11)
        if y == 0 or y == 2 or y == 4 or y == 6 or y == 7 or y == 9 or y == 11:
            z = random.randint(1, 31)
        if y == 1:
            z = random.randint(1, 29)
        else:
            z = random.randint(1, 30)
        print(month[y],z,",",x)
        
    else:
        y = random.randint(0, 11)
        if y == 0 or y == 2 or y == 4 or y == 6 or y == 7 or y == 9 or y == 11:
            z = random.randint(1, 31)
        if y == 1:
            z = random.randint(1, 28)
        else:
            z = random.randint(1, 30)
        print(month[y],z,",",x)
        
map()
date()
