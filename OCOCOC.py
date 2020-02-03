from PIL import Image
from PIL import ImageFilter
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'D:\ract\tesseract.exe'

img = Image.open("test29.jpg")
new_size = tuple(2*x for x in img.size)
img = img.filter(ImageFilter.DETAIL)
# img = img.resize(new_size, Image.BILINEAR)
img.show()

#辨識的語言是否有繁體中文
# text = pytesseract.image_to_string( img,lang="chi_tra")
text = pytesseract.image_to_string( img)

print(text)

with open("./0001.txt","w",1,"utf-8") as fn:
    fn.write(text)