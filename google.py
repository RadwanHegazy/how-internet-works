from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def home():
    return HTMLResponse(content=f"<h1>Welcome to Google.com</h1>")


@app.get('/test')
def home():
    return HTMLResponse(content=f"<h1>Welcome to Google.com</h1><br><p>This is test page</p>")
