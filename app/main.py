from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes import products

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(products.router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    produtos = products.get_all_products()  # Simulação
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})
