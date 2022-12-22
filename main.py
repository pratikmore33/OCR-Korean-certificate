from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile

from ocr import parse_image

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API For OCR"}

# Post request to upload image/pdf and get text
@app.post("/api/v1/ocr/")
async def ocr(file: UploadFile = File(...)):
    if file.content_type == "image/png" or file.content_type == "image/jpeg":
        contents = await file.read()
        result = parse_image(contents)
        return {"data": result}
    else:
        return {"error": "Please upload image file"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
