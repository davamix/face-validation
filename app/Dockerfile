FROM python:3.8.2

WORKDIR /usr/src/face-login

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# ADD ./requirements.txt ./

# RUN pip install -r requirements.txt

ADD . .

CMD ["python", "src/main.py"]