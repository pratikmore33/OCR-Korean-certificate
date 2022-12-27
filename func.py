import cv2
import pytesseract
import re

def reg_pattern(image):
    img = cv2.imread(image)
    text = pytesseract.image_to_string(img,lang='kor',config='--psm 6')
    # pattern for registration no
    
   
   
    #registration no
    if  re.search(r'(등록번호)',text) == None:
        t1 = 'None'
    else:
        p1 = re.search(r'(등록번호)',text)
        t1 = text[p1.start():p1.end()+16]

    
    # date of birth
    if re.search(r'(생 년 월 일|생년월일)',text) == None:
        t2 = 'None'
    else:
        p2 = re.search(r'(생 년 월 일|생년월일)',text)
        t2 =text[p2.start():p2.end()+16]
    
    # date of opening 
    if re.search(r'(개업 년월일|개 업 연 뭘 일 :|개 업 연 월 일)',text)== None:
        t3 = 'None'
    else:
        p3 = re.search(r'(개업 년월일|개 업 연 뭘 일 :|개 업 연 월 일)',text)
        t3 =text[p3.start():p3.end()+16]
    
    # name of business
    if re.search(r'(상       호 ：|상      호 :|상     호 :|창      호 ：|상      호 ：)',text)== None:
        t4 = 'None'
    else:
        p4 = re.search(r'(상       호 ：|상      호 :|상     호 :|창      호 ：|상      호 ：)',text)
        t4 = text[p4.start():p4.end()+16]
    
    # location of business
    if re.search(r'(사 업 장 소 재 지|사업장소재지)',text)== None:
        t5 = 'None'
    else:
        p5 = re.search(r'(사 업 장 소 재 지|사업장소재지)',text)
        t5 = text[p5.start():p5.end()+28]

    # type of business
    if  re.search(r'(사 업 의 종 류|사업의 종류)',text)== None:
        t6 = 'None'
    else:
        p6 = re.search(r'(사 업 의 종 류|사업의 종류)',text)
        t6 = text[p6.start():p6.end()+13]

    final_str = t1+'\n'+t2+'\n'+t3+'\n'+t4+'\n'+t5+'\n'+t6
    return final_str