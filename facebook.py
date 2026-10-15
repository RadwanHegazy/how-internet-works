from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def home():
    return HTMLResponse(content=f"<h1>Welcome to facebook.com</h1>")

