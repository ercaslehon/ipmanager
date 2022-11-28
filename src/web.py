#!/opt/ipmanager/venv/bin/python3
from mysql.connector import connect, Error
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ip import show_ip, search_ip, add_ip, del_ip, upd_ip
from net import show_net, search_net, add_net, del_net, upd_net


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "There are two sections. The IP section is responsible for the IP addresses in the table, the net section is responsible for the networks. The currently available interaction methods are: search, show, add, del, upd. There will be more functionality in the future)"}


#There is a manager for IP


@app.get("/ip/upd")
async def ip_upd(ip, used, comment):
    return JSONResponse(upd_ip(ip, used, comment)[0], status_code=show_ip(ip)[1])

@app.get("/ip/del")
async def ip_del(ip):
    return JSONResponse(del_ip(ip)[0], status_code=show_ip(ip)[1])

@app.get("/ip/add")
async def ip_add(ip, used, comment):
    return JSONResponse(add_ip(ip, used, comment)[0], status_code=show_ip(ip)[1])

@app.get("/ip/show")
async def ip_show(ip):
    return JSONResponse(show_ip(ip)[0], status_code=show_ip(ip)[1])


@app.get("/ip/search")
async def ip_search():
    return JSONResponse(search_ip())



#There is a manager for NETWORK



@app.get("/net/upd")
async def net_upd(net, active, comment):
    return JSONResponse(upd_net(net, active, comment)[0], status_code=show_ip(ip)[1])

@app.get("/net/del")
async def net_del(net):
    return JSONResponse(del_net(net)[0], status_code=show_ip(ip)[1])

@app.get("/net/add")
async def net_add(net, active, comment):
    return JSONResponse(add_net(net, active, comment)[0], status_code=show_ip(ip)[1])

@app.get("/net/show")
async def net_show(net):
    return JSONResponse(show_net(net)[0], status_code=show_ip(ip)[1])

@app.get("/net/search")
async def net_search():
    return JSONResponse(search_net())
