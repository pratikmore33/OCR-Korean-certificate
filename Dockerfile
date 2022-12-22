# 
FROM python:3.9

# Install tesseract
RUN apt-get update && apt-get install -y tesseract-ocr-all
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/
CMD ["python", "-m", "main"]
