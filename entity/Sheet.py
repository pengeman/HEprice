class Sheet(object):
    id = 0
    type = ""
    pic = ""

    def __init__(self):
        self.id = 0
        self.type = ""
        self.pic = ""

    def jsonformat(self):
        return {
            "id": self.id,
            "type": str(self.type),
            "pic": str(self.pic)
        }
