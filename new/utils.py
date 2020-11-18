import pymysql

def create_db(name):
    cursor = conn.cursor()
    try:
        # header should be entered as parameters of the func
        cursor.execute("""
        create database %s(
        id int not null,
        name char(10),
        chara char(4),
        move int not null,
        addr int not null
        """ % name)
    except Exception:
        cursor.execute('show errors')
        error = cursor.fetchone()
        print(error)
        create_database()
    else:
        print('Created a new database named %s' % name)
 