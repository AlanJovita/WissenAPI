import mysql.connector
from Model.log import Log

host = '177.234.148.10'
user = 'prem0867_user_wissen'
senha='h@gIh%S9v-O&'
bd='prem0867_wissen'

def open_connect():

    try:
        con = mysql.connector.connect(host=host,user=user,password=senha,database=bd)
        if con.is_connected():
           return con
        else:
           return None
    except mysql.connector.Error as erro:
        Log.Registrar("Mysql Error! Falha ao conectar no banco: {}".format(erro))
        return None 
    except:
        return None

def open_connect_product():

    try:
        con = mysql.connector.connect(host=host,user='prem0867_produtos',password='k!od094T70L6',database='prem0867_produtos')
        if con.is_connected():
           return con
        else:
           return None
    except mysql.connector.Error as erro:
        Log.Registrar("Mysql Error! Falha ao conectar no banco: {}".format(erro))
        return None 
    except:
        return None

def close_connect(cursor,con):
    if con.is_connected():
        cursor.close()
        con.close()
        

def executar(sql)->bool:
 try:
    con = open_connect()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    return True
 except Exception as e:
    Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {e}")
    return False
 finally:
    close_connect(cursor,con)

def selectAll(sql):

    con = open_connect()

    if (con == None):
        return None
    else:   
        
        cursor = con.cursor(buffered=True)

        try:
            cursor.execute(sql)
        
            return cursor.fetchall()
            
        except Exception as e:
            Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {e}")
            return None
        finally:
            close_connect(cursor,con)


def selectOne(sql):
    
    con = open_connect()
    if (con == None):
        return None
    else:   
        
        cursor = con.cursor(buffered=True)
        try:
            cursor.execute(sql)
        
            result = cursor.fetchone()
            
            if result==None:
                return None
            else:        
                return result[0]
        except Exception as e:
            Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {e}")
            return None
        finally:
            close_connect(cursor,con)

def selectId(sql):

    con = open_connect()
    if (con == None):
        return None
    else:   
        con.autocommit=False
        cursor = con.cursor()

        try:

            cursor.execute(sql)
            cursor=None           
            last_inserted_id=cursor.lastrowid

            con.commit()

            return last_inserted_id
        
        except mysql.connector.Error as err:
            con.rollback()
            Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {err}")
        except Exception as e:
            con.rollback()
            Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {e}")
        finally:
           close_connect(cursor,con)

def selectProduct(sql):
    
    con = open_connect_product()
    if (con == None):
        return None
    else:   
        
        cursor = con.cursor(buffered=True)

        try:
            cursor.execute(sql)

            result = cursor.fetchone()
            
            if result==None:
                return None
            else:        
                return result
        
        except Exception as e:
            Log.Registrar(f"Mysql Error SQL:|{sql}| Exception: {e}")
            return None
        finally:
            close_connect(cursor,con)
        
    




