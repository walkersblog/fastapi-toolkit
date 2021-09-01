import asyncio
import time
from datetime import timedelta

import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services.jokes import get_joke_async

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/jokes')
async def jokes(request: Request):
    start = time.time()

    results = await asyncio.gather(
        get_joke_async(),
        get_joke_async(),
        get_joke_async(),
        get_joke_async(),
        get_joke_async()
    )

    end = time.time()
    duration = timedelta(seconds=end - start)

    return templates.TemplateResponse('jokes.html', {'request': request, 'results': results, 'duration': duration})
