from flask import render_template

from DAO.UserDao import UserDao


# 登陆口令验证
def login_check(username, pwd):
    flag = 0
    print("login check")
    userDao = UserDao()
    user = userDao.getUserByName(username)
    if user is not None:
        password = user.password
        if password == pwd:
            flag = 1
    else:
        msg = "用户名或口令错误"
        pass

    if flag == 1:
        return True
    else:
        return False

    # if flag == 1:
    #     return render_template('HEcalculate/HEhome2.html')
    # else:
    #     return render_template('loginhome/login.html', error=msg)
