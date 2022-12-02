from app.models import IpAddresses, Networks
from app.valid import valid_ip, valid_net
from tortoise.contrib.pydantic import pydantic_model_creator 

#functional part

ip_pydantic = pydantic_model_creator(IpAddresses)
net_pydantic = pydantic_model_creator(Networks)

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
            result = await ip_pydantic.from_queryset(IpAddresses.filter(ip = ip ))
            return result
        else:
            return {"message": "ip-address is valid, but doesnt exist"}
    else:
        return {"message" : "ip-address is invalid"}


async def add_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if await check_ip(ip) is False:
            await IpAddresses.create(ip = ip, used = used, comment = comment)
            result = await show_ip(ip)
            return result
        else:
            return {"message" : "ip-address is already exist"}
    else:
        return {"message":"ip-address is invalid"}


async def del_ip(ip):
    if valid_ip(ip) is True:
        if await check_ip(ip) is True:
            await IpAddresses.filter(ip = ip).delete()
            return {"message" :f"{ip} has been deleted"}
        else:
            return {"message" : "{ip} is address valid, but already doesnt exist"}
    else:
        return {"message" : "ip-address is invalid"}


async def upd_ip(ip, used, comment):
    if valid_ip(ip) is True:
        if await check_ip(ip) is True:
            old_version = await show_ip(ip)
            await IpAddresses.filter(ip = ip).update(used = used, comment = comment)
            new_version = await show_ip(ip)
            result = {"Before" : old_version, "after" : new_version}
            return result
        else:
            return {"message": "ip-address is valid, but doesnt exist. Try add ip."}
    else:
        {"message": "ip-addres is invalid"}




#NETWORKS



async def search_net():
    return await net_pydantic.from_queryset(Networks.all())


async def show_net(net):
    if valid_net(net) is True:
        if await check_net(net) is True:
            result = await net_pydantic.from_queryset(Networks.filter( network = net ))
            return result
        else:
            return {"message": "Network is valid, but doesnt exist"}
    else:
        return {"message" : "Network is invalid"}


async def add_net(net, active, comment):
    if valid_net(net) is True:
        if await check_net(net) is False:
            await Networks.create(network = net, active = active, comment = comment)
            result = await show_net(net)
            return result
        else:
            return {"message" : "Network is already exist"}
    else:
        return {"message" : "Network is invalid"}


async def del_net(net):
    if valid_net(net) is True:
        if await check_net(net) is True:
            await Networks.filter(network = net).delete()
            return {"message" :f"{net} has been deleted"}
        else:
            return {"message" : "{net} is address valid, but already doesnt exist"}
    else:
        return {"message" : "Network is invalid"}


async def upd_net(net, active, comment):
    if valid_net(net) is True:
        if await check_net(net) is True:
            old_version = await show_net(net)
            await Networks.filter(network = net).update(active = active, comment = comment)
            new_version = await show_net(net)
            result = {"Before" : old_version, "after" : new_version}
            return result
        else:
            return {"message": "Network is valid, but doesnt exist. Try add new network."}
    else:
        {"message": "Network is invalid"}
