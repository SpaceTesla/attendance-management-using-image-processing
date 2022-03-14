# ------------------ Imports ------------------ #

#qualitative enhancement of image to enable better results with ocr
from PIL import Image, ImageEnhance

#ocr
import pytesseract as tess

#geometrical manipulation of image
import matplotlib.pyplot as plt  


#extracting path of image which the user would have input in the file 
#dialogue box part of the program

f1 = open("text/tess_paths.txt", 'r')
tess_path = f1.read()

#extracting path of tesseract which the user would have input in the file dialogue box
#part of the program

tess.pytesseract.tesseract_cmd = tess_path


#opening image file in a file handle fh to enable manipulation
fh = open("text/image_paths.txt")


#path of each image is stored as an independent element in a list
image_path_list = eval(fh.read())

#extracting length of image_path_list to facilitate the formation of mutiple
#text files through iteration later on
len_list = len(image_path_list)
for i in image_path_list:
    image = Image.open(i)

#image.show()#this opens photo viewer
#plt.imshow(image)

#convert image to black and white
    image = image.convert('L')

# image enhancements using ImageEnhance
    #specifies the degree of enhancement of image. 1 will be the original value, 
    #more than 1 will signify increment in a particular aspect whereas less than 1 will signify the opposite.
    
    Contrast_factor = 2.5
    Brightness_factor = 1.5
    Sharpness_factor = 2.5
    
    image = ImageEnhance.Contrast (image).enhance(Contrast_factor)
    
    image = ImageEnhance.Brightness(image).enhance(Brightness_factor)
    
    image = ImageEnhance.Sharpness (image) .enhance(Sharpness_factor)

# flipping the image in various orientations to negate the orientation error in the uploaded image(if any).
    transpose_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    transpose_image2 = image.transpose (Image.FLIP_TOP_BOTTOM)
    
    transpose_image3 = image.transpose(Image.ROTATE_90)
    
    transpose_image4 = image.transpose(Image.ROTATE_180)
    
    transpose_image5 = image.transpose(Image.ROTATE_270)
    
    transpose_image6 = image.transpose (Image.TRANSPOSE)


#viewing all different image orientations, specifing thier axes,size,title to facilitate further image processing
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

    
    #creating an loop in which an unspecified number of uploaded images will be rotated and 
    #be processed by tesseract after which output obtained is converted into 7 textfiles(for each image),
    #1 textfile for 1 particular orientation.  
    
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