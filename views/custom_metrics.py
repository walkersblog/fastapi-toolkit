import fastapi
from fastapi import Form
from starlette import status
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from metrics.click_counter import get_current_click_counter_value, increment_click_counter
from metrics.page_counter import increment_page_counter, get_current_page_counter_value

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/custom_metrics')
def metrics(request: Request):
    increment_page_counter()
    hits = get_current_page_counter_value()
    clicks = get_current_click_counter_value()
    return templates.TemplateResponse('custom_metrics.html', {'request': request,
                                                              'current_page_counter': hits,
                                                              'current_click_counter': clicks})


@router.post('/custom_metrics')
def metrics(request: Request, action: str = Form(...)):
    if action == 'click_counter':
        increment_click_counter()
        return fastapi.responses.RedirectResponse('/custom_metrics', status_code=status.HTTP_302_FOUND)
