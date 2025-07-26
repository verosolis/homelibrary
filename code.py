#code from https://www.geeksforgeeks.org/how-to-make-a-barcode-reader-in-python/

# Importing libraries
import cv2
import pandas as pd
import os
from pyzbar.pyzbar import decode

from tkinter import ttk
from tkinter import *



def app():
    root = Tk()
    root.title("LIBRARY")

    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Button(frm, text="EXIT", command=root.destroy).grid(column=1, row=0)
    buttonADD =  ttk.Button(frm, text="ADD NEW BOOK", command=AddNewBook).grid(column=1, row=1)
    buttonUPDATE = ttk.Button(frm, text="UPDATE STATUS", command=UpdateStatus).grid(column=1, row=2)
    ttk.Button(frm, text="PPRINT BAR CODE", command=root.destroy).grid(column=1, row=3)

    
    
    root.mainloop()
    buttonADD.pack()
    buttonUPDATE.pack()

def AddNewBook():
    root2= Tk()
    root2.title("ADD NEW BOOK")

    frm2 = ttk.Frame(root2, padding=100)
    frm2.grid()
    entry = ttk.Entry(frm2, width = 50)
    entry.pack(pady=10)
    submit_button = ttk.Button(frm2, text="Get Input", command=get_input)
    submit_button.pack()
    root2.mainloop()

def get_input():
        user_text = entry.get()
        print(f"User entered: '{user_text}'")

def UpdateStatus():
    CamaraCodeTaker()
    BarcodeReader("barcode_read.png")
    

# Make one method to decode the barcode 
def BarcodeReader(image):
    found = 1 
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
        found = 0
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:  
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using 
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10), 
                          (255, 0, 0), 2)
             
            if barcode.data!="":
                dataframe1 = pd.read_excel('list.xlsx',index_col=None, header=None)

                for i in range(0,len(dataframe1)):
                    if str(dataframe1[4][i]) == str(barcode.data,'UTF-8'):                        
                        print('{:30s} {:30s} {:30s} {:30s}'.format( str(dataframe1[0][1]), str(dataframe1[1][1]), str(dataframe1[2][1]), str(dataframe1[3][1]) ) )
                        print('{:30s} {:30s} {:30s} {:30s}'.format( str(dataframe1[0][i]), str(dataframe1[1][i]), str(dataframe1[2][i]), str(dataframe1[3][i]) ) )
                        os.remove("./barcode_read.png")
                        break
                        


    if(not found):
        os.remove("./barcode_read.png")

def CamaraCodeTaker():
#https://www.youtube.com/watch?v=IhRfqiC29Ds&t=442s
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            print("EXITING CAMERA")
            break
        if key == 32: # spacebar SS
            img_name = "barcode_read.png"
            cv2.imwrite(img_name,frame)
            #print("CHEESE")
            break


    vc.release()
    cv2.destroyWindow("preview")


 
if __name__ == "__main__":
  # Take the image from user
    #image="bar.png"
    #BarcodeReader(image)
    #CamaraCodeTaker()
    #BarcodeReader("barcode_read.png")
    app()
