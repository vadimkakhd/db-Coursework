import cx_Oracle
from datafororacle import *

def getUsers():
    connection = cx_Oracle.connect(username, password, databaseName)

    cursor = connection.cursor()


    query = 'SELECT * FROM "User"'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def is_user(user_login, user_pass):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    count = cursor.callfunc("user_package.is_user", cx_Oracle.NATIVE_INT, [user_login, user_pass])

    cursor.close()
    connection.close()

    return count

def add_user(u_nickname, u_login, u_pass, u_name, u_surname, u_faculty, u_course):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("user_package.add_user", [u_nickname, u_login, u_pass, u_name, u_surname, u_faculty, u_course])
    cursor.close()
    connection.close()


def del_user(u_nickname):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    cursor.callproc("user_package.deluser", [u_nickname])
    cursor.close()
    connection.close()

def add_resourse(u_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("resourse_package.add_resourse", [u_resourse])
    cursor.close()
    connection.close()

def del_resourse(u_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("resourse_package.del_resourse", [u_resourse])
    cursor.close()
    connection.close()

def get_resourse(u_resourse=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if not u_resourse:
        query = 'select * from table(resourse_package.get_resourse())'
        cursor.execute(query)
    else:
        query = 'select * from table(resourse_package.get_resourse(:u_resourse))'
        cursor.execute(query, u_resourse=u_resourse)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_resourse(new_resourse, old_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("resourse_package.update_resourse", [new_resourse, old_resourse])
    cursor.close()
    connection.close()

def add_theme(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("lection_theme_package.add_theme", [u_theme])
    cursor.close()
    connection.close()

def del_theme(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("lection_theme_package.del_theme", [u_theme])
    cursor.close()
    connection.close()

def get_theme(theme=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if not theme:
        query = 'select * from table(lection_theme_package.get_lection_theme())'
        cursor.execute(query)
    else:
        query = 'select * from table(lection_theme_package.get_lection_theme(:theme))'
        cursor.execute(query, theme=theme)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_theme(new_theme, old_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("lection_theme_package.update_theme", [new_theme, old_theme])
    cursor.close()
    connection.close()

def add_info(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("information_package.add_info", [u_theme])
    cursor.close()
    connection.close()

def del_info(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callfunc("information_package.del_info", [u_theme])
    cursor.close()
    connection.close()

def get_information(nick=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if not nick:
        query = 'select * from table(information_package.get_information())'
        cursor.execute(query)
    else:
        query = 'select * from table(information_package.get_information(:nick))'
        cursor.execute(query, nick=nick)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result