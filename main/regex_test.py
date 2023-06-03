import re


def validate_string(input_string):
    pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\d{1,3}-(304|316|tai|ni|mo|ha)-(0.5|0.6|0.7|0.8|1.0|1.2)-(0.1|0.16|0.2|0.25)Mpa-(epdm|nbr|fkm)-(304|316)衬套-(tan|304|316)接管-(1|2)$'

    if re.match(pattern, input_string):
        print("字符串验证通过")
    else:
        print("字符串验证失败")


# 要验证的字符串
tests = "BP50b100-tai-0.6-0.1Mpa-epdm-304衬套-tan接管-1"

# 调用验证函数
validate_string(tests)
