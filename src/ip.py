#!/opt/ipmanager/venv/bin/python3
from getpass import getpass
from mysql.connector import connect, Error



def search_ip():
    query = "SELECT * FROM ipaddresses" 
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def show_ip(ip):
        query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
        conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def add_ip(ip, used, comment):
    query = f"insert into ipaddresses (`ip`, `used`, `comment`) value ('{ip}', '{used}', '{comment}')"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result

def del_ip(ip):
    query = f"delete from ipaddresses where ip = '{ip}'"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result

def upd_ip(ip, used, comment):
    query = f"update ipaddresses set `used` = '{used}', `comment` = '{comment}' where ip = '{ip}'"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    return result
