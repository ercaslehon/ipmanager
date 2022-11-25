#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress

#This is function for check a conditions

def valid_net(net):
    try:
        ipaddress.ip_network(net)
        return True
    except:
        return False

def check_net(net):
    valid_net(net)
    if valid_net(net) is True:
        query = f"select * FROM networks WHERE net = '{net}' "
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) == 0:
            return True
        else:
            return False
    else:
        return False


#This is function for interaction with database



def show_net(net):
    valid_net(net)
    check_net(net)
    if valid_net(net) is True and check_net(net) is False:
        query = f"select * FROM networks WHERE net = '{net}' "
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    else:
        return {"message": "network is invalid or doesnt exist"}

def add_net(net, active, comment):
    valid_net(net)
    check_net(net)
    if valid_net(net) is True and check_net(net) is True:
        query = f"insert into networks (`net`, `active`, `comment`) value ('{ip}', '{active}', '{comment}')"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "network is invalid or doesnt exist"}

def del_net(net):
    valid_net(net)
    check_net(net)
    if valid_net(net) is True and check_net(net) is False:
        query = f"delete from networks where net = '{net}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "network is invalid or already deleted"}

def upd_net(net, active, comment):
    valid_net(net)
    check_net(net)
    if valid_net(net) is True and check_net(net) is False:
        query = f"update networks set `active` = '{active}', `comment` = '{comment}' where net = '{net}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "network is invalid or doesnt exist"}

def search_net():
    query = "SELECT * FROM networks" 
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
