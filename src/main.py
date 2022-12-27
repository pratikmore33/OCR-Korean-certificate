from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from ocr import parse_image

import re

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "API For OCR"}

# Post request to upload image/pdf and get text
@app.post("/api/v1/ocr/")
async def ocr(file: UploadFile = File(...)):
    if file.content_type == "image/png" or file.content_type == "image/jpeg":
        contents = await file.read()
        result = parse_image(contents)

        # store image to public folder
        with open(f"static/{file.filename}", "wb") as buffer:
            buffer.write(contents)

        # get file url
        file_url = f"http://localhost:8000/static/{file.filename}"

        # check if business registration form
        if "등록번호" in result:
            data = parse_business_registration_form(result)
            return {"data": data, "file_url": file_url}

        return {"data": {
            "text": result,
        }, "file_url": file_url}
    else:
        return {"error": "Please upload image file"}

def parse_business_registration_form(text):
    #registration no
    if  re.search(r'(등록번호)',text) == None:
        t1 = 'None'
    else:
        p1 = re.search(r'(등록번호)',text)
        t1= text[p1.end():p1.end()+16]

    
    # date of birth
    if re.search(r'(생 년 월 일|생년월일)',text) == None:
        t2 = 'None'
    else:
        p2 = re.search(r'(생 년 월 일|생년월일)',text)
        t2 = text[p2.end():p2.end()+16]
    
    # date of opening 
    if re.search(r'(개업 년월일|개 업 연 뭘 일 :|개 업 연 월 일)',text)== None:
        t3 = 'None'
    else:
        p3 = re.search(r'(개업 년월일|개 업 연 뭘 일 :|개 업 연 월 일)',text)
        t3 =text[p3.end():p3.end()+16]
    
    # name of business
    if re.search(r'(상       호 ：|상      호 :|상     호 :|창      호 ：|상      호 ：)',text)== None:
        t4 = 'None'
    else:
        p4 = re.search(r'(상       호 ：|상      호 :|상     호 :|창      호 ：|상      호 ：)',text)
        t4 = text[p4.end():p4.end()+16]
    
    # location of business
    if re.search(r'(사 업 장 소 재 지|사업장소재지)',text)== None:
        t5 = 'None'
    else:
        p5 = re.search(r'(사 업 장 소 재 지|사업장소재지)',text)
        t5 = text[p5.end():p5.end()+28]

    # type of business
    if  re.search(r'(사 업 의 종 류|사업의 종류)',text)== None:
        t6 = 'None'
    else:
        p6 = re.search(r'(사 업 의 종 류|사업의 종류)',text)
        t6 = text[p6.end():p6.end()+13]

    return {'등록번호':t1,'생 년 월 일':t2,'개업 년월일':t3,'상       호':t4,'사 업 장 소 재 지':t5,'사 업 의 종 류':t6}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
