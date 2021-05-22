import easyocr
#快速识别图片中的文字ocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = reader.readtext('j.png',detail=0)
result="".join(result)
print(result)
