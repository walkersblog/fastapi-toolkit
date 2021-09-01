import asyncio
import time
from datetime import timedelta

import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services.async_sleep import async_sleep
from services.sync_sleep import sync_sleep

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/async_sleep')
async def async_sleep_demo(request: Request):

    start = time.time()
    results = await asyncio.gather(
        async_sleep(start, 1),
        async_sleep(start, 1),
        async_sleep(start, 1),
        async_sleep(start, 1),
        async_sleep(start, 1),
    )

    end = time.time()
    duration = timedelta(seconds=end - start)

    return templates.TemplateResponse('async_sleep_demo.html', {'request': request, 'results': results, 'duration': duration})


@router.get('/sync_sleep')
def sync_sleep_demo(request: Request):

    start = time.time()

    results = [
        sync_sleep(start, 1),
        sync_sleep(start, 1),
        sync_sleep(start, 1),
        sync_sleep(start, 1),
        sync_sleep(start, 1)
    ]

    end = time.time()
    duration = timedelta(seconds=end - start)

    return templates.TemplateResponse('sync_sleep_demo.html', {'request': request, 'results': results, 'duration': duration})