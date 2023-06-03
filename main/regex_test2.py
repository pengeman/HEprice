import re


def match_character(input_string):
    pattern = r'^BP-[304|316]$'

    if re.match(pattern, input_string):
        print("匹配成功")
    else:
        print("匹配失败")


# 要匹配的字符串
test_string = "BP-304"

# 调用匹配函数
match_character(test_string)
