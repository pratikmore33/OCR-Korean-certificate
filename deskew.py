from pdf2image import convert_from_path, convert_from_bytes
print('hello')
image = convert_from_path('US_Declaration.pdf',poppler_path=r'C:\Program Files\poppler-22.12.0\Library\bin')
print(type(image))
print(len(image))