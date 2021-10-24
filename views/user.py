import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")

router = fastapi.APIRouter()

@router.get('/user')
def index(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})