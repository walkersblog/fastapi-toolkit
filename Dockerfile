FROM ubi8/python-39

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER 0
RUN mkdir /code
WORKDIR /code

RUN chown -R 1001:0 /code
USER 1001

COPY . /code/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python main.py