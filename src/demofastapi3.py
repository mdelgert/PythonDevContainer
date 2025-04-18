from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("fastapi.html", {"request": request})

@app.get("/sample-json", response_class=JSONResponse)
async def get_sample_json():
    sample_data = {
        "message": "This is a sample JSON response",
        "data": {
            "id": 1,
            "name": "Example User",
            "email": "user@example.com",
            "roles": ["admin", "user"],
            "active": True
        },
        "timestamp": "2025-04-17T12:00:00Z"
    }
    return JSONResponse(content=sample_data)