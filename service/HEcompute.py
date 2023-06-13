import logging.handlers

from DAO import HEdao
from service.HEparament import HEparament

# 解析换热器型号数据
HEtype_paramert = {
    "sheet": " ",  # 板型
    "texture": " ",  # 材质
    "thinkness": " ",  # 厚度
    "area": "",  # 面积
    "pressure": " ",  # 压力
    "gasket": "",  # 法兰垫片
    "lining": " ",  # 夹板衬套
    "pipeline": " ",  # 夹板接管
    "standard": " ",  # 工业标准
    "flange1": " ",  # 法兰-HG/T20592-09国标 加工标准
    "flange2": " "  # 法兰 JB/T81-2015  供热标准
}

HEpara = HEparament();

''' 
换热器型号BP200mhv-300-304-0.5-0.16Mpa-密封垫片-衬套材质-接管方式-1/2化工标准/供热标准
以BP开头，然后一个数字两位或三位长，包括[32,50,100,150,200,250,300,350,400,450,500,550]，紧接是字符串，2个字符到5个字符长度，其中第一个字符是b或m,然后是分隔符-，
然后是个数字，从1到999,然后是分隔符-，
然后是个字符串包括[304,316,tai,ni,mo,ha]，然后是分隔符-，
然后是个数字包括[0.5,0.6,0.7,0.8,1.0,1.2]，然后是分隔符-，
然后是个数字，包括[0.1,0.16,0.2,0.25],紧接是Mpa,然后是分隔符-，
然后是不分大小写的字符串[empd,nbr,fkm],然后是分隔符-,
然后是字符串[304,316]，紧接是“衬套",然后是分隔符-,
然后是字符串[tan,304,316]接管,然后是分隔符-,
最后是1或2
return : HEprice_values = {
            'price_guide' : 'xx',
            'price_90' : 'xx',
            'price_80' : 'xx',
            'price_70' : 'xx'
        }
'''


def calHE(HEtype):
    HEpara = parse2(HEtype)
    price_sheet = calHE_sheet(HEpara.sheet, HEpara.texture, HEpara.thinkness)
    price_splint = calHE_splint(HEpara.sheet, HEpara.area, HEpara.pressure, HEpara.lining)
    price_flange = calHE_flange(HEpara.sheet, HEpara.standard, HEpara.lining)
    price_package = calHE_package(HEpara.sheet, HEpara.area)
    price_collet = calHE_collet(HEpara.sheet)
    price = price_sheet + price_splint + price_flange + price_package + price_collet


def parse(HEtype):
    paramert = {
        "sheet": " ",  # 板型
        "texture": " ",  # 材质
        "thickness": " ",  # 厚度
        "area": "",  # 面积
        "flange1": " ",  # 法兰-HG/T20592-09国标 加工标准
        "flange2": " "  # 法兰 JB/T81-2015  供热标准
    }

    HEparemets = HEtype.split("-")  # 将板型数据分割成参数数组
    paramert["sheet"] = HEparemets[0]
    paramert["area"] = HEparemets[1]
    paramert["texture"] = HEparemets[2]
    paramert["thickness"] = HEparemets[3]
    paramert["pressure"] = HEparemets[4]
    paramert["gasket"] = HEparemets[5]  # 密封垫片
    paramert["lining"] = HEparemets[6]  # 夹板衬套
    paramert["pipeline"] = HEparemets[7]  # 接管
    paramert["standard"] = HEparemets[8]
    return paramert


'''
解析板换型号，如果解析失败，返回None
使用类记录板型参数信息
'''


def parse2(HEtype):
    HEparemets = HEtype.split("-")  # 将板型数据分割成参数数组
    _HEparament = HEparament()
    _HEparament.sheet = HEparemets[0]
    _HEparament.area = HEparemets[1]
    _HEparament.texture = HEparemets[2]
    _HEparament.thinkness = HEparemets[3]
    _HEparament.pressure = HEparemets[4]
    _HEparament.gasket = HEparemets[5]  # 密封垫片
    _HEparament.lining = HEparemets[6]  # 夹板衬套
    _HEparament.pipeline = HEparemets[7]  # 接管
    _HEparament.standard = HEparemets[8]
    if _HEparament.standard == 1:
        _HEparament.flange1 = 1
        _HEparament.flange2 = 0
    else:
        _HEparament.flange1 = 0
        _HEparament.flange2 = 1
    b = HEparemets[0]
    b = b[2:][0:2]
    if b == '32':
        b = 'BP32b'
        _HEparament.sheet = b
    return _HEparament


# 计算板片价格
# 参数sheet：BP100B,BP200M
# texture: 304,316,ni,tai
# thinckness: 0.5, 0,6
def calHE_sheet(sheet, texture, thinkness):
    sheetPrice = HEdao.getPriceByType(sheet, texture, thinkness)
    return sheetPrice


# 计算框架板价格
# 参数： sheet: BP100
# area : 50 板片面积，用于计算板片数量
# pressure : 16 , 压力
# lining: 304 内衬
def calHE_splint(sheet, area, pressure, lining):
    area_entity = HEdao.getSheetAreaByType(sheet)
    sheetarea = area_entity.area
    classnum = int(sheetarea / area)
    splint_entity = HEdao.getSplingbyType(sheet, pressure, classnum, lining)
    return splint_entity.price


# 计算法兰价格
def calHE_flange(sheet, classs, texture, stand):
    if stand == 1:
        flange_entity = HEdao.getFlange1ByType(sheet, classs, texture)
    else:
        flange_entity = HEdao.getFlange2ByType(sheet, classs, texture)
    return flange_entity.price



# 计算包装价格
def calHE_package(sheet , area):
    package_entity = HEdao.getPackageByType(sheet, area)
    return package_entity.price

# 计算接管价格
def calHE_pipeline(sheet, texture):
    pipeline_entity = HEdao.getPipelineByType(sheet, texture)
    return pipeline_entity.price



# 计算地托价格
def calHE_collet(sheet):
    collet_entity = HEdao.getColletByType(sheet)
    return collet_entity.price
