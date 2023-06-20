class User(object):
    id = 0
    name = ""
    code = ""
    password = ""
    department = ""
    role = ""

    def __init__(self):
        id = 0
        name = ""
        code = ""
        password = ""
        department = ""
        role = ""

    def jsonformat(self):
        return {
            "id": self.id,
            "name": str(self.name),
            "code": str(self.code),
            "password": str(self.password),
            "department": str(self.department),
            "role": str(self.role)
        }
