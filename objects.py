class routeObject:
    __start = ''
    __end = ''
    __distance = 0
    __time = 0
    def timeinminutes(self):
        return round(self.time/60)
    def oldPrice(self):
        return 5.90 + self.distance * 1.60

class priceObject:
    __vendor = ''
    __amount = 0
    __diff = 0
    __char = ''
    def __init__(self, vendor, amount):
        self.vendor = vendor
        self.amount = amount
    def color(self):
        if self.char == 'fa-arrow-up':
            return 'red'
        else:
            return 'green'