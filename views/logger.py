import datetime
import logging
import random

import fastapi
from fastapi import Form
from starlette.templating import Jinja2Templates
from starlette.requests import Request

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')


@router.get('/logger')
def logger(request: Request):
    return templates.TemplateResponse('logger.html', {'request': request})


@router.post('/logger')
def logger(request: Request, action: str = Form(...), custom_string_input: str = Form(...)):
    if action == 'logger_one':
        now = datetime.datetime.now()
        formatedate = now.strftime("%Y-%m-%d %H:%M:%S")
        error_string = f'[{formatedate}] "ERROR" Status: 500 "Message from Logger:" Internal Server Error'
        logger_one = logging.getLogger(__name__)
        logger_one.error(error_string)
        return templates.TemplateResponse('logger.html', {'request': request})

    if action == 'logger_two':
        number1 = random.randint(1000, 9999)
        number2 = random.randint(1000, 9999)
        now = datetime.datetime.now()
        formatedate = now.strftime("%Y-%m-%d %H:%M:%S")
        credit_card_string = f'[{formatedate}] "INFO" Status: 200 Customer Credit Card number 4321-4321-{number1}-{number2}'
        logger_two = logging.getLogger(__name__)
        logger_two.error(credit_card_string)
        return templates.TemplateResponse('logger.html', {'request': request})

    if action == 'custom_string':
        logger_input = logging.getLogger(__name__)
        logger_input.error(custom_string_input)
        return templates.TemplateResponse('logger.html', {'request': request})
