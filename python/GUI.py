# Final GUI File
# Project by: Varun Shankar Duddu, Vishal S Hegde, Shivansh Karan
# This it the first part of the project created by Shivansh karan

# ----------------------- Imports ----------------------- #

from tkinter import *
from tkinter import filedialog
import webbrowser



# ---------------- Window Initialization ---------------- #

## Creating tkinter window

root = Tk()                                      # This is the window object where all the magic happens
root.title("Attendace Management System")        # Title of the window
#root.geometry("1020x500")                       # Size of the window



## Creating frame to store everything except for the status bar

frame1 = Frame(root)         # Not required if not using the status bar
frame1.pack(padx=5, pady=5)




# ---------------------- Image part --------------------- #

image_path_list = []         # This will store paths of all the images


## Creating variables using loops ---
#* [help](https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop)

for i in range(1,6):
    globals()["var%s" % i] = StringVar()         # Creates 5 variables var1, var2, var3...
    globals()["path_label_%s" %i] = Label(       # Creates 5 variables path_label_1, path_label_2,...
        frame1,
        textvariable = globals()["var%s" % i],   # text variable to set the value as file path
        font=("JetBrains Mono", 20),
        bd=3,                                    # just gives a good looking border
        relief=SUNKEN,                           # appears like sunken
        anchor= E,                               # anchors (fixes) the text ot the east (right) <E : east>
        width=40,
    )

z = 1    # it is used as an argument in the function below
         # it connects global and the local scope of the @attach_image_fn


## Function to attach image 
def attach_image_fn(e):   # e represents the number of function call. for ex. e=1 for the first function call
                          # e is used to choosing variables and assigning changes in a loop
                        
    # Making them globles to make changes to them globally
    global path_label_1, path_label_2, path_label_3, path_label_4, path_label_5
    global z, image_path_list
    
    # To receive paths of images 
    image_path = filedialog.askopenfilename(
        filetypes=(    # different file types for different image formats
            ("png files", "*.png"),
            ("jpeg files", "*.jpeg"),
            ("jpg files", "*.jpg"),            
        )
    )
    
    image_path_list.append(image_path)        # adds the paths to the path list
    
    # To set the value of var1, to var6 as file name for corresponding valuses of 'e'
    globals()["var%s" % e].set(image_path)    # when e=1, var1.set(image_path), and so on...
    
    # ! Don't use (["path_label_%s" %e]) <in brackets> or u will get an error
    globals()["path_label_%s" %e].grid(row=e, column=0,         # Corresponding e value assigned to the row
                                         padx=5, pady=5,        # Gives external padding
                                         sticky=W)              # Sticks (fixes) label to west (left) <W : west>

    # if no file selected
    if len(image_path) <= 2:    
        globals()["var%s" % e].set("No file selected")     # Displays no file selected if so
        (globals()["path_label_%s" %e]).config(
            font=("JetBrains Mono", 20, "italic"), fg="red")

    z+=1   # Very important, helps in iteration


# Filedialog button


attach_img_btn = Button(
    frame1,
    width=38,
    state=NORMAL,
    text = "attach image",
    font = ("JetBrains Mono", 20,),
    command = lambda: attach_image_fn(z),        # Lambda here is an anonymous function 
).grid(row=0, column=0, padx=5, pady=5,)




# --------------------- Excel Part ---------------------- #

## Excel label (Will contain the path of the excel file)

xl_text = StringVar()

xl_label = Label(            # Following the same procedure as earlier
    frame1,
    textvariable=xl_text,
    font=("JetBrains Mono", 20),
    bd=3,
    relief=SUNKEN,
    anchor= E,
    width=40,
)


## Excel attach function

def attach_xl_fn():     # To be used with the button below
    global xl_path
    xl_path = filedialog.askopenfilename(
        filetypes=(
            ("excel file", "*.xlsx"),
        )
    )
    xl_text.set(xl_path)
    xl_label.grid(row=1, column=2, padx=5, pady=5)
    # if no file selected
    if len(xl_path) <= 2:    
        xl_text.set("No file selected")     # Displays no file selected if so
        xl_label.config(
            font=("JetBrains Mono", 20, "italic"), fg="red")



## Excel button

attach_xl_btn = Button(
    frame1,
    text = "Attach Excel Sheet",
    font = ("JetBrains Mono", 20,),
    width=39,
    command = attach_xl_fn
).grid(row=0, column=2, padx=5, pady=5)


# ------------------- Tesseract Part -------------------- #

## Tesseract label 

tes_text = StringVar()

tes_label = Label(            # Following the same procedure as earlier
    frame1,
    textvariable=tes_text,
    font=("JetBrains Mono", 20),
    bd=3,
    relief=SUNKEN,
    anchor= E,
    width=40,
)


## Tesseract Function

def tess_fn():
    global tes_path
    tes_path = filedialog.askopenfilename(
        filetypes=(
            ("windows executable", "*.exe"),
        )
    )
    tes_text.set(tes_path)
    tes_label.grid(row=6, column=2, padx=5, pady=5)
    # if no file selected
    if len(tes_path) <= 2:    
        tes_text.set("No file selected")     # Displays no file selected if so
        tes_label.config(
            font=("JetBrains Mono", 20, "italic"), fg="red")


## Tesserect Button

tes_btn = Button(
    frame1,
    text = "Attach Tesseract Path",
    font = ("JetBrains Mono", 20,),
    width=39,
    command = tess_fn

).grid(row=5, column=2, padx=5, pady=5)


# ----------------- Help & Exit Button ------------------ #


# Second frame
frame2 = Frame(root)                        # includes help and exit buttons
frame2.pack(padx=5, pady=5)

## Help function

def help_fun():         # To be used with @help_btn below
    github_link = "https://github.com/SpaceTesla/attendance-management-using-image-processing"
    webbrowser.open_new_tab(github_link)


## Help button

help_btn = Button(frame2, text="Help", command= help_fun)
help_btn.grid(row=1, column=1)

## Exit button 

exit_btn = Button(frame2, text="Exit", command= root.destroy)
exit_btn.grid(row=1, column=2)


# --------------------- Status Bar ---------------------- #

## Status bar at the bottom

status_label = Label(
    root,
    text="You can select up to 5 images and 1 excel sheet  ",
    font = ("JetBrains Mono",12),
    bd=3,
    relief=SUNKEN,
    anchor=E,                     # Text is aliened to the east (right)
).pack(fill=X,                    # To fill the entire space in the botton like x-axis line
       side=BOTTOM,               # The side to fill 
       ipady=2,)




# ------------------------------------------------------- #


root.mainloop()         # Main loop loops throughout the process until you close the window
# So the tkinter part is closed here




# ---------------- File Handling Part ------------------- #

## Image text file

f1 = open("text/image_paths.txt","w")
f1.write(str(image_path_list))
f1.close()


## Excel text file

try:                    # If xl_path is not defined we will get an error
    f2 = open("text/excel_paths.txt","w")
    f2.write(str(xl_path))
    f2.close()
    
except NameError:       # Case arises when we don't attach any excel file and close the window
    pass

# ------------------------- EOF ------------------------- #
