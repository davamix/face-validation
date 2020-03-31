FROM python:3.8.2

WORKDIR /usr/src/face-login

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

ADD ./requirements.txt ./

# Windows + CUDA 10.1 (https://pytorch.org/)
RUN pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install -r requirements.txt

ADD . .

CMD ["python", "src/main.py"]