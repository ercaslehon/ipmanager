#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress

#This is function for check a conditions

#network validation function
def valid_net(net):
    try:
        ipaddress.ip_network(net)
        return True
    except:
        return False

#Function to check if there is no network in the table. True when doesnt exist, False when exist.
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
        status = 200
        return [result, status]
    elif valid_net(net) is True and check_net(net) is True:
        result = {"message": "network is valid, but doesnt exist"}
        status = 404
        return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        return [result, status]

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
        status = 200
        return result
    elif valid_net(net) is True and check_net(net) is False:
        result = {"message": "network already exist", "check it": show_net(net)}
        status = 412
        return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        return [result, status]

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
        status = 200
        return [result, status]
    elif valid_net(net) is True and check_net(net) is True:
        result = {"message": "This network already deleted"}
        status = 412
        return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        return [result, status]

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
        status = 200
        return [result, status]
    elif valid_net(net) is True and check_net(net) is True:
        result = {"message": "network valid, but doesnt exist."}
        status = 404
        return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        return [result, status]

def search_net():
    query = "SELECT * FROM networks" 
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
