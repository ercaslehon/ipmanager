#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
import ipaddress
from logbook import Logger, StreamHandler, FileHandler
import sys

#This is function for logging

#StreamHandler(sys.stdout).push_application()
FileHandler('./logs/ipmanager.log').push_application()
log = Logger('ipmanager')


#This is functions for check a conditions

#ip validation function
def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        #log.info(f'valid IP True -> {ip}')
        return True
    except:
        return False

#Function to check if there is no IP in the table. True when doesnt exist, False when exist.
def check_d_exist_ip(ip):
    query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        return True
    else:
        return False
    
    
#This is function for interaction with database


def show_ip(ip):
    if valid_ip(ip) is True:
        if check_d_exist_ip(ip)is False:
            query = f"select * FROM ipaddresses WHERE ip = '{ip}' "
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            status = 200
            return [result, status]
        else:
            result = {"message": "ip-addres valid, but doesnt exist"}
            status = 404
            return [result, status]
    else:
        result = {"message": "ip-adres are invalid"}
        status = 400
        return [result, status]

def add_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if check_d_exist_ip(ip) is True:
            query = f"insert into ipaddresses (`ip`, `used`, `comment`) value ('{ip}', '{used}', '{comment}')"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            internal_result = cursor.fetchall()
            message = {"ip-addres added, check it": show_ip(ip)[0]}
            result = {'message': message, 'status': 200}
            log.info(f'Added new IP -> {ip}')
            return result
        else:
            message = {"ip-addres already exist, check it": show_ip(ip)[0]}
            log.warn(f'Cant add new IP -> {ip}: Cause IP already exist')
            result = {'message': message, 'status': 412}
            return result
    else:
        message = {"message": "ip-addres is invalid"}
        log.warn(f'Cant add new IP -> {ip}: Cause IP is invalid')
        result = {'message': message, 'status': 400}
        return result

def del_ip(ip):
    if valid_ip(ip) is True:
        if check_d_exist_ip(ip) is False:
            query = f"delete from ipaddresses where ip = '{ip}'"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            internal_result = cursor.fetchall()
            message = {"message": "ip-addres deleted"}
            result = {'message': message, 'status': 200}
            log.info(f'Deleted old IP -> {ip}')
            return result
        else:
            message = {"message": "This ip-adress already deleted"}
            log.warn(f'Cant delete old IP -> {ip}: Cause IP already deleted')
            result = {'message': message, 'status': 412}
            return result
    else:
        message = {"message": "ip-addres is invalid"}
        result = {'message': message, 'status': 400}
        log.warn(f'Cant delete this IP -> {ip}: Cause IP is invalid')
        return result

def upd_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if check_d_exist_ip(ip) is False:
            old_version = show_ip(ip)[0]
            query = f"update ipaddresses set `used` = '{used}', `comment` = '{comment}' where ip = '{ip}'"
            conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            internal_result = cursor.fetchall()
            new_version = show_ip(ip)[0]
            message = {"ip address has been updated, check it": show_ip(ip)[0]}
            result = {'message': message, 'status': 200}
            log.info(f'{old_version} modify to {new_version}')
            return result
        else:
            message = {"message": "ip-addres valid, but doesnt exist. Try add ip."}
            result = {'message': message, 'status': 404}
            log.warn(f'Cant modify this IP -> {ip}: Cause IP doesnt exist.')
            return result
    else:
        message  = {"message": "ip-addres is invalid"}
        result = {'message': message, 'status': 400}
        log.warn(f'Cant modify this IP -> {ip}: Cause IP is invalid')
        return result

def search_ip():
    query = "SELECT * FROM ipaddresses"
    conn = connect(host="127.0.0.1", user="admin", password="secret", database="ipmanager_db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
