from tortoise import Tortoise
from tortoise.models import Model


async def connectToDatabase(): 
    await Tortoise.init(
        db_url="mysql://admin:secret@127.0.0.1:3306/ipmanager_db",
        modules={"models": ["app.models"]}
    )

