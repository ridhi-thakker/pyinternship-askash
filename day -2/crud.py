import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pycrud"
)
mycursor = mydb.cursor()


def createtable():
    mycursor.execute(
        "CREATE TABLE student2 (sid INT(10) AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),dob DATE)")
    mycursor.execute("SHOW TABLES")
    mycursor.close()
    mydb.close()


def insert():
    sql = "INSERT INTO student (sid, name, dob) VALUES (%s,%s,%s)"
    val = (1, "ridhi", "2007-01-10")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()


def update():
    sql = "UPDATE student SET dob = '2000-12-22' WHERE name = 'ridhi'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    mycursor.close()
    mydb.close()


def delete():
    sql = "DELETE FROM student WHERE sid = '1'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    mycursor.close()
    mydb.close()


print("If you want to Create Table Enter c.")
print("If you want to Insert into Table Enter i.")
print("If you want to update Table Enter u.")
print("If you want to delete from Table Enter d.")
print("")
print("")
que = input("What action you want to perform?")
if(que == "c"):
    createtable()
if(que == "i"):
    insert()
if(que == "u"):
    update()
if(que == "d"):
    delete()
