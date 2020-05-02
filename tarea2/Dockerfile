FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /mapsy
WORKDIR /mapsy
COPY requirements.txt /mapsy/
RUN pip install -r requirements.txt
COPY . /mapsy/
CMD python3 manage.py runserver 0.0.0.0:$PORT