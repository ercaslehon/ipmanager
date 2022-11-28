#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress


#This is function for check a conditions

#ip validation function
def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

#Function to check if there is no IP in the table. True when doesnt exist, False when exist.
def check_ip(ip):
    valid_ip(ip)
    if valid_ip(ip) is True:
        query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
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


def show_ip(ip):
    valid_ip(ip)
    check_ip(ip)
    if valid_ip(ip) is True and check_ip(ip) is False:
        query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        status = 200
        return [result, status]
    elif valid_ip(ip) is True and check_ip(ip) is True:
        result = {"message": "ip-addres valid, but doesnt exist"}
        status = 404
        return [result, status]
    else:
        result = {"message": "ip-adres are invalid"}
        status = 400
        return [result, status]
    


def add_ip(ip, used, comment):
    valid_ip(ip)
    check_ip(ip)
    if valid_ip(ip) is True and check_ip(ip) is True:
        query = f"insert into ipaddresses (`ip`, `used`, `comment`) value ('{ip}', '{used}', '{comment}')"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        status = 200
        return [result, status]
    elif valid_ip(ip) is True and check_ip(ip) is False:
        result = {"message": "ip-adres already exist", "check it": show_ip(ip)}
        status = 412
        return [result, status]
    else:
        result = {"message": "ip-addres is invalid"}
        status = 400
        return [result, status]

def del_ip(ip):
    valid_ip(ip)
    check_ip(ip)
    if valid_ip(ip) is True and check_ip(ip) is False:
        query = f"delete from ipaddresses where ip = '{ip}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        status = 200
        return [result, status]
    elif valid_ip(ip) is True and check_ip(ip) is True:
        result = {"message": "This ip-adress already deleted"}
        status = 412
        return [result, status]
    else:
        result = {"message": "ip-addres is invalid"}
        status = 400
        return [result, status]

def upd_ip(ip, used, comment):
    valid_ip(ip)
    check_ip(ip)
    if valid_ip(ip) is True and check_ip(ip) is False:
        query = f"update ipaddresses set `used` = '{used}', `comment` = '{comment}' where ip = '{ip}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        status = 200
        return [result, status]
    elif valid_ip(ip) is True and check_ip(ip) is True:
        result = {"message": "ip-addres valid, but doesnt exist."}
        status = 404
        return [result, status]
    else:
        result = {"message": "ip-addres is invalid"}
        status = 400
        return [result, status]

def search_ip():
    query = "SELECT * FROM ipaddresses"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
