#!/opt/ipmanager/venv/bin/python3
from getpass import getpass
from mysql.connector import connect, Error



def search_net():
    query = "SELECT * FROM networks" 
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def show_net(net):
    query = f"select * FROM networks WHERE net = '{net}' "
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result



def add_net(net, active, comment):
    query = f"insert into networks (`net`, `active`, `comment`) value ('{ip}', '{active}', '{comment}')"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result

def del_net(net):
    query = f"delete from networks where net = '{net}'"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result

def upd_net(net, active, comment):
    query = f"update networks set `active` = '{active}', `comment` = '{comment}' where net = '{net}'"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result
