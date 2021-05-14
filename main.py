from os import path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

html = ''
if path.isfile('index.html'):
    with open('index.html') as file:
        html = file.read()


@app.get("/")
async def root():
    return HTMLResponse(html)


@app.get('/audio')
def audio():
    au = open('file.wav', mode='rb')
    return StreamingResponse(au, media_type="audio/wav")


@app.get('/list_files')
def list_files(request: Request):
    files = ['a', 'b', 'c']

    return templates.TemplateResponse(
        "available_records.html.j2",
        {"request": request, "files": files},
    )
