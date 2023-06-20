class Thinkness(object):
    id = 0
    thinkness = 0.0
    about = ""

    def __init__(self):
        self.id = 0
        self.thinkness = 0.0
        self.about = ""


    def jsonformat(self):
        return {
            "id": self.id,
            "thinkness": self.thinkness,
             "about": self.about
        }
