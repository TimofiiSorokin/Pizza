FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./server/requirements.txt .
RUN pip install -r requirements.txt
COPY ./server /code/
COPY ./server/entrypoint.sh /code/
ENTRYPOINT ["/code/entrypoint.sh"]