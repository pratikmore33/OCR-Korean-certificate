# 
FROM python:3.9



# Install curl for healthchecks
RUN apt install curl


# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir --upgrade -r requirements.txt


# Install tesseract
RUN apt-get update && apt-get install -y tesseract-ocr-all
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
RUN pip install opencv-python
RUN pip install pytesseract
RUN pip install numpy
RUN pip install Pillow
RUN pip install aiofiles
RUN pip install deskew

# Copy the app
COPY . .

# Expose the app's port
EXPOSE 8000

# Run the FastAPI server
ENTRYPOINT ["python", "-m"] 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]