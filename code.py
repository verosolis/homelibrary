#code from https://www.geeksforgeeks.org/how-to-make-a-barcode-reader-in-python/

# Importing library
import cv2
import pandas as pd
import os
from pyzbar.pyzbar import decode
  
# Make one method to decode the barcode 
def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
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
               
            # Print the barcode data
##                print(barcode.data)
##                print(barcode.type)
                dataframe1 = pd.read_excel('list.xlsx',index_col=None, header=None)
                #Col Row
##                print(dataframe1[1][2]) 
##                print(dataframe1 [3][4])
##                print(dataframe1 [4][4])
##                print(str(barcode.data,'UTF-8'))
##                print(len(dataframe1))
                for i in range(0,len(dataframe1)):
                    if str(dataframe1[4][i]) == str(barcode.data,'UTF-8'):
                        #print(str(dataframe1[0][1]),str(dataframe1[0][i]),str(dataframe1[0][2]),str(dataframe1[1][i]),str(dataframe1[0][3]),str(dataframe1[3][i]),str(dataframe1[0][4]),str(dataframe1[4][i]))
                        #print(str(dataframe1[0][1]), str(dataframe1[1][1]), str(dataframe1[2][1]), str(dataframe1[3][1]))
                        #print(str(dataframe1[0][i]), str(dataframe1[1][i]), str(dataframe1[2][i]), str(dataframe1[3][i]))
                        print('{:30s} {:30s} {:30s} {:30s}'.format( str(dataframe1[0][1]), str(dataframe1[1][1]), str(dataframe1[2][1]), str(dataframe1[3][1]) ) )
                        
                        print('{:30s} {:30s} {:30s} {:30s}'.format( str(dataframe1[0][i]), str(dataframe1[1][i]), str(dataframe1[2][i]), str(dataframe1[3][i]) ) )

                        os.remove("./barcode_read.png")
                    else:
                        print("CODE NOT FOUND")
                        os.remove("./barcode_read.png")
                
    #Display the image
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
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
    CamaraCodeTaker()
    BarcodeReader("barcode_read.png")