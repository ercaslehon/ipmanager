#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress
from logbook import Logger, StreamHandler, FileHandler
import sys

#This is function for logging

#StreamHandler(sys.stdout).push_application()
FileHandler('./logs/ipmanager.log').push_application()
log = Logger('ipmanager')

#This is function for check a conditions

#network validation function
def valid_net(net):
    try:
        ipaddress.ip_network(net)
        return True
    except:
        return False

#Function to check if there is no network in the table. True when doesnt exist, False when exist.
def check_d_exist_net(net):
    query = f"select * FROM networks WHERE net = '{net}' "
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        return True
    else:
        return False


#This is function for interaction with database



def show_net(net):
    if valid_net(net) is True:
        if check_d_exist_net(net) is False:
            query = f"select * FROM networks WHERE net = '{net}' "
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            status = 200
            return [result, status]
        else:
            result = {"message": "network is valid, but doesnt exist"}
            status = 404
            return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        return [result, status]

def add_net(net, active, comment):
    if valid_net(net) is True:
        if check_d_exist_net(net) is True:
            query = f"insert into networks (`net`, `active`, `comment`) value ('{net}', '{active}', '{comment}')"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            result1 = cursor.fetchall()
            result = show_net(net)[0]
            status = 200
            log.info(f'Added new network -> {net}')
            return [result, status]
        else:
            result = {"message": "network already exist", "check it": show_net(net)[0]}
            status = 412
            log.warn(f'Cant add new network -> {net}: Cause network already exist')
            return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        log.warn(f'Cant add new network -> {net}: Cause network is invalid')
        return [result, status]

def del_net(net):
    if valid_net(net) is True: 
        if check_d_exist_net(net) is False:
            query = f"delete from networks where net = '{net}'"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            result1 = cursor.fetchall()
            result = {"nessage": "network deleted"}
            status = 200
            log.info(f'Deleted old network -> {net}')
            return [result, status]
        else:
            result = {"message": "This network already deleted"}
            status = 412
            log.warn(f'Cant delete old network -> {net}: Cause network already deleted')
            return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        log.warn(f'Cant delete this network -> {net}: Cause network is invalid')
        return [result, status]

def upd_net(net, active, comment):
    if valid_net(net) is True:
        if check_d_exist_net(net) is False:
            old_version = show_net(net)[0]
            query = f"update networks set `active` = '{active}', `comment` = '{comment}' where net = '{net}'"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            result1 = cursor.fetchall()
            result = show_net(net)[0]
            status = 200
            log.info(f'{old_version} modify to {result}')
            return [result, status]
        else:
             result = {"message": "network valid, but doesnt exist."}
             status = 404
             log.warn(f'Cant modify this network -> {net}: Cause network doesnt exist.')
             return [result, status]
    else:
        result = {"message": "network is invalid"}
        status = 400
        log.warn(f'Cant modify this network -> {net}: Cause network is invalid')
        return [result, status]

def search_net():
    query = "SELECT * FROM networks" 
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
