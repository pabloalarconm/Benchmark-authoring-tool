FROM python:3.12.3-alpine3.19

COPY . /code

WORKDIR /code/script

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]