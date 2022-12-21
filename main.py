"""
Created on Wed Nov 18 13:07:51 2020

@author: win10
"""
#pip install fastapi uvicorn

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import shutil
import ocr
import os


# 2. Create the app object
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


@app.post("/extract_text")
def extract_text(image: UploadFile = File(...)):
    temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
    text = ocr.read_image(temp_file)
    return {"filename": image.filename, "text": text}

def _save_file_to_disk(uploaded_file,path=".",save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path,save_as+extension)
    with open(temp_file,"wb")as buffer:
        shutil.copyfileobj(uploaded_file.file,buffer)
    return temp_file


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port = 8000)
#uvicorn main:app --reload