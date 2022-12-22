# 
FROM python:3.9

# Install tesseract
RUN apt-get update && apt-get install -y tesseract-ocr-all
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
RUN pip install opencv-python
RUN pip install pytesseract
RUN pip install numpy
RUN pip install Pillow

COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-m", "main"]
