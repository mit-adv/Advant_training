from fastapi import FastAPI,Request
from .core.database import Base
from .core.database import engine
from .api.v1 import auth,todo,admin,user
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="todo/templates")
app.mount('/static',StaticFiles(directory='app/static'),name='static')

@app.get("/")
def home(request: Request):
    return RedirectResponse('/todos/todo-page')

@app.get('/healthy')
def health_check():
    return {'status':"Healthy"}

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(admin.router)
app.include_router(user.router)