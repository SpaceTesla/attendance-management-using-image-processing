from PIL import Image, ImageEnhance
import pytesseract as tess
import matplotlib.pyplot as plt
import numpy as np
tess.pytesseract.tesseract_cmd = r"C:\Users\Meghana\AppData\Local\Programs\Tesseract-OCR\tesseract"
fh = open("text/image_paths.txt")
image_path_list = eval(fh.read())
print(image_path_list)
len_list = len(image_path_list)
for i in image_path_list:
    image = Image.open(i)
#image.show()#this opens photo viewer
#plt.imshow(image)

#convert image to black and white
    image = image.convert('L')

# image enhancements using ImageEnhance
    image = ImageEnhance.Contrast (image).enhance(2.5)
    image = ImageEnhance.Brightness(image).enhance(1.5)
    image = ImageEnhance.Sharpness (image) .enhance(2.5)


    transpose_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_image2 = image.transpose (Image.FLIP_TOP_BOTTOM)
    transpose_image3 = image.transpose(Image.ROTATE_90)
    transpose_image4 = image.transpose(Image.ROTATE_180)
    transpose_image5 = image.transpose(Image.ROTATE_270)
    transpose_image6 = image.transpose (Image.TRANSPOSE)
#viewing all different image orientations
    plt. figure(figsize=(10,10))
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
    plt.title("TRANSPOSE")

    
    for j in range(1,len_list+1):
        text = tess.image_to_string(transpose_image1)
        fh = open("text."+str(j)+".1.txt","w+")
        fh.write(text)
        #print(text)
        
        text = tess.image_to_string(transpose_image2)
        fh = open("text."+str(j)+".2.txt","w+")
        fh.write(text)
        print(text)
        
        text = tess.image_to_string(transpose_image3)
        fh = open("text."+str(j)+".3.txt","w+")
        fh.write(text)
        print(text)
        
        text = tess.image_to_string(transpose_image4)
        fh = open("text."+str(j)+".4.txt","w+")
        fh.write(text)
        print(text)
        
        text = tess.image_to_string(transpose_image5)
        fh = open("text."+str(j)+".5.txt","w+")
        fh.write(text)
        print(text)
        
        text = tess.image_to_string(transpose_image6)
        fh = open("text."+str(j)+".6.txt","w+")
        fh.write(text)
        print(text)
        
        text = tess.image_to_string(image)
        fh = open("text."+str(j)+".7.txt","w+")
        fh.write(text)
        print(text)