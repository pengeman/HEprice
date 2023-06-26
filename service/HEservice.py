### 提供换热器的相关数据
import DAO.HEdao

# 获得sheet的全部数据
def getSheetAll():
    sheet_list = DAO.HEdao.getSheetall()
    return  sheet_list

def getTextureAll():
    texture_list = DAO.HEdao.getTextureAll()
    return texture_list

def getThinknessAll():
    return DAO.HEdao.getThinknessAll()

def getPackageAll():
    return DAO.HEdao.getPackageAll()

# 获得底托的全部数据
# return list(entity)
def getColletAll():
    collet_ls = DAO.HEdao.getColletAll()
    return collet_ls


# 新增一个底托价格
# 参数：板型，单价
# 返回：0失败，1成功
def newCollet(type, price):
    r = DAO.HEdao.newCollet(type, price)
    if r > 0:
        return 1
    else:
        return 0


# 更新一个底托价格
# 参数：板型，单价
# 返回：0失败，1成功
def updateCollet(id, type, price):
    r = DAO.HEdao.updateCollet(id,type, price)
    if r > 0:
        return 1
    else:
        return 0