### 提供换热器的相关数据
import DAO.HEdao


# 获得底托的全部数据
# return list(entity)
def getColletAll():
    collet_ls = DAO.HEdao.getColletAll()
    return collet_ls