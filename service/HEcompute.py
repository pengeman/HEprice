import logging.handlers


# 解析换热器型号数据
HEtype_paramert = {
"sheet" : " " ,    # 板型
"texture" : " " ,  #材质
"thickness" : " " ,#厚度
"area" : ""       ,#面积
"pressure" : " " , #压力
"gasket" : ""  ,   #法兰垫片
"lining" : " " ,   #夹板衬套
"pipeline": " ",   #夹板接管
"standard" : " " , #工业标准
"flange1" : " "   ,#法兰-HG/T20592-09国标 加工标准
"flange2" : " "    #法兰 JB/T81-2015  供热标准
}


''' 
换热器型号BP200mhv-300-304-0.5-0.16Mpa-密封垫片-衬套材质-接管方式-1/2化工标准/供热标准
'''
def calHE(HEtype):
    #参数初始化
    global HEtype_paramert
    HEtype_paramert.clear()
    d = 23 * 3
    HEtype_paramert = parse(HEtype)  # 解析板型数据
    pass


def parse(HEtype):
    paramert = {
        "sheet": " ",  # 板型
        "texture": " ",  # 材质
        "thickness": " ",  # 厚度
        "area": "",  # 面积
        "flange1": " ",  # 法兰-HG/T20592-09国标 加工标准
        "flange2": " "  # 法兰 JB/T81-2015  供热标准
    }

    HEparemets = HEtype.split("-") # 将板型数据分割成参数数组
    paramert["sheet"] = HEparemets[0]
    paramert["area"] = HEparemets[1]
    paramert["texture"] = HEparemets[2]
    paramert["thickness"] = HEparemets[3]
    paramert["pressure"] = HEparemets[4]
    paramert["gasket"] = HEparemets[5]  #密封垫片
    paramert["lining"] = HEparemets[6]  #夹板衬套
    paramert["pipeline"] = HEparemets[7] #接管
    paramert["standard"] = HEparemets[8]
    return paramert


# 计算板片价格
def calHE_sheet():
    pass

# 计算框架板价格
def calHE_splint():
    pass


# 计算法兰价格
def calHE_flange():
    pass

# 计算包装价格
def calHE_package():
    pass

# 计算地托价格
def calHE_collet():
    pass
