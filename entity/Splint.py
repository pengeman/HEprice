class Splint(object):
    id = 0
    type = ""
    pressure = 0
    classmin = 0
    classmax = 0
    lining = ""
    price = 0
    pic = ''

    def __init__(self):
        self.id = 0
        self.type = ""
        self.pressure = 0
        self.classmin = 0
        self.classmax = 0
        self.lining = ''
        self.price = 0
        self.pic = ''

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "pressure": self.pressure,
            "classmin": self.classmin,
            "classmax": self.classmax,
            "lining": str(self.lining),
            "price": self.price,
            "pic": self.pic
        }
