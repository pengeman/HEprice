class SheetArea(object):
    id = 0
    sheet = ""
    area = 0

    def __init__(self):
        self.id = 0
        self.sheet = ""
        self.area = 0

    def jsonformat(self):
        return {
            "id": self.id,
            "sheet": str(self.sheet),
            "area": self.area
        }
