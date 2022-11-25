#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress


#This is function for check a conditions

def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

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
        return result
    else:
        return {"message": "ip-addres is invalid or doesnt exist"}

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
        return result
    else:
        return {"message": "ip-addres is invalid or already exist"}

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
        return result
    else:
        return {"message": "ip-addres is invalid or already deleted"}

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
        return result
    else:
        return {"message": "ip-addres is invalid or doesnt exist"}


def search_ip():
    query = "SELECT * FROM ipaddresses"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
