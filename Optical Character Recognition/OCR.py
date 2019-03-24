from PIL import Image
import pytesseract
import cv2

#img = Image.open('image/D2HENNaUgAE_x59 - Copy.png');
mj = cv2.imread("image/ez.jpg")
img = cv2.imread("image/ez.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grays = cv2.cvtColor(mj, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray, lang='eng');
test = pytesseract.image_to_string(grays, lang='eng');

print(text)
print(test)
