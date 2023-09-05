import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='cdb')

    
def addPerson(t):
    db=getConnection()
    sql='insert into kdpadd values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def selectAllPerson():
    db=getConnection()
    sql='select * from cdbadd'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deletePerson(ids):
    db=getConnection()
    sql='delete from cdbadd where id=%s'
    cr=db.cursor()
    cr.execute(sql,ids)
    db.commit()
    db.close()

def selectPersonById(id1):
    db=getConnection()
    #sql='select * from kdpadd where Id=%s'
    cr=db.cursor()
    print(id1)
    cr.execute("select * from cdbadd where Id=%s",(id1,))
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updatePerson(t):
    db=getConnection()
    sql='update cdbadd set FullName=%s,Gender=%s,Age=%s,where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def Log_check(t):
    db=getConnection()
    sql="select EmailID, contact from cdbadd where EmailID=%s and contact=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
