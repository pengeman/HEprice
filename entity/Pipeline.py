class Pipeline(object):
    id = 0
    type = ""
    texture = ""
    price = 0

    def __init__(self):
        self.id = 0
        self.type = ""
        self.texture = ""
        self.price = 0

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "texture": str(self.texture),
            "price": self.price
        }
