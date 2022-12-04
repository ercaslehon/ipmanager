from fastapi import FastAPI, HTTPException
from database.connectToDatabase import connectToDatabase
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from fastapi.responses import JSONResponse
from view import search_ip, show_ip, add_ip, del_ip, mod_ip, search_net, show_net, add_net, del_net, mod_net
#from app.models import IpAddresses, Networks

#Functionality Part
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


#IPADDRESSES


@app.get("/ip/search")
async def ip_search():
    return await search_ip()

@app.get("/ip/show")
async def ip_show(ip):
     result = await show_ip(ip)
     raise HTTPException( status_code = result['status'], detail = result['message'])
     

@app.get("/ip/add")
async def ip_add(ip, used, comment):
    result = await add_ip(ip, used, comment)
    print(result)
    raise HTTPException( status_code = result['status'], detail = result['message'])


@app.get("/ip/del")
async def ip_del(ip):
    result = await del_ip(ip)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/ip/mod")
async def ip_mod(ip, used, comment):
    result = await mod_ip(ip, used, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])


#NETWORKS

@app.get("/net/search")
async def net_search():
    return await search_net()

@app.get("/net/show")
async def net_show(net):
    result = await show_net(net)
    print(result)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/add")
async def net_add(net, active, comment):
    result = await add_net(net, active, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/del")
async def net_del(net):
    result = await del_net(net)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/mod")
async def net_mod(net, active, comment):
    result = await mod_net(net, active, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])


#REGISTER CONNETCT

register_tortoise(
    app,
    db_url="mysql://admin:secret@127.0.0.1:3306/ipmanager_db",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


