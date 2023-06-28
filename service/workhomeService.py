# 工作主页面业务模型
import service.HEservice


def getsheet():
    sheetall_ls = service.HEservice.getSheetAll() ##list(entity)
    # 转换成<option>xxx</option>
    sheetoption_ls = list()
    for sheet_entity in sheetall_ls:
        id = sheet_entity.id
        type = sheet_entity.type
        pic = sheet_entity.pic
        sheetoption_ls.append("<option id='"+str(id)+"'>" + type + "</option>")
    return sheetoption_ls

## 材质
def getTexture():
    textureall_ls = service.HEservice.getTextureAll()
    # 转换成<option>xxx</option>
    textoption_ls = list()
    for texture_entity in textureall_ls:
        id = texture_entity.id
        texture = texture_entity.texture
        about = texture_entity.about
        textoption_ls.append("<option id='" + str(id) + "'>" + texture + "</option>")
    return textoption_ls


## 厚度
def getThinkness():
    thinknessall_ls = service.HEservice.getThinknessAll()
    # 转换成<option>xxx</option>
    thinknessoption_ls = list()
    for thinkness_entity in thinknessall_ls:
        id = thinkness_entity.id
        thinkness = thinkness_entity.thinkness
        about = thinkness_entity.about
        thinknessoption_ls.append("<option id='"+str(id)+"'>"+str(thinkness)+"</option>")
    return thinknessoption_ls

## 承压
def getPressure():
    pressureall_ls = service.HEservice.getPressureAll()
    pressureoption_ls = list()
    if pressureall_ls is None:
        pressureoption_ls.append("<option id='1'>1.0Mpa</option>")
        pressureoption_ls.append("<option id='2'>1.6Mpa</option>")
        pressureoption_ls.append("<option id='3'>2.0Mpa</option>")
        pressureoption_ls.append("<option id='4'>2.5Mpa</option>")
        return pressureoption_ls
    else:
        for pressure_entity in pressureall_ls:
            id = pressure_entity.id
            pressure = pressure_entity.pressure
            pressureoption_ls.append("<option id='" + str(id) + "'>" + str(pressure) + "</option>")
        return pressureoption_ls

## 橡胶垫片材质
def getEpdm():
    epdm_ls = service.HEservice.getEpdmAll()
    epdm_ls.append("<option id='1'>epdm</option>")
## 包装
def getPackage():
    packageoption_ls = list()
    packageall_ls = service.HEservice.getPackageAll()
    for package_eneity in packageall_ls:
        package_eneity.id
        package_eneity.type