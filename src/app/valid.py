import ipaddress

def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        #log.info(f'valid IP True -> {ip}')
        return True
    except:
        return False

def valid_net(net):
    try:
        ipaddress.ip_network(net)
        return True
    except:
        return False
