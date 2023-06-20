class Package(object):
    id = 0
    type = ""
    area = 0
    price = 0

    def __init__(self):
        id = 0
        type = ""
        area = 0
        price = 0

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "area": self.area,
            "price": self.price
        }

