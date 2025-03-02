from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.templating import _TemplateResponse
from pathlib import Path

app = FastAPI()

# Set up templates directory
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/")
async def read_root(request: Request) -> _TemplateResponse:
    """Render the home page.

    Args:
        request (Request): The incoming request object

    Returns:
        _TemplateResponse: The rendered HTML template
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )