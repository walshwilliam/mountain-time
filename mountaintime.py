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
    x = random.randint(0, 11)
    month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    leapyear = ["1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", "1984", "1988", "1992", "1996", "2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028"]
    if x == 0 or x == 2 or x == 4 or x == 6 or x == 7 or x == 9 or x == 11:
        y = random.randint(1, 31)
    if x == 1:
        y = random.randint(1, 29)
    else:
        y = random.randint(1, 30)
    if x == 1 and y == 29:
        z = random.randint(0,19)
        print(month[x], y, leapyear[z])
    else:
        z = random.randint(1950, 2030)
        print(month[x], y, ",", z)
        
map()
date()
