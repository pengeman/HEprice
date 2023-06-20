class Texture(object):
    id = 0
    texture = ""
    about = ""

    def __init__(self):
        self.id = 0
        self.texture = ""
        self.about = ""

    def jsonformat(self):
        return {
            "id": self.id,
            "texture": str(self.texture),
            "about": self.about
        }
