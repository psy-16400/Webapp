import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='kdp')

    
def addVadak(t):
    db=getConnection()
    sql='insert into kdpadd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def selectAllVadak():
    db=getConnection()
    sql='select * from kdpadd'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteVadak(ids):
    db=getConnection()
    sql='delete from kdpadd where id=%s'
    cr=db.cursor()
    cr.execute(sql,ids)
    db.commit()
    db.close()

def selectVadakById(id1):
    db=getConnection()
    #sql='select * from kdpadd where Id=%s'
    cr=db.cursor()
    print(id1)
    cr.execute("select * from kdpadd where Id=%s",(id1,))
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateVadak(t):
    db=getConnection()
    sql='update kdpadd set FullName=%s,Gender=%s,Age=%s,EmailID=%s,Contact=%s,Emg_Contact=%s,Address=%s,Location=%s,Experience=%s,Preference=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def Log_check(t):
    db=getConnection()
    sql="select EmailID, contact from kdpadd where EmailID=%s and contact=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
