FROM python:3.10-slim

WORKDIR /src

COPY requirements.txt /src

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

EXPOSE 80

CMD python3 -m uvicorn main:app --host 0.0.0.0 --port 80




