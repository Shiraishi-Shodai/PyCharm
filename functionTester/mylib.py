def functionAdd(a,b):
    c = a + b
    return c

def calcTaxPriceSimple(price):
    return price * 1.1

keigenZeiritsu = 1.08
seizyouZeiritsu = 1.10

def calcTaxPriceKeigen(price,flag):
    if flag:
        return price * keigenZeiritsu
    else:
        return price * seizyouZeiritsu