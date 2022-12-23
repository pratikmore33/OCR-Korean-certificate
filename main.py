from typing import Union
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from ocr import parse_image

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
        if "법인등록번호" in result:
            data = parse_business_registration_form(result)
            return {"data": data, "file_url": file_url}

        return {"data": {
            "text": result,
        }, "file_url": file_url}
    else:
        return {"error": "Please upload image file"}

def parse_business_registration_form(content):
    # 법인등록번호
    corporate_registration_number=content[content.find("법인등록번호 : ")+len("법인등록번호 : "):content.find("법인등록번호 : ")+len("법인등록번호 : ")+13]
    
    # 법인명
    # corporate_name=content[content.find("법인명 : ")+len("법인명 : "):content.find("법인명 : ")+len("법인명 : ")+13]

    # 사업장 소재지
    business_location=content[content.find("사업장 소재지 : ")+len("사업장 소재지 : "):content.find("본 점 소 재 지 : ")]

    # 본점 소재지
    head_office_location=content[content.find("본 점 소 재 지 : ")+len("본 점 소 재 지 : "):content.find("사 업 의 _종 류 、|업태|")]

    # 사업의 종류
    business_type=content[content.find("사 업 의 _종 류 、|업태|")+len("사 업 의 _종 류 、|업태|"):content.find("목   블록체인기반시스템소프트웨어개발및공")]

    # 사업의 종류
    business_type=content[content.find("사 업 의 _종 류 、|업태|")+len("사 업 의 _종 류 、|업태|"):content.find("목   블록체인기반시스템소프트웨어개발및공")]

    return {"법인등록번호": corporate_registration_number, 
    # "법인명":corporate_name,
    "사업장 소재지": business_location, 
    "본점 소재지": head_office_location,
     "사업의 종류": business_type,
     }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
