from fastapi import FastAPI
from database.connectToDatabase import connectToDatabase
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from fastapi.responses import JSONResponse
from view import search_ip, show_ip, add_ip, del_ip, upd_ip, search_net, show_net, add_net, del_net, upd_net
from app.models import IpAddresses, Networks
from tortoise.contrib.pydantic import pydantic_model_creator


#Functionality Part
app = FastAPI()
ip_pydantic = pydantic_model_creator(IpAddresses)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


#IPADDRESSES


@app.get("/ip/search")
async def ip_search():
    return await search_ip()

@app.get("/ip/show")
async def ip_show(ip):
    return await show_ip(ip)

@app.get("/ip/add")
async def ip_add(ip, used, comment):
    return await add_ip(ip, used, comment)

@app.get("/ip/del")
async def ip_del(ip):
    return await del_ip(ip)

@app.get("/ip/upd")
async def ip_upd(ip, used, comment):
    return await upd_ip(ip, used, comment)


#NETWORKS

@app.get("/net/search")
async def net_search():
    return await search_net()

@app.get("/net/show")
async def net_show(net):
    return await show_net(net)

@app.get("/net/add")
async def net_add(net, active, comment):
    return await add_net(net, active, comment)

@app.get("/net/del")
async def net_del(net):
    return await del_net(net)

@app.get("/net/upd")
async def net_upd(net, active, comment):
    return await upd_net(net, active, comment)


#REGISTER CONNETCT

register_tortoise(
    app,
    db_url="mysql://admin:secret@127.0.0.1:3306/ipmanager_db",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


