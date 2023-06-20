class Flange1(object):
    id = 0
    type = ""
    texture = ""
    class_=""
    price=0

    def __init__(self):
        id = 0
        type = ""
        texture = ""

        class_ = ""
        price = 0

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "texture": str(self.texture),
            "class_": str(self.class_),
            "price": self.price,
            "about": str(self.about)
        }
