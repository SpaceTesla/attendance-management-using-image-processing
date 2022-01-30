from PIL import Image
import pytesseract as tess
import matplotlib.pyplot as plt
import numpy as np
tess.pytesseract.tesseract_cmd = r"C:\Users\Meghana\AppData\Local\Programs\Tesseract-OCR\tesseract"
image = Image.open("C:\\Users\\Meghana\\workshop\\ocrpic1.png")
#image.show()#this opens photo viewer
#plt.imshow(image)


#displaying some properties
print(image.size)
print(image.format)
print(image.mode)

transpose_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
transpose_image2 = image.transpose (Image. FLIP_TOP_BOTTOM)
transpose_image3 = image.transpose( Image. ROTATE_90)
transpose_image4 = image.transpose( Image. ROTATE_180)
transpose_image5 = image.transpose(Image.ROTATE_270)
transpose_image6 = image.transpose (Image. TRANSPOSE)
#displaying images
'''plt. figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(transpose_image1)
plt.title("FLIP_LEFT_RIGHT")
plt.subplot(3,2,2)

plt. imshow(transpose_image2)
plt.title("FLIP_TOP_BOTTOM")
plt.subplot(3,2,3)
plt.imshow(transpose_image2)
plt.title("ROTATE_90")
plt.subplot(3,2,4)

plt. imshow(transpose_image4)
plt.title("ROTATE_180")
plt.subplot(3,2,5)
plt.imshow(transpose_image5)
plt.title("ROTATE_270")
plt.subplot(3,2,6)
plt.imshow(transpose_image6)
plt.title("TRANSPOSE")'''

#ocr application on images of all orientations
text = tess.image_to_string(transpose_image1)
print(text)
text = tess.image_to_string(transpose_image2)
print(text)
text = tess.image_to_string(transpose_image3)
print(text)
text = tess.image_to_string(transpose_image4)
print(text)
text = tess.image_to_string(transpose_image5)
print(text)
text = tess.image_to_string(transpose_image6)
print(text)
text = tess.image_to_string(image)
print(text)