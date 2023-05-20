import config.base_setting


class DBconfig(config.base_setting.Config):
    # MySQL所在主机名
    HOSTNAME = "127.0.0.1"
    # MySQL监听的端口号，默认3306
    PORT = 3306
    # 连接MySQL的用户名，自己设置
    USERNAME = "peng"
    # 连接MySQL的密码，自己设置
    PASSWORD = "sa"
    # MySQL上创建的数据库名称
    DATABASE = "heat_exchanger"
    # 通过修改以下代码来操作不同的SQL比写原生SQL简单很多 --》通过ORM可以实现从底层更改使用的SQL
