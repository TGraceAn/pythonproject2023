import pymysql.cursors
from ..entities import *
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='admin',
                             port= 3306,
                             database='ZOO',
                             cursorclass=pymysql.cursors.DictCursor)
def test():
    cursor = connection.cursor()
    sql = "select * from person limit 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def get_all(table):
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM {table};"
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result

def insert_one(table, values):
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {table} values {values};"
        cursor.execute(sql)
        connection.commit()
        

def update_one(table, cols, values):
    _set = ""
    for index in range(1, len(cols)):
        if index == (len(cols)-1):
            _set = _set + f"{str(cols[index])} = '{str(values[index])}'"
        else:
            _set = _set + f"{str(cols[index])} = '{str(values[index])}', "

    with connection.cursor() as cursor:
        sql = f"""UPDATE {table}
                SET {_set}
                WHERE {cols[0]} = '{values[0]}';"""
            
        
        cursor.execute(sql)
        connection.commit()  


def show_all_info_ostaff():
    sql = """SELECT *
            FROM OSTAFF
            INNER JOIN EMPLOYEE ON OSTAFF.OEmpID = EMPLOYEE.EmployeeID
            INNER JOIN PERSON ON EMPLOYEE.EmployeeFullName = PERSON.FullName;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result

def show_all_info_zookeeper():
    sql = """SELECT *
            FROM ZOOKEEPER
            INNER JOIN EMPLOYEE ON ZOOKEEPER.ZEmpID = EMPLOYEE.EmployeeID
            INNER JOIN PERSON ON EMPLOYEE.EmployeeFullName = PERSON.FullName;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result
    
def show_all_zskills():
    sql = """SELECT *
            FROM ZOOKEEPER
            INNER JOIN ZSKILLS ON ZOOKEEPER.KeeperID = ZSKILLS.Kskillid;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result
    
def show_all_info_visitor():
    sql = """SELECT *
            FROM VISITOR
            INNER JOIN PERSON ON VISITOR.VisitorFullName = PERSON.FullName;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result
    
def show_all_feeding():
    sql = """SELECT *
            FROM ANIMAL
            INNER JOIN FEEDING ON ANIMAL.species = FEEDING.species ;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames, result
    
def get_col_person():
    sql = """SELECT * FROM PERSON LIMIT 1;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames
    
def get_col_zookeeper():
    sql = """SELECT * FROM ZOOKEEPER LIMIT 1;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames
    
def get_col_ostaff():
    sql = """SELECT * FROM OSTAFF LIMIT 1;"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        colnames = [col[0] for col in cursor.description]
        return colnames
    
def del_one(table, key, value):
    with connection.cursor() as cursor:
        sql = f"DELETE FROM {table} WHERE {key}='{value}'"
        print(sql)
        cursor.execute(sql)
        connection.commit()  
