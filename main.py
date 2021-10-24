from fastapi import FastAPI
import uvicorn

from api import user_api, reason_api
from views import home, user, admin
import config 

# disable the /docs
app = FastAPI(docs_url='/docs', redoc_url=None)

app.include_router(user_api.router, prefix=config.PATH_PREFIX)
app.include_router(reason_api.router, prefix=config.PATH_PREFIX)
#app.include_router(res_api.router)
#app.include_router(home.router)
#app.include_router(user.router)
#app.include_router(admin.router)


if __name__ == '__main__':
    #from db.init_db import init_db
    #init_db()
    uvicorn.run(app, host=config.HOST_IP, port=config.HOST_PORT)

    
