# 底托

class Collet(object):
    id = 0
    type = ""
    price = 0
    about = ""

    def __init__(self):
        id = 0
        type = ""
        price = 0
        about = ""

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "price": str(self.price),
            "about": self.about
        }
