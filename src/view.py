from app.models import IpAddresses, Networks
from app.valid import valid_ip, valid_net
from tortoise.contrib.pydantic import pydantic_model_creator 
import sys
from logbook import Logger, StreamHandler, FileHandler


#functional part

ip_pydantic = pydantic_model_creator(IpAddresses)
net_pydantic = pydantic_model_creator(Networks)
FileHandler('./logs/ipmanager.log').push_application()
log = Logger('ipmanager')


async def check_ip(ip):
    result = await ip_pydantic.from_queryset(IpAddresses.filter(ip = ip ))
    if len(result) == 0:
        return False
    else:
        return True

async def check_net(net):
    result = await net_pydantic.from_queryset(Networks.filter(network = net ))
    if len(result) == 0:
        return False
    else:
        return True



#IPADDRESSES

async def search_ip():
    return await ip_pydantic.from_queryset(IpAddresses.all())


async def show_ip(ip):
    if valid_ip(ip) is True:
        if await check_ip(ip) is True:
            message  = await ip_pydantic.from_queryset(IpAddresses.filter(ip = ip ))
            result = {"message" : message, "status" : 200}
            return result
        else:
            message = {"message" : "ip-address is valid, but doesnt exist"}
            result = {"message" : message, "status" : 404}
            return result
    else:
        message = {"message" : "ip-address is invalid"}
        result = {"message" : message, "status" : 400}
        return result


async def add_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if await check_ip(ip) is False:
            await IpAddresses.create(ip = ip, used = used, comment = comment)
            message = {"IP":"has been added", "Check It" : await show_ip(ip)}
            log.info(f'Added new IP -> {ip}')
            result = {'message' : message, 'status' : 200}
            return result
        else:
            log.warn(f'Cant add new IP -> {ip} : Cause IP already exist')
            message = {"IP" : "already exist", "check it" : await show_ip(ip)}
            result = {"message" : message, "status" : 412}
            return message
    else:
        log.warn(f'Cant add new IP -> {ip}: Cause IP is invalid')
        message = {"message" : "ip-address is invalid"}
        result = {'message': message, 'status': 400}
        return result


async def del_ip(ip):
    if valid_ip(ip) is True:
        if await check_ip(ip) is True:
            await IpAddresses.filter(ip = ip).delete()
            log.info(f'Deleted old IP -> {ip}')
            message = {"message" : f"{ip} has been deleted"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Cant delete old IP -> {ip}: Cause IP already deleted')
            message = {"message" : "This ip-adress already deleted"}
            result = {'message': message, 'status': 404}
            return result
    else:
        log.warn(f'Cant delete this IP -> {ip}: Cause IP is invalid')
        message = {"message" : "ip-addres is invalid"}
        result = {'message': message, 'status': 400}
        return result

async def upd_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if await check_ip(ip) is True:
            old_version = await show_ip(ip)
            await IpAddresses.filter(ip = ip).update(used = used, comment = comment)
            new_version = await show_ip(ip)
            log.info(f'{old_version} modify to {new_version}')
            message = {"IP" : "Has been updated", "Check It" : new_version}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Cant modify this IP -> {ip}: Cause IP doesnt exist.')
            message = {"message" : "IP-address valid, but doesnt exist. Try add ip."}
            result = {'message' : message, 'status': 404}
            return result
    else:
        log.warn(f'Cant modify this IP -> {ip}: Cause IP is invalid')    
        message  = {"message" : "ip-address is invalid"}
        result = {'message': message, 'status': 400}
        return result



#NETWORKS



async def search_net():
    return await net_pydantic.from_queryset(Networks.all())


async def show_net(net):
    if valid_net(net) is True:
        if await check_net(net) is True:
            message = await net_pydantic.from_queryset(Networks.filter( network = net ))
            result = {"message" : message, "status" : 200}
            return result
        else:
            message = {"message": "Network is valid, but doesnt exist"}
            result = {"message" : message, "statis" : 400}
            return result
    else:
        message = {"message" : "Network is invalid"}
        result = {"message" : message, "status" : 400}


async def add_net(net, active, comment):
    if valid_net(net) is True:
        if await check_net(net) is False:
            await Networks.create(network = net, active = active, comment = comment)
            log.info(f'Added new network -> {net}')
            message = {"network": "Has been added", "check it" : await show_net(net)}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Cant add new network -> {net}: Cause network already exist')
            message = {"network" : "already exist", "check it" : await show_net(net)}
            result = {'message': message, 'status': 412}
            return result
    else:
        result = {'message': message, 'status': 412}
        message = {"message": "network is invalid"}
        result = {'message': message, 'status': 400}
        return result


async def del_net(net):
    if valid_net(net) is True:
        if await check_net(net) is True:
            await Networks.filter(network = net).delete()
            log.info(f'Deleted old network -> {net}')
            message = {"message": "network deleted"}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Cant delete old network -> {net}: Cause network already deleted')
            message = {"message": "This network already deleted"}
            result = {'message': message, 'status': 412}
            return result
    else:
        log.warn(f'Cant delete this network -> {net}: Cause network is invalid')
        message = {"message": "network is invalid"}
        result = {'message': message, 'status': 400}
        return result


async def upd_net(net, active, comment):
    if valid_net(net) is True:
        if await check_net(net) is True:
            old_version = await show_net(net)
            await Networks.filter(network = net).update(active = active, comment = comment)
            new_version = await show_net(net)
            log.info(f'{old_version} modify to {new_version}')
            message = {"Network" : "has been updated", "check it": new_version}
            result = {'message': message, 'status': 200}
            return result
        else:
            log.warn(f'Cant modify this network -> {net}: Cause network is doesnt exist')
            message = {"message": "network is valid, but doesnt exist"}
            result = {'message': message, 'status': 404}
            return result
    else:
        log.warn(f'Cant modify this network -> {net}: Cause network is invalid')
        message = {"message": "network is invalid"}
        result = {'message': message, 'status': 400}
        return result
