FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /burguer
WORKDIR /burguer
COPY requirements.txt /burguer/
RUN pip install -r requirements.txt
COPY . /burguer/
CMD python3 manage.py runserver 0.0.0.0:$PORT