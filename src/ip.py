#!/opt/ipmanager/venv/bin/python3
from getpass import getpass
from mysql.connector import connect, Error

def valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def show_ip(ip):
    valid_ip(ip)
    if valid_ip(ip) is True:
        query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    else:
        return {"message": "ip-addres is invalid"}

def add_ip(ip, used, comment):
    valid_ip(ip)
    if valid_ip(ip) is True:
        query = f"insert into ipaddresses (`ip`, `used`, `comment`) value ('{ip}', '{used}', '{comment}')"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "ip-addres is invalid"}

def del_ip(ip):
    valid_ip(ip)
    if valid_ip(ip) is True:
        query = f"delete from ipaddresses where ip = '{ip}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "ip-addres is invalid"}

def upd_ip(ip, used, comment):
    valid_ip(ip)
    if validIP(ip) is True:
        query = f"update ipaddresses set `used` = '{used}', `comment` = '{comment}' where ip = '{ip}'"
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    else:
        return {"message": "ip-addres is invalid"}


def search_ip():
    query = "SELECT * FROM ipaddresses"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
